# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 18:11:23 2023

@author: gesit
"""



import pickle
import numpy as np


class image:
    def __init__(self):
        pass
    def mnist(self):
        with open(r'D:\SE\Python\Neural Network\data\mnist.pkl', 'rb') as f:
            train, val, test = pickle.load(f, encoding='latin1')
        
        trainx,trainy=train
        valx,valy=val
        testx,testy=test
        
        trainx1=trainx.reshape([trainx.shape[0],28,28])
        trainy1=np.zeros([trainy.shape[0],10])
        trainy1[np.arange(trainy.shape[0]),trainy]=1
        
        valx1=valx.reshape([valx.shape[0],28,28])
        valy1=np.zeros([valy.shape[0],10])
        valy1[np.arange(valy.shape[0]),valy]=1
        
        testx1=testx.reshape([testx.shape[0],28,28])
        testy1=np.zeros([testy.shape[0],10])
        testy1[np.arange(testy.shape[0]),testy]=1
        
        
        # trainy1, valy1, testy1=trainy, valy, testy
        
        return [[trainx1, trainy1], [valx1, valy1],[testx1,testy1]]
        # print (trainx.shape, ", ", valx.shape, ", ", testx.shape)
    



















