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

def read_dataset(path):
    data = sorted((loadtxt(path, delimiter=",", unpack=False)).tolist())
    for i in range(0, len(data)):
        data[i] = int(data[i])
    return data


#Інтервальний ряд таблиця
def Interval_print(table_list, data):
    x = PrettyTable()
    x.field_names = ["Интервалы", "Кількість елементів", "Частота"]
    for i in range(len(table_list)):
        temp = table_list[i][1] / len(data)
        x.add_row([f"{table_list[i][0][0]} - {table_list[i][0][1]}", table_list[i][1], (round(temp, 3))])
    print(x)
#Інтервальний ряд
def internal_var(data):
    min = np.min(data)
    max = np.max(data)
    R = max-min
    interval = m.ceil(1+float(3.322*(float(m.log10(len(data))))))
    #interval = 25
    class_length = round(R/interval)
    table_list = list()

    first_elem = min
    second_elem = first_elem + class_length

    for i in range(interval):
        temp = [first_elem, second_elem]
        first_elem = second_elem
        second_elem = second_elem + class_length
        if(i == interval-2):
            second_elem = max

        list_temp = [temp, 0]
        

        table_list.append(list_temp)

    for x in range(len(data)):
        for i in range(len(table_list)):
            if (data[x] >= table_list[i][0][0]) and (data[x] < table_list[i][0][1]):
                table_list[i][1] = table_list[i][1] + 1
                break

    borders = list()
    borders.append(table_list[0][0][0])
    for i in range(0, len(table_list)):
        borders.append(table_list[i][0][1])

    plt.xticks(borders, rotation=55)
    plt.hist(data, bins=borders)
    plt.show()

    return table_list

def character(data):
    #print(data)
    print("Мода: ", st.mode(data))
    print("Медиана: ", np.median(data))
    print("Середне: ", np.mean(data) )
    print("Розмах: ", np.max(data)-np.min(data))
    print("1 квартиль: ", np.percentile(data,25))
    print("2 квартиль: ", np.percentile(data,50))
    print("3 квартиль: ", np.percentile(data,75))
    print("Квартильний розмах: ", np.percentile(data,75)- np.percentile(data,25))
    print("Дисперсия:", np.var(data))
    print("СКВ: ", m.sqrt(np.var(data)))





def empirical_cdf(data):
    hist, edges = np.histogram(data, bins=len(data))
    Y = hist.cumsum()
    for i in range(len(Y)):
        plt.plot([edges[i], edges[i+1]],[float(Y[i]/len(Y)), float(Y[i]/len(Y))], c="blue")
    plt.show()


def change_data(data, table_list):
    new_data = data
    
    for i in range(len(table_list)):
        for k in range(len(data)):
            if (table_list[i][0][0]<=data[k]< table_list[i][0][1]):
                    new_data[k] = (table_list[i][0][0]+table_list[i][0][1])/2
    x= len(table_list)-1             
    new_data[len(data)-1] = (table_list[x][0][0]+table_list[x][0][1])/2

    return new_data

def main():
    data = read_dataset(r"C:\Users\Антон\Desktop\КПИ\2 Семестр\Аналіз даних\Лаба 1\File_data.csv")
    print("числові характеристики вибірки")
    character(data)
    #
    print("варіаційний ряд для простої вибірки")
    print(data)

    table_list=internal_var(data)
    #
    print("інтервальний варіаційний ряд для згрупованої вибірки")
    Interval_print(table_list, data)
    new_data=change_data(data, table_list)
    #
    print("числові характеристики вибірки")
    character(data)
    
    
    
    
    empirical_cdf(new_data)
   
    #character(new_data)
    


if __name__ == "__main__":
    main()
