# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 00:59:26 2018

@author: 11854
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import math
dim=2

#读取数据
filename='data_LDA.txt'
train_data = np.loadtxt(filename, delimiter=',', dtype=np.str)
train_data = np.float64(train_data)

#train_data=preprocessing.scale(train_data)
#K=kernel(np.vstack((train_data1_mean,train_data2_mean)))
data_mean=train_data
#data_mean=train_data
nun_of_data=data_mean.shape[0]
distance_maxtrix=np.zeros([nun_of_data,nun_of_data])
K=np.zeros([nun_of_data,nun_of_data])
K0=np.zeros([nun_of_data,nun_of_data])
#k是kernel矩阵
a=np.sum(np.square(data_mean),axis=1,keepdims=True)
#生成一个一行500列的向量，每一个元素是每张图片3072个像素点数据的平方和,x是测试集,y^2
b=np.sum(np.square(data_mean),axis=1)
#生成一个一行5000行的向量，每一个元素是每张图片3072个像素点数据的平方和,x是训练集x^2
c=np.multiply(-2,np.dot(data_mean,data_mean.T))
#distance_maxtrix=np.add(a,b)
#distance_maxtrix=np.add(distance_maxtrix,c)
#distance_maxtrix=np.sqrt(distance_maxtrix)



kernel_sigma=7.0001


#算距离矩阵
for i in range(nun_of_data):
    for j in range(nun_of_data):
        distance_maxtrix[i][j]=np.linalg.norm(data_mean[i]-data_mean[j])
        K0[i][j]=math.exp(-distance_maxtrix[i][j]**2/2/kernel_sigma**2)
oneN=np.ones_like(K0)/nun_of_data
#oneN=np.ones_like(K0)
K=K0-oneN.dot(K0)-K0.dot(oneN)+(oneN.dot(K0)).dot(oneN)

B=np.zeros_like(K)
B[0:201,0:201]=np.ones((201,201))/201
B[201:402,201:402]=np.ones((201,201))/201

#提取特征值，特征向量
ddd=np.linalg.inv(K0.dot(K0))
ccc=(K0.dot(B)).dot(K0)
#ccc=((np.linalg.inv(K0)).dot(B)).dot(K0)
eigenvalue,featurevector=np.linalg.eig(ddd.dot(ccc))
featurevector=featurevector.real
eigenvalue=eigenvalue.real


eigenvalue_index=np.argsort(-eigenvalue)
eigenvalue_index=eigenvalue_index[0:dim]
#按照降序排列，返回索引
#eigenvalue_sort1=eigenvalue[np.argsort(-eigenvalue)]
eigenvalue_sort=eigenvalue[eigenvalue_index[0:dim]]
featurevector_sort=featurevector[:,eigenvalue_index[0:dim]]

data_mapped=(featurevector_sort.T).dot(K0)
data_mapped=data_mapped.T
plt.scatter(data_mapped[0:201,0], data_mapped[0:201,1], s=5,c='g')
plt.scatter(data_mapped[201:402,0], data_mapped[201:402,1], s=5,c='r')
#plt.scatter(data_mapped[0:201,0], data_mapped[0:201,0], s=5,c='g')
#plt.scatter(data_mapped[201:402,0], data_mapped[201:402,0], s=5,c='r')
plt.show() 



