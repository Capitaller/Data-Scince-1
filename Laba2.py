import numpy as np
import statistics as st
from numpy import loadtxt
from numpy.core.fromnumeric import mean
from numpy.lib.function_base import median
from pandas.core.base import DataError
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import math as m
import seaborn as sns
from sympy import *

def read_dataset(path):
    data = sorted((loadtxt(path, delimiter=",", unpack=False)).tolist())
    for i in range(0, len(data)):
        data[i] = int(data[i])
    return data

# Первый метод
def moment_method1(data):
    a1 = sum(data)/len(data)
    
    sy1 = m.sqrt(np.var(data))
    
    return a1 , sy1
# Второй метод
def moment_method2(data):
    a2 = st.mean(data)
    sum_temp = 0
    for i in range (len(data)):
        sum_temp+=(data[i] - a2) ** 2
    sy2 = m.sqrt(sum_temp/len(data))
    return a2 , sy2
def grafik1(data):
    a_list = list()
    mm = list()
    for i in range (1,20):
        for k in range(0,len(data),i):
            if(k<len(data)):
                a_list.append(data[k])
        mm_temp = moment_method1(a_list)        
        mm.append(mm_temp)

    median_list = list()
    for i in range(len(mm)):
        median_list.append(mm[i][0])
    
    median_list.reverse()

    plt.plot(median_list)
    mm1 = moment_method1(data)
    plt.title('Математичне сподівання')
    
    
    plt.hlines(mm1[0],0,len(median_list))
    plt.show()
def grafik2(data):
    a_list = list()
    mm = list()
    for i in range (1,20):
        for k in range(0,len(data),i):
            if(k*i<len(data)):
                a_list.append(data[k*i])
        mm_temp = moment_method1(a_list)        
        mm.append(mm_temp)

    median_list = list()
    for i in range(len(mm)):
        median_list.append(mm[i][1])
    
    median_list.reverse()

    plt.plot(median_list)
    mm1 = moment_method1(data)
    
    plt.title('Середньоквадратичне відхилення')
    plt.hlines(mm1[1],0,len(median_list))
    
    plt.show()
    
def main():
    data = read_dataset(r"C:\Users\Антон\Desktop\КПИ\2 Семестр\Аналіз даних\Лаба 1\File_data.csv")
    
    mm1 = moment_method1(data)
    mm2 = moment_method2(data)
    print("точковa оцінкa параметрів розподілу методом моментів: ", mm1[0], mm1[1])
    print("точковa оцінкa параметрів розподілу методом найбільшої подібності: ", mm2[0], mm2[1])
    grafik1(data)
    grafik2(data)


if __name__ == "__main__":
    main()
