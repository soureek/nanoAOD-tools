import fileinput, string, sys, os, time, datetime
import argparse as arg

parser = arg.ArgumentParser(description='inputs discription')
parser.add_argument('-y', '--year', dest='years', type=str, nargs=1, help="Year [ UL2016preVFP , UL2016postVFP , UL2017 , UL2018 ]")
parser.add_argument('-l', '--lep', dest='leptons', type=str, nargs=1, help="lepton [ el , mu ]")

args = parser.parse_args()

if (args.years == None or args.leptons == None):
        print "USAGE: %s [-h] [-y <Data year> -l <lepton>]"%(sys.argv [0])
        sys.exit (1)

if args.years[0] not in ['UL2016preVFP', 'UL2016postVFP','UL2017','UL2018']:
    print('Error: Incorrect choice of year, use -h for help')
    exit()

if args.leptons[0] not in ['el','mu']:
    print('Error: Incorrect choice of lepton, use -h for help')
    exit()

print "year = ",args.years[0]
print "lepton = ",args.leptons[0]
year   = args.years[0]
lep    = args.leptons[0]
date   = datetime.datetime.now()

if(year == 'UL2016preVFP'):
    from dataset_UL2016preVFP_phy3 import *
    outputDir = "/store/user/mikumar/RUN2_UL/MiniTree_crab/SIXTEEN/MC/check/"
    Datasets = Datasets_MC_UL2016APV
if(year == 'UL2016postVFP'):
    from dataset_UL2016postVFP_phy3 import *
    outputDir = "/store/user/mikumar/RUN2_UL/MiniTree_crab/SIXTEEN/MC/check/"
    Datasets = Datasets_MC_UL2016

if(year == 'UL2017'):
    from dataset_UL2017_phy3 import *
    outputDir = "/store/user/mikumar/RUN2_UL/MiniTree_crab/SEVENTEEN/MC/check/"
    Datasets = Datasets_MC_UL2017

RequestNames = Datasets.keys()
print RequestNames
print "len(Datasets) = ",len(Datasets)
cfgfile = "crab_cfg_Minitree.py"
crab_scriptfile = "crab_script_Minitree.py"
#bweight_cal = "Mc_prob_cal_forBweght.py"
MinitreeModule = "MinitreeModule.py"

def replacemachine(fileName, sourceText, replaceText):
    print "editing ",fileName,
    ##################################################################
    for line in fileinput.input(fileName, inplace=True):
        if line.strip().startswith(sourceText):
        	line = replaceText
    	sys.stdout.write(line)
    print "All went well, the modifications are done"
    ##################################################################

for i in range(0,len(RequestNames)):
    RequestName = RequestNames[i]
    Dataset = Datasets[RequestNames[i]][0]	
    NumberOfEvents = Datasets[RequestNames[i]][1] 
    Xsection = Datasets[RequestNames[i]][2]

    if(lep=="el" and RequestName.find("MuEnriched")!=-1 and RequestName.find("QCD")!=-1): continue
    if(lep=="mu" and RequestName.find("EMEnriched")!=-1 and RequestName.find("QCD")!=-1): continue
    region_tag = "2J1T1"
    update_RequestName = "config.General.requestName = '"+RequestName+"_Minitree_"+region_tag+"_"+lep+"_"+year+"'\n" 
    update_Dataset = "config.Data.inputDataset = '"+Dataset+"'\n"
    update_DirBase = "config.Data.outLFNDirBase = '"+outputDir+region_tag+"_"+lep+"/"+RequestName+"'\n"
    update_DatasetTag = "config.Data.outputDatasetTag = 'MiniTree_"+date.strftime("%d")+"_"+date.strftime("%b")+date.strftime("%y")+"_MC"+year+"_"+RequestName+"_"+region_tag+"_check'\n"
    update_InputFiles = "config.JobType.inputFiles = ['ElectronSF','MuonSF','scaleFactor.py','jme.py','crab_script_Minitree.py','../../scripts/haddnano.py','Mc_prob_cal_forBweght.py','foxwol_n_fourmomentumSolver.py','MinitreeModule.py','cut_strings.py','keep_and_drop_mu_Minitree.txt','keep_and_drop_el_Minitree.txt']\n"
    if(year=='UL2016preVFP' or year=='UL2016postVFP' ):cut_string = "treecut = cut_"+region_tag+"_"+lep+"_2016\n"
    elif(year=='UL2017'):cut_string = "treecut = cut_"+region_tag+"_"+lep+"_2017\n"
    modules = "\t\tmodules=[MinitreeModuleConstr"+region_tag+"_"+lep+"_mc_"+year+"(),jmeCorrections"+year+"_MC_AK4CHS()],\n"
    branchsel = '\t\toutputbranchsel="keep_and_drop_'+lep+'_Minitree.txt",\n' 
     
    update_NumberOfEvents = "\t\tNEvents = "+NumberOfEvents+"\n"
    update_Xsection = "\t\tx_sec = "+Xsection+"\n"

    print "\t"+cut_string 
    print modules
    print branchsel 
    print "\tRequestName: ",update_RequestName  
    print "\tDatasets = ",update_Dataset  
    print "\tDirBase = ",update_DirBase  
    print "\tDatasetTag = ",update_DatasetTag  
    print "\tNumber of Events = ",NumberOfEvents  
    print "\tXsection = ",Xsection	   
    print "InputFiles: ",update_InputFiles  
    #print "update_effi_file: ", update_effi_file

    replacemachine(cfgfile,'config.General.requestName =', update_RequestName)
    replacemachine(cfgfile,'config.Data.inputDataset =', update_Dataset )
    replacemachine(cfgfile,'config.Data.outLFNDirBase =', update_DirBase )
    replacemachine(cfgfile,'config.Data.outputDatasetTag =', update_DatasetTag )
    replacemachine(cfgfile,'config.JobType.inputFiles =', update_InputFiles )
    replacemachine(crab_scriptfile,'treecut =', cut_string )
    replacemachine(crab_scriptfile,'modules=', modules )
    replacemachine(crab_scriptfile,'outputbranchsel=', branchsel )
    #replacemachine(bweight_cal,'Effi_FIle = ROOT.TFile(', update_effi_file )
    replacemachine(MinitreeModule,'NEvents = ', update_NumberOfEvents )
    replacemachine(MinitreeModule,'x_sec = ',update_Xsection)


    #cmd_crab_kill = "crab purge crab_2016/crab_MiniTree_2016/2J1T1/crab_"+RequestName[i]+"_Minitree2J1T1_mu"
    #os.system(cmd_crab_kill)

    #cmd_rm_dir = "rm -rf crab_"+RequestName[i]+"_Minitree2J1T0_el"
    #os.system(cmd_rm_dir)

    cmd_crab_submit = "crab submit -c crab_cfg_Minitree.py"
    #os.system(cmd_crab_submit)  
 


    #cmd_rm_dir = "rm -rf crab_"+RequestName[i]+"_2J1T1MiniTr_mu_mc"
    #os.system(cmd_rm_dir)


    print "DONE -----",i,"---",region_tag,"---",RequestName,"---",NumberOfEvents,"-----",Xsection, "-------------------------------------------------------------------"
    #time.sleep(10)"""
    