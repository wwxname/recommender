import math

import numpy as np


class DataNorm:
    def __init__(self):
        self.arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99, 999]
        self.res = []
        self.x_max = max(self.arr)
        self.x_min = min(self.arr)
        self.x_mean = sum(self.arr) / len(self.arr)
        self.x_std = np.std(self.arr)

    ## 最小最大数据标准化
    def min_max(self):
        self.res.clear()
        for x in self.arr:
            self.res.append(round((x - self.x_min) / (self.x_max - self.x_min), 4))

    def z_score(self):
        self.res.clear()
        for x in self.arr:
            self.res.append(round((x - self.x_mean) / self.x_std, 4))

    def decimal_scaling(self):
        self.res.clear()
        abs_max = max([abs(ele) for ele in self.arr])
        i = 1
        while math.pow(10, i) < abs_max:
            i = i + 1
        for x in self.arr:
            self.res.append(round(x / math.pow(10, i), 4))

    def print(self):
        print("arr : ", self.arr)
        print("mean :", self.x_mean, ",std :", self.x_mean)
        print("res : ", self.res)


if __name__ == '__main__':
    data = DataNorm()
    # data.min_max()
    # data.z_score()
    data.decimal_scaling()
    data.print()
