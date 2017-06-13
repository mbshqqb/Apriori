# -*- coding:utf-8 -*-
import numpy as np
from support_confidence import *
train=[[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
mins=0.5
minc=0.7

def apriori(train,mins,minc):
    items=[1,2,3,4,5]
    n_item=len(items)

    freq=[{}for i in range(n_item)]#1-5项集
    #产生频繁项集
    for i in items:#1项集
        freq[0][frozenset([i])]=support(train, [i])
    for k in range(1,n_item):#k+1项集
        keyset=freq[k-1].keys()
        can_freq=set([i_k|j_k for i_k in keyset for j_k in keyset if list(i_k)[len(i_k)-1]<list(j_k)[len(j_k)-1] and list(i_k)[:len(i_k)-1]==list(j_k)[:len(j_k)-1]])
        for k_k in can_freq:
            s=support(train, list(k_k))
            if s>=mins:
                freq[k][k_k]=s
    print(freq)

    rule=[{}for i in range(n_item)]#1-5项集
    #产生规则
    for k in range(1,n_item):#k+1项集,1项集没有规则
        for key,value in freq[k].items():
            key=list(key)
            #产生规则,相当于前面的产生频繁项集
            rule_y_set =[set() for i in range(len(key))]#每一个set中存储后件为h的后件
            for i in range(len(key)):#存储后件为1的后件
                x=set(key)-set([key[i]])
                y=list([key[i]])
                if(confidence(value,train,x)>=minc):
                    rule_y_set[0].add(frozenset(y))#倒序的
                    rule[0][frozenset(x)]=y
            #产生候选规则,
            for h in range(1,k):#为k+1项集，但需要循环k次，生成 k->1  h->k-h 1->k,h表示当前规则的后件有h个
                pre_y_set=rule_y_set[h-1]
                can_rule_y= set([i_k | j_k for i_k in pre_y_set for j_k in pre_y_set if list(i_k)[len(i_k) - 1] < list(j_k)[len(j_k) - 1] and list(i_k)[:len(i_k) - 1] == list(j_k)[:len(j_k) - 1]])
                #将规则加入
                for cr_y in can_rule_y:
                    cr_x=set(key) - set(cr_y)
                    if (confidence(value, train,cr_x ) >= minc):
                        rule_y_set[h].add(cr_y)  # 倒序的
                        rule[k][frozenset(cr_x)]=list(cr_y)
    print(rule)
apriori(train,mins,minc)