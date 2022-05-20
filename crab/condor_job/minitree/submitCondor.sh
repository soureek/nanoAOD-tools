#!/bin/bash
#REFERENCE
#https://github.com/florez/CONDOR

if [ "$#" -ne 4 ]; then                                                                 #check if input parameters are less than 3
  echo "Usage: $0 <year> <sample> <lep> <region>" >&1
  echo "i.e  ./submitCondor_new.sh UL2016preVFP Mc mu 2J1T1"
  exit 1
fi
if ! [ "$1" ]; then
  echo "$1 not found" >&2
  exit 1
fi

year=$1
sample=$2
lep=$3
region=$4
crab_dir="/home/mikumar/t3store3/workarea/Nanoaod_tools/CMSSW_10_2_28/src/PhysicsTools/NanoAODTools/crab"

if ! [[ "UL2016preVFP" == "$year" || "UL2016postVFP" == "$year" || "UL2017" == "$year" || "UL2018" == "$year" ]]; then
    echo "wrong choice of year ["UL2016preVFP UL2016postVFP UL2017 UL2018"]"
    exit 1
fi

if ! [[ "Mc" == "$sample" || "Data" == "$sample" ]]; then
    echo "wrong choice of sample ["Mc Data"]"
    exit 1
fi

if ! [[ "mu" == "$lep" || "el" == "$lep" ]]; then
    echo "wrong choice of lepton ["el mu"]"
    exit 1
fi

if ! [[ "2J1T1" == "$region" || "2J1T0" == "$region" ]]; then
    echo "wrong choice of lepton ["2J1T1 2J1T0"]"
    exit 1
fi
#------------------------------------------------
#create the same datasetfile depending on year
#------------------------------------------------

if [[ "UL2016preVFP" == "$year" ]]; then
     dataset_file=$crab_dir"/minitree/dataset_UL2016preVFP_phy3.py"
     outputDir="/store/user/mikumar/RUN2_UL/MiniTree_crab/SIXTEEN_preVFP/"
     if [[ $sample == "Mc" ]]; then
	channels="Tbarchannel"
     fi

     if [[ $sample == "Data" && $lep == "mu" ]]; then
     	channels="Run2016E_preVFP_mu"
	# Run2016B_preVFP_mu Run2016D_preVFP_mu Run2016C_preVFP_mu Run2016F_preVFP_mu"
     fi
     
     if [[ $sample == "Data" && $lep == "el" ]]; then
     	channels="Run2016E_preVFP_el Run2016B_preVFP_el Run2016D_preVFP_el Run2016C_preVFP_el Run2016F_preVFP_el"
     fi

elif  [[ "UL2016postVFP" == "$year" ]]; then
     dataset_file=$crab_dir"/minitree/dataset_UL2016postVFP_phy3.py"
     outputDir="/store/user/mikumar/RUN2_UL/MiniTree_crab/SIXTEEN_postVFP/"
     if [[ $sample == "Mc" ]]; then
	channels=""
     fi

     if [[ $sample == "Data" && $lep == "mu" ]]; then
     	channels=""
     fi
     
     if [[ $sample == "Data" && $lep == "el" ]]; then
     	channels=""
     fi

elif  [[ "UL2017" == "$year" ]]; then
     dataset_file=$crab_dir"/minitree/dataset_UL2017_phy3.py"
     outputDir="/store/user/mikumar/RUN2_UL/MiniTree_crab/SEVENTEEN/"
     if [[ $sample == "Mc" ]]; then
	channels=""
     fi

     if [[ $sample == "Data" && $lep == "mu" ]]; then
     	channels=""
     fi
     
     if [[ $sample == "Data" && $lep == "el" ]]; then
     	channels=""
     fi

elif  [[ "UL2018" == "$year" ]]; then
     dataset_file=$crab_dir"/minitree/dataset_UL2018_phy3.py"
     outputDir="/store/user/mikumar/RUN2_UL/MiniTree_crab/EIGHTEEN/"
     if [[ $sample == "Mc" ]]; then
	channels=""
     fi

     if [[ $sample == "Data" && $lep == "mu" ]]; then
     	channels=""
     fi
     
     if [[ $sample == "Data" && $lep == "el" ]]; then
     	channels=""
     fi

fi

if ! [ -e "$dataset_file" ]; then
  echo "$dataset_file not found" >&2
  exit 1
fi



#------------------------------------------------
#create a directory where all the outputs will be
#stored, for different merged ntuple input files
#------------------------------------------------
file=$dataset_file
localdir=$(basename $dataset_file)  #get the file name from the dataset_file path 
#baseDir=$crab_dir"/condor_job/$(cut -d'.' -f1 <<<"$localdir")_$(date +"%d-%m-%Y")"
baseDir=$(pwd)"/$(cut -d'.' -f1 <<<"$localdir")_$(date +"%d-%m-%Y")"
echo $localdir
echo $baseDir 
#baseDir="/home/mikumar/tryout2/out_log_$(cut -d'_' -f2 <<<"$year")_$(date +"%d-%m-%Y")"
mkdir -p $baseDir


#-----------------
#create tar file
#-----------------
tarFile=$baseDir/minitree.tar.gz
rm -rf $tarFile
PhysicsTools=${crab_dir}/../../../PhysicsTools

tar --exclude='.git' --exclude=${PhysicsTools}'/NanoAODTools/crab/condor_job'  --exclude=${PhysicsTools}'/NanoAODTools/crab/tree' --exclude=${PhysicsTools}'/NanoAODTools/crab/Gen_Study' --exclude=${PhysicsTools}'/NanoAODTools/crab/Gen_Study_Sebastien' --exclude=${PhysicsTools}'/NanoAODTools/crab/efficiency' --exclude=${PhysicsTools}'/NanoAODTools/crab/lumi_n_pileup' --exclude=${PhysicsTools}'/NanoAODTools/crab/cutflow' --exclude=${PhysicsTools}'/NanoAODTools/crab/puWeight' --exclude=${PhysicsTools}'/NanoAODTools/crab/Effective_Number' -zcvf $tarFile ${PhysicsTools}
#echo $channels

for channel in $channels; do
    #echo $channel
    #------------------------------------------------
    #Run python script to create input txt file using the dataset name
    #------------------------------------------------
    mkdir "$baseDir""/""$channel"
    outcond="$baseDir""/""$channel"
    #------------------------------------------------
    #copy inportant script to the condor direcrtory
    #------------------------------------------------
    cp condorSetup.sub $outcond
    cp runAtCondor.sh $outcond
    cp $file $outcond
    cp prepare_input_filelist.py $outcond
    cp $crab_dir/minitree/crab_script_Minitree.py $outcond
    cp $crab_dir/minitree/MinitreeModule.py $outcond
    mv $tarFile $outcond
    cd $outcond

    python prepare_input_filelist.py -y "$year" -s "$sample" -l "$lep" -r "$region" -c "$channel"

    count=0
    input_files="All_input_files_"$channel".txt"
    input_file_list_10="inputFiles=["
    outputDir=${outputDir}${sample}"/"${channel}"/"${region}"_"${lep}"/"
    file_tail=`tail -n 1 $input_files`

    cat $input_files | while read ntupleT2Path
    do
  	#----------------------------------------------
  	# increase the counter to count the files
  	#----------------------------------------------
  	((count++))
  	#if [[ $count%10==0 || $ntupleT2Path == $file_tail ]]; then
  	if [[ $count%10 -eq 0 || $ntupleT2Path == $file_tail ]]; then

	     mkdir -p $count
	     #------------------------------------------------
    	     #copy important script to the final condor direcrtory
    	     #------------------------------------------------
	     cp condorSetup.sub $count
	     cp runAtCondor.sh $count
	     cp MinitreeModule.py $count
	     cp crab_script_Minitree.py	$count 
	     cd $count

    	     input_file_list_10=$input_file_list_10"'root\://se01.indiacms.res.in/"$ntupleT2Path"' ] " #adding file in the inputfile list and close list for 10 files
	     #------------------------------------------------
             #Inshirt input files to the crab script
             #------------------------------------------------	
    	     #echo $input_file_list_10
	     echo $count
	     sed -i 's:INPUT:'"$input_file_list_10"':g' crab_script_Minitree.py 
	     sed -i "s:INPUT:root\://se01.indiacms.res.in/${outputDir}tree_$count.root:g" condorSetup.sub
	     condor_submit condorSetup.sub
	     cd ../		    	
             input_file_list_10="inputFiles=["
  	else
    	     input_file_list_10=$input_file_list_10"'root\://se01.indiacms.res.in/"$ntupleT2Path"' , "  #adding file in the inputfile list
  	fi
  
  #condor_submit condorSetup.sub
    done
done