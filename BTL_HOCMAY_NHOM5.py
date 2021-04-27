
from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
import tkinter as tk
from tkinter import *
from tkinter import messagebox

master=tk.Tk()
master.title("Dự đoán giá Biệt thự")
tk.Label(master, text="Nhập các thông tin dưới đây", fg='blue').grid (column=0, row=0)

tk.Label (master, text="nhap so tang:", fg='blue').grid (column=0, row=1)
s1 = Entry(master,width=70)
s1.grid(column=1, row=1)
tk.Label (master, text="Nhap dien tich :", fg='blue').grid (column=0, row=2)
s2 = Entry(master,width=70)
s2.grid(column=1, row=2)
tk.Label (master, text="Nhap so mat tien:", fg='blue').grid (column=0, row=3)
s3 = Entry(master,width=70)
s3.grid(column=1, row=3)

##### truyền dữ liệu ######
b_x='da.txt'
b_y='dat.txt'
data=pd.read_csv(b_x,sep='\t')
label=pd.read_csv(b_y,sep='\t')
# print(type(data))
X = data.values
# print(X)
# print(label)
X = data.values
Y=label.values
# print(X.shape)
# print(Y.shape)

one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, Y)
w = np.dot(np.linalg.pinv(A), b)
#print ('w=',w)

w_0 = w[0][0]
w_1 = w[1][0]
w_2 = w[2][0]
w_3 = w[3][0]



def predict():
	b1=float(s1.get())
	b2=float(s2.get())
	
	y_0 = w_0 + w_1*b1+w_2*b2
	messagebox.showinfo( "Giá phần mềm :",y_0)
tk.Button(master,  text='Enter', command=predict).grid(row=5, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=5)

#master.mainloop()
#x1 = float(input("Nhập số Tầng: "))
#x2 = float(input("nhập diện tích: "))
#x3 = float(input("Nhập số mặt tiền: "))

#giadudoan =  w_3*x3 + w_2*x2 + w_1*x1 + w_0
#print(  u'giabietthududoan: %.2f' %(giadudoan))
