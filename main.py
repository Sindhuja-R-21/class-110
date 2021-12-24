import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("data.csv")
data=df["temp"].to_list()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("Population Mean = ",population_mean)
print("Std_deviation=",std_deviation)


def random_set_of_means():

    dataset=[]

    for i in range(0,100):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean



def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()


def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_means()
        mean_list.append(set_of_means)
    show_fig(mean_list)


setup()


