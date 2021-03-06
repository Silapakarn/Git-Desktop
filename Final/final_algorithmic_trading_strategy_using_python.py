# -*- coding: utf-8 -*-
"""Final_Algorithmic Trading Strategy Using Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vtNGFZZoxy9vMXh0nM7Y-De9V0OZrrjz
"""

#import the libraries
import pandas as pd
import numpy as np
from datetime import  datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Load Data
from google.colab  import files
uploaded = files.upload()

#Store the Data
AAPL = pd.read_csv('AAPL.csv')
#Show Data
AAPL

#Visualize the data
plt.figure(figsize=(12.5,4.5))
plt.plot(AAPL['Adj Close'], label  = ' AAPL ')
plt.title('Apple Adj Close Price History')
plt.xlabel('Oct. 02, 2006 - Dec. 30, 2020')
plt.ylabel('Adj Close Price USD($)')
plt.legend(loc='upper left')
plt.show

#Create simple moving Average with a 30 day window
SMA30 = pd.DataFrame()
SMA30['Adj Close'] = AAPL['Adj Close'].rolling(window= 30).mean()
SMA30

#Create simple moving Average with a 100 day 
SMA100 = pd.DataFrame()
SMA100['Adj Close'] = AAPL['Adj Close'].rolling(window= 100).mean()
SMA100

#Visualize the data
plt.figure(figsize=(12.5,4.5))
plt.plot(AAPL['Adj Close'], label  = ' AAPL ')
plt.plot(SMA30['Adj Close'], label = 'SMA30')
plt.plot(SMA100['Adj Close'], label = 'SMA100')
plt.title('Apple Adj Close Price History')
plt.xlabel('Oct. 02, 2006 - Dec. 30, 2020')
plt.ylabel('Adj Close Price USD($)')
plt.legend(loc='upper left')
plt.show

#Create a new data frame to store all the  data
data = pd.DataFrame()
data['AAPL'] = AAPL['Adj Close']
data['SMA30'] = SMA30['Adj Close']
data['SMA100'] = SMA100['Adj Close']
data

#Create a function tp signal buy and sell the Asset/Stock
def  buy_sell(data):
  sigPriceBuy = []
  sigPriceSell = []
  flag = -1

  for i in range(len(data)):
    if data['SMA30'][i] > data['SMA100'][i]:
      if flag != 1:
        sigPriceBuy.append(data['AAPL'][i])
        sigPriceSell.append(np.nan)
        flag = 1
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    elif data['SMA30'][i] < data['SMA100'][i]:
      if flag != 0:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(data['AAPL'][i])
        flag = 0
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    else :
      sigPriceBuy.append(np.nan)
      sigPriceSell.append(np.nan)

  return (sigPriceBuy,  sigPriceSell)

#Store the buy and sell data into a variable
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

#Show the data 
data

#Visualize the data and the strategy  to buy and sell the stock
plt.figure(figsize=(12.6,4.6))
plt.plot(data['AAPL'], label  = ' AAPL ', alpha = 0.35)
plt.plot(data['SMA30'], label = 'SMA30', alpha = 0.35)
plt.plot(data['SMA100'], label = 'SMA100', alpha = 0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', marker= '^', color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'Sell', marker= 'v', color = 'red')
plt.title('Apple Adj Close Price History Buy and Sell Signals')
plt.xlabel('Oct. 02, 2006 - Dec. 30, 2020')
plt.ylabel('Adj Close Price USD($)')
plt.legend(loc='upper left')
plt.show