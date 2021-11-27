import random
import statistics
import plotly.figure_factory as ff
import csv
import pandas as pd
import plotly.express as px
import numpy as np
#"gender","race/ethnicity","parental level of education","lunch","test preparation course","math score","reading score","writing score"
df = pd.read_csv("StudentsPerformance.csv")
mathList = df["math score"].to_list()

mean = sum(mathList)/len(mathList)
print("Mean :" ,mean)
median = statistics.median(mathList)
print("Median :" ,median)
mode = statistics.mode(mathList)
print("Mode :" ,mode)

std_devi = statistics.stdev(mathList)
print("The standard deviation is " + str(std_devi))



standard_start1, standard_end1 = mean - std_devi, mean + std_devi
list_of_data_within_1_std_deviation = [result for result in mathList if result > standard_start1 and result < standard_end1]


print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(mathList)))

standard_start2, standard_end2 = mean - (2*std_devi), mean + (2*std_devi)
list_of_data_within_2_std_deviation = [result for result in mathList if result > standard_start2 and result < standard_end2]


print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(mathList)))

standard_start3, standard_end3 = mean - (3*std_devi), mean + (3*std_devi)
list_of_data_within_3_std_deviation = [result for result in mathList if result > standard_start3 and result < standard_end3]


print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(mathList)))