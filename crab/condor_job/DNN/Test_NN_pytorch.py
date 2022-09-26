#source /cvmfs/cms.cern.ch/cmsset_default.sh
import torch
import pandas as pd
import numpy as np
import ROOT as rt
import root_numpy
from IPython.display import display
from torch.utils.data import TensorDataset, DataLoader
from torch import nn
from torch.utils.tensorboard import SummaryWriter
from datetime import datetime
import os


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        #self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(18, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 6),
            #nn.Softmax(dim=1),
        )



    def forward(self, x):
        #x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


VARS = ['MuonEta', 'MuonPt', 'MuonPhi', 'MuonE',
        'lJetEta', 'lJetPt', 'lJetPhi', 'lJetMass',
        'bJetEta', 'bJetPt', 'bJetPhi', 'bJetMass',
        'Px_nu', 'Py_nu', 'Pz_nu',
        'FW1', 'bJetdeepJet', 'lJetdeepJet',
        ]


train_ch = ['WS_Top_signal', 'Top_signal', 'Top_bkg', 'WS_Top_bkg', 'EWK_BKG', 'QCD_BKG']
types = ['train', 'test', 'valid']
files = []
for channel in train_ch:
    for typ in types:
        files.append('2017_' + channel + '_' + typ + '.root')

print(files)
#files = ['preVFP2016_Top_signal_train.root', 'preVFP2016_EWK_BKG_train.root', 'preVFP2016_Top_bkg_train.root', 'preVFP2016_Top_signal_test.root', 'preVFP2016_EWK_BKG_test.root', 'preVFP2016_Top_bkg_test.root']
m = nn.LogSoftmax(dim=1)
for fil in files:
	print(fil)
	df_test = rt.RDataFrame("Events",fil).AsNumpy()
		
	#display(df_tr_top_signal_new)

	x_te = np.vstack([df_test[var] for var in VARS]).T
	print("shape of x for training" ,x_te.shape)

	y_te = np.vstack([0]*(x_te.shape[0]))
	y_te = np.vstack([y_te]).astype(int)
	print("shape of y for training", y_te.shape)

	tensor_x_te = torch.Tensor(x_te) # transform to torch tensor
	tensor_y_te = torch.Tensor(y_te)

	device = "cuda:1" if torch.cuda.is_available() else "cpu"
	print(f"Using {device} device")

	if torch.cuda.is_available():
		tensor_x_te = tensor_x_te.to(device)
		tensor_y_te = tensor_y_te.to(device)


	batch = 200
	test_dataset = TensorDataset(tensor_x_te,tensor_y_te) # create your datset
	testing_loader = DataLoader(test_dataset, batch_size = batch, shuffle = False) # create your dataloader

	model = NeuralNetwork().to(device)
	model.load_state_dict(torch.load('weights_l08/model_20220914_173358_41'))
	y_arr = np.zeros((x_te.shape[0], 6))

	for i, tdata in enumerate(testing_loader):
		#print(i)
		tinputs, tlabels = tdata
		toutput = model(tinputs)
		toutput1 = m(toutput)
		toutputs = torch.Tensor.cpu(toutput1)
		#print(np.shape(toutputs))
		if i < x_te.shape[0]//batch:
			y_arr[batch*i:batch*(i+1), :] = np.exp(toutputs.detach().numpy())
		else:
			y_arr[batch*i:, :] = np.exp(toutputs.detach().numpy())
	#print(y_arr[:10,:])
	#print(y_arr[-10:,:])
	#print(np.shape(y_arr))
	y_arr = y_arr.ravel().view(dtype = np.dtype([('c1', np.double), ('c2', np.double), ('c3', np.double), ('c4', np.double), ('c5', np.double), ('c6', np.double)]))
	fname, ext = os.path.splitext(fil)
	root_numpy.array2root(y_arr, 'weights_l08/' + fname + '_apply.root', mode='recreate')
