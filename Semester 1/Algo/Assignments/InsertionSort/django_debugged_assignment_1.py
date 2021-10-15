#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:41:00 2021

@Authors: Adam Sahnoun, Dennis Blaufuss, Lars Wrede, Philipp Voit, Sophie Merl
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd
from time import perf_counter_ns


# basic insertion sort func with clock
def insertion(input_list):
    time_start = perf_counter_ns()
    j = 1
    while j < len(input_list):
        key = input_list[j]
        i = j - 1
        while i > -1 and input_list[i] > key:
            input_list[i + 1] = input_list[i]
            i -= 1
        input_list[i + 1] = key
        j += 1
    time_end = perf_counter_ns()
    time_span = time_end - time_start
    return time_span


# func to run through dataframe, running and logging the output of 'insertion'
def insertion_df(input_df):
    i = 0
    n = len(input_df.index)
    while i < n:
        time_span = insertion(input_df["Numbers"][i])
        input_df["Time_Span"][i] = time_span
        i += 1


"wir machen komischen bums ladidu"
# creation of df for input
data_count = []
data_list = []

n = 10
i = 1
j = 0
while j < n:
    count = i * 25
    data_count.append(count)
    temp_list = list(range(0, count))
    rd.shuffle(temp_list)
    data_list.append(temp_list)
    i *= 2
    j += 1

data = {"Count": data_count, "Numbers": data_list, "Time_Span": list(range(0,
                                                                           n))}


# list for time_span as placeholder -> ugly but works :D
df = pd.DataFrame(data, index=list(range(0, n)))
insertion_df(df)


# Renaming X-Axes-Ticks
def shorten_numbers(num):
    # Variable from symbols will be assigned to form
    form = []
    # Dictionary
    symbols = {"K": 1000, "": 1}
    for i in symbols:
        num_trimmed = num / symbols[i]
        if(num_trimmed >= 1):
            num = num_trimmed
            form = i
            break
    return f"{str(round(num,2)).rstrip('0').rstrip('.')}{form}"


Ticks = []
for i in df["Count"]:
    Ticks.append(shorten_numbers(i))
df["Count_Ticks"] = Ticks
df = df.replace(["250", "500"], "")
# Changing Nanoseconds to Minutes
df["Time_Span_in_Min"] = (df["Time_Span"]/1000000000)/60

# Plot
# Dimension and Style of the Chart
fig, ax = plt.subplots(figsize=(16, 5))
plt.style.use("ggplot")
# Reference Line
ax.axline((0, 0), (df["Count"][8], df["Time_Span_in_Min"][8]),
          color="black",
          linestyle="--",
          label="Reference Line")
# Line Plot
ax.plot(df["Count"], df["Time_Span_in_Min"],
        marker="o",
        color="red",
        label="Time Span")
# Labeling and aligning the axes to 0
ax.set_xlabel("Number of Cards")
ax.set_xlim(xmin=0)
ax.set_ylabel("Time Span in Minutes")
ax.set_ylim(ymin=0)
ax.set_title("Calculate time complexity of insertion sort")
# Renaming X-Axis + Rotation
plt.xticks(df["Count"], np.array(df.iloc[:, 3].apply(str)), rotation=45)
# Legend
fig.legend(loc=1, bbox_to_anchor=(1, 0.15), bbox_transform=ax.transAxes)

plt.show()
