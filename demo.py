# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 18:32:19 2018

@author: Saaji
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")
import math
d = 10
N = 10000
num_of_sel = [0] * d
ads_selected = []
sum_of_rewards = [0] * d
total_reward = 0
for n in range(0,N):
    ad = 0
    max_ucb = 0
    for i in range(0,d):
        if num_of_sel[i] > 0:
            average_reward = sum_of_rewards[i]/num_of_sel[i]
            delta_i = math.sqrt(3/2 * math.log(n+1)/num_of_sel[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_ucb:
            max_ucb = upper_bound
            ad = i
    ads_selected.append(ad)        
    num_of_sel[ad] = num_of_sel[ad] + 1
    reward = dataset.values[n,ad]
    sum_of_rewards[ad] = sum_of_rewards[ad] + reward
    total_reward = total_reward + reward
    
        
            
        


