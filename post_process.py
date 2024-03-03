import numpy as np

bias = 187500.02235174447

path = "./best_data_left/OpenBCI-RAW-2024-03-02_15-08-54.txt"

file = open(path, mode="r").readlines()

data = []

for line in file:
    if "%" not in line:
        results = line.rstrip().split(", ")
        data.append([results[0], results[3], results[6]])

for d in range(1, len(data)):
    data[d] = [float(data[d][0]), (float(data[d][1]) + bias) / 1000, (float(data[d][2]) + bias) / 1000]


print(data[-1])
