# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd

train=[[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
def support(train, xy):
    return sum([set(t).issuperset(xy)for t in train])/len(train)
print(support(train, [2, 3]))

def confidence(s,train,x):
    return s*len(train)/sum([set(t).issuperset(x)for t in train])
#print(confidence(0.5,train,[2,3].remove(3)))#2->3
print(confidence(0.5,train,set([2,3])-set([3])))#2->3