# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 22:06:25 2023

@author: gesit
"""

# import matplotlib.pyplot as plt
import numpy as np
# import pickle as pkl
# from tqdm import tqdm
# from PIL import Image


# import sys
# sys.path.append(r"D:\SE\Python\AI")

# from cupy.data import file_process, Images





class noise:
    def __init__(self):
        pass
        
        
    def beta_scheduler(self, total_step=1000):
        beta_1=np.linspace(0.0001, 0.02, total_step) #implementation from original paper
        x=1
        alpha_t=np.empty(0)
        for beta in beta_1:
        #     x=(np.sqrt(1-beta))*x            
            x=(1-beta)*x
            alpha_t=np.append(alpha_t,x)
        return alpha_t
    
        # plt.plot(alpha_t**0.5)
        # plt.plot(np.cos((1-beta_t)*(np.pi/2)))
        # plt.show()
        # print(alpha_t[-10:])
    def add_noise(self, original_image, step, alpha_t):
        
        original_image=(original_image/255)
        alpha=alpha_t[step]
        mean=(alpha**0.5)*original_image
        variance=((1-alpha)**0.5)
    #     variance=beta_1[step]*50
        
    #     print (((1-alpha)**0.5), (alpha**0.5))
        noise=np.random.normal(mean, variance)
    
    #     noise=np.random.normal(mean, 1)
        
    #     noise=np.minimum(noise,255)
    #     print (noise)
    
        noise=((noise/2)+0.5)*255
        noise=np.minimum(noise,255)
        noise=np.maximum(noise,0)
        
        return noise.astype(np.uint8)
    
    
        
        
        
                  
                  
                  
                
        
    












