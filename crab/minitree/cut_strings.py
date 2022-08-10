#iso_mu

cut = "Entry$<500 && (HLT_IsoMu24==1 || HLT_IsoTkMu24 ==1) && (Sum$(Muon_pt>26 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.06 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==1) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && (TMath::Sqrt((Muon_eta[0]-Jet_eta)*(Muon_eta[0]-Jet_eta)+(TVector2::Phi_mpi_pi(Muon_phi[0]-Jet_phi)*TVector2::Phi_mpi_pi(Muon_phi[0]-Jet_phi)))>0.4))==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==1)"

cut_2J0T1_mu_2016 = "(HLT_IsoMu24==1 || HLT_IsoTkMu24 ==1) && (Sum$(Muon_pt>26 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.06 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==1) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_Isomu>0.4)==2) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_Isomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==0)"

cut_2J1T1_mu_2016 = "(HLT_IsoMu24==1 || HLT_IsoTkMu24 ==1) && (Sum$(Muon_pt>26 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.06 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==1) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_Isomu>0.4)==2) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_Isomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==1)"

cut_3J1T1_mu_2016 = "(HLT_IsoMu24==1 || HLT_IsoTkMu24 ==1) && (Sum$(Muon_pt>26 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.06 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==1) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 &&  Jet_dR_Ljet_Isomu>0.4)==3) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_Isomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==1)"

cut_3J2T1_mu_2016 = "(HLT_IsoMu24==1 || HLT_IsoTkMu24 ==1) && (Sum$(Muon_pt>26 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.06 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==1) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 &&  Jet_dR_Ljet_Isomu>0.4)==3) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_Isomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==2)"

#antiiso_mu

cut ="(HLT_IsoMu24==1 || HLT_IsoTkMu24 ==1) && (Sum$(Muon_pt>26 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all>0.2 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && (TMath::Sqrt((Muon_eta[0]-Jet_eta)*(Muon_eta[0]-Jet_eta)+(TVector2::Phi_mpi_pi(Muon_phi[0]-Jet_phi)*TVector2::Phi_mpi_pi(Muon_phi[0]-Jet_phi)))>0.4))==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==1)"

cut_2J1T0_mu_2016 = "(HLT_IsoMu24==1 || HLT_IsoTkMu24 ==1) && (Sum$(Muon_pt>26 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all>0.2 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsomu>0.4)==2) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_AntiIsomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==1)"

cut_2J0T0_mu_2016 = "(HLT_IsoMu24==1 || HLT_IsoTkMu24 ==1) && (Sum$(Muon_pt>26 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all>0.2 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsomu>0.4)==2) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_AntiIsomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==0)"

cut_3J1T0_mu_2016 = "(HLT_IsoMu24==1 || HLT_IsoTkMu24 ==1) && (Sum$(Muon_pt>26 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all>0.2 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsomu>0.4)==3) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_AntiIsomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==1)"

cut_3J2T0_mu_2016 = "(HLT_IsoMu24==1 || HLT_IsoTkMu24 ==1) && (Sum$(Muon_pt>26 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all>0.2 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsomu>0.4)==3) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_AntiIsomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==2)"




#iso_el

cut = "Entry$<500 && HLT_Ele32_eta2p1_WPTight_Gsf==1 && (Sum$(Electron_pt>35 && abs(Electron_eta)<2.1 && Electron_cutBased==4 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && (TMath::Sqrt((Electron_eta[0]-Jet_eta)*(Electron_eta[0]-Jet_eta)+(TVector2::Phi_mpi_pi(Electron_phi[0]-Jet_phi)*TVector2::Phi_mpi_pi(Electron_phi[0]-Jet_phi)))>0.4))==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==1)"

cut_2J1T1_el_2016 = "HLT_Ele32_eta2p1_WPTight_Gsf==1 && (Sum$(Electron_pt>35 && abs(Electron_eta)<2.1 && Electron_cutBased==4 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_Isoel>0.4)==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_Isoel>0.4 && Jet_btagDeepFlavB>0.6502)==1)"

cut_2J0T1_el_2016 = "HLT_Ele32_eta2p1_WPTight_Gsf==1 && (Sum$(Electron_pt>35 && abs(Electron_eta)<2.1 && Electron_cutBased==4 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_Isoel>0.4)==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_Isoel>0.4 && Jet_btagDeepFlavB>0.6502)==0)"

cut_3J1T1_el_2016 = "HLT_Ele32_eta2p1_WPTight_Gsf==1 && (Sum$(Electron_pt>35 && abs(Electron_eta)<2.1 && Electron_cutBased==4 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_Isoel>0.4)==3) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_Isoel>0.4 && Jet_btagDeepFlavB>0.6502)==1)"

cut_3J2T1_el_2016 = "HLT_Ele32_eta2p1_WPTight_Gsf==1 && (Sum$(Electron_pt>35 && abs(Electron_eta)<2.1 && Electron_cutBased==4 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_Isoel>0.4)==3) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_Isoel>0.4 && Jet_btagDeepFlavB>0.6502)==2)"

#antiiso_el

cut = "HLT_Ele32_eta2p1_WPTight_Gsf==1 && (Sum$(Electron_pt>35 && abs(Electron_eta)<2.1 && Electron_cutBased!=4 && Electron_cutBased>=1 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1  && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && (TMath::Sqrt((Electron_eta[0]-Jet_eta)*(Electron_eta[0]-Jet_eta)+(TVector2::Phi_mpi_pi(Electron_phi[0]-Jet_phi)*TVector2::Phi_mpi_pi(Electron_phi[0]-Jet_phi)))>0.4))==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==1)"

cut_2J1T0_el_2016 = "HLT_Ele32_eta2p1_WPTight_Gsf==1 && (Sum$(Electron_pt>35 && abs(Electron_eta)<2.1 && Electron_cutBased!=4 && Electron_cutBased>=1 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsoel>0.4)==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_AntiIsoel>0.4 && Jet_btagDeepFlavB>0.6502)==1)"

cut_2J0T0_el_2016 = "HLT_Ele32_eta2p1_WPTight_Gsf==1 && (Sum$(Electron_pt>35 && abs(Electron_eta)<2.1 && Electron_cutBased!=4 && Electron_cutBased>=1 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsoel>0.4)==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_AntiIsoel>0.4 && Jet_btagDeepFlavB>0.6502)==0)"

cut_3J1T0_el_2016 = "HLT_Ele32_eta2p1_WPTight_Gsf==1 && (Sum$(Electron_pt>35 && abs(Electron_eta)<2.1 && Electron_cutBased!=4 && Electron_cutBased>=1 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsoel>0.4)==3) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_AntiIsoel>0.4 && Jet_btagDeepFlavB>0.6502)==1)"

cut_3J2T0_el_2016 = "HLT_Ele32_eta2p1_WPTight_Gsf==1 && (Sum$(Electron_pt>35 && abs(Electron_eta)<2.1 && Electron_cutBased!=4 && Electron_cutBased>=1 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsoel>0.4)==3) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_AntiIsoel>0.4 && Jet_btagDeepFlavB>0.6502)==2)"



################################################################### 2J1L0T ########################################################################
#2J1T_iso_mu

cut_2J1L0T1_mu_2016 = "(HLT_IsoMu24==1 || HLT_IsoTkMu24 ==1) && (Sum$(Muon_pt>26 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.06 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==1) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 &&  Jet_dR_Ljet_Isomu>0.4)==2) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_Isomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.0480)==1) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_Isomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==0)"

#2J1T_antiiso_mu

cut_2J1L0T0_mu_2016 = "(HLT_IsoMu24==1 || HLT_IsoTkMu24 ==1) && (Sum$(Muon_pt>26 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all>0.2 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsomu>0.4)==2) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_AntiIsomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.0480)==1)  && (Sum$(Jet_pt>40 && Jet_dR_Ljet_AntiIsomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.6502)==0)"

#2J1T_iso_el

cut_2J1L0T1_el_2016 = "HLT_Ele32_eta2p1_WPTight_Gsf==1 && (Sum$(Electron_pt>35 && abs(Electron_eta)<2.1 && Electron_cutBased==4 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_Isoel>0.4)==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_Isoel>0.4 && Jet_btagDeepFlavB>0.0480)==1)  && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_Isoel>0.4 && Jet_btagDeepFlavB>0.6502)==0)"


#2J1T_antiiso_el

cut_2J1L0T0_el_2016 = "HLT_Ele32_eta2p1_WPTight_Gsf==1 && (Sum$(Electron_pt>35 && abs(Electron_eta)<2.1 && Electron_cutBased!=4 && Electron_cutBased>=1 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsoel>0.4)==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_AntiIsoel>0.4 && Jet_btagDeepFlavB>0.0480)==1) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_AntiIsoel>0.4 && Jet_btagDeepFlavB>0.6502)==0)"


##################-----2017----##############################------2017----####################################------2017----####################

#iso_mu

cut_2J1T1_mu_2017 = "(HLT_IsoMu27==1) && (Sum$(Muon_pt>30 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.06 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==1) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 &&  Jet_dR_Ljet_Isomu>0.4)==2) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_Isomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.7476)==1)"

cut_2J0T1_mu_2017 = "(HLT_IsoMu27==1) && (Sum$(Muon_pt>30 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.06 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==1) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 &&  Jet_dR_Ljet_Isomu>0.4)==2) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_Isomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.7476)==0)"

cut_3J1T1_mu_2017 = "(HLT_IsoMu27==1) && (Sum$(Muon_pt>30 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.06 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==1) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 &&  Jet_dR_Ljet_Isomu>0.4)==3) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_Isomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.7476)==1)"

cut_3J2T1_mu_2017 = "(HLT_IsoMu27==1) && (Sum$(Muon_pt>30 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.06 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==1) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 &&  Jet_dR_Ljet_Isomu>0.4)==3) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_Isomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.7476)==2)"

#2J1T_antiiso_mu

cut_2J1T0_mu_2017 = "(HLT_IsoMu27==1 ) && (Sum$(Muon_pt>30 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all>0.2 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsomu>0.4)==2) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_AntiIsomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.7476)==1)"

cut_2J0T0_mu_2017 = "(HLT_IsoMu27==1 ) && (Sum$(Muon_pt>30 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all>0.2 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsomu>0.4)==2) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_AntiIsomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.7476)==0)"

cut_3J1T0_mu_2017 = "(HLT_IsoMu27==1 ) && (Sum$(Muon_pt>30 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all>0.2 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsomu>0.4)==3) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_AntiIsomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.7476)==1)"

cut_3J2T0_mu_2017 = "(HLT_IsoMu27==1 ) && (Sum$(Muon_pt>30 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all>0.2 && Muon_tightId==1)==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Electron_cutBased ==1 && Electron_pt>15 && abs(Electron_eta)<2.5 && (abs(Electron_eta) < 1.4442 || abs(Electron_eta) > 1.566))==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsomu>0.4)==3) && (Sum$(Jet_pt>40 && Jet_dR_Ljet_AntiIsomu>0.4 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_btagDeepFlavB>0.7476)==2)"

#iso_el

cut_2J1T1_el_2017 = "(HLT_Ele35_WPTight_Gsf==1 || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned==1) && (Sum$(Electron_pt>37 && abs(Electron_eta)<2.1 && Electron_cutBased==4 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_Isoel>0.4)==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_Isoel>0.4 && Jet_btagDeepFlavB>0.7476)==1)"

cut_2J0T1_el_2017 = "(HLT_Ele35_WPTight_Gsf==1 || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned==1) && (Sum$(Electron_pt>37 && abs(Electron_eta)<2.1 && Electron_cutBased==4 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_Isoel>0.4)==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_Isoel>0.4 && Jet_btagDeepFlavB>0.7476)==0)"

cut_3J1T1_el_2017 = "(HLT_Ele35_WPTight_Gsf==1 || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned==1) && (Sum$(Electron_pt>37 && abs(Electron_eta)<2.1 && Electron_cutBased==4 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_Isoel>0.4)==3) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_Isoel>0.4 && Jet_btagDeepFlavB>0.7476)==1)"

cut_3J2T1_el_2017 = "(HLT_Ele35_WPTight_Gsf==1 || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned==1) && (Sum$(Electron_pt>37 && abs(Electron_eta)<2.1 && Electron_cutBased==4 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_Isoel>0.4)==3) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_Isoel>0.4 && Jet_btagDeepFlavB>0.7476)==2)"

#antiiso_el

cut_2J1T0_el_2017 = "(HLT_Ele35_WPTight_Gsf==1 || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned==1) && (Sum$(Electron_pt>37 && abs(Electron_eta)<2.1 && Electron_cutBased!=4 && Electron_cutBased>=1 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsoel>0.4)==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_AntiIsoel>0.4 && Jet_btagDeepFlavB>0.7476)==1)"

cut_2J0T0_el_2017 = "(HLT_Ele35_WPTight_Gsf==1 || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned==1) && (Sum$(Electron_pt>37 && abs(Electron_eta)<2.1 && Electron_cutBased!=4 && Electron_cutBased>=1 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsoel>0.4)==2) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_AntiIsoel>0.4 && Jet_btagDeepFlavB>0.7476)==0)"

cut_3J1T0_el_2017 = "(HLT_Ele35_WPTight_Gsf==1 || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned==1) && (Sum$(Electron_pt>37 && abs(Electron_eta)<2.1 && Electron_cutBased!=4 && Electron_cutBased>=1 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsoel>0.4)==3) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_AntiIsoel>0.4 && Jet_btagDeepFlavB>0.7476)==1)"

cut_3J2T0_el_2017 = "(HLT_Ele35_WPTight_Gsf==1 || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned==1) && (Sum$(Electron_pt>37 && abs(Electron_eta)<2.1 && Electron_cutBased!=4 && Electron_cutBased>=1 && (abs(Electron_EtaSC)<1.4442 || abs(Electron_EtaSC)>1.5660) && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Electron_cutBased>=1 && Electron_pt>15 && abs(Electron_eta)<2.5 && ((abs(Electron_EtaSC)<=1.479 && abs(Electron_dz)< 0.10 && abs(Electron_dxy)< 0.05) || (abs(Electron_EtaSC)> 1.479 && abs(Electron_dz)< 0.20 && abs(Electron_dxy)< 0.10)))==1) && (Sum$(Muon_looseId==1 && Muon_pt>10 && abs(Muon_eta)<2.4 && Muon_pfRelIso04_all<0.2)==0) && (Sum$(Jet_pt>40 && abs(Jet_eta)<4.7 && Jet_jetId!=0 && Jet_puId>0 && Jet_dR_Ljet_AntiIsoel>0.4)==3) && (Sum$(Jet_pt>40 && Jet_jetId!=0 && Jet_puId>0 && abs(Jet_eta)<2.4 && Jet_dR_Ljet_AntiIsoel>0.4 && Jet_btagDeepFlavB>0.7476)==2)"
