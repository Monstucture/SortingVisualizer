import random
import time
import visualizer


class Algorithm:
    def __init__(self, name):
        self.array = random.sample(range(512), 512)  # Random array of 512 in size
        self.name = name

    def update_dis(self, swap1=None, swap2=None):
        visualizer.update(self, swap1, swap2)

    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed

class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            min_i = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_i]:
                    min_i = j
            self.array[i], self.array[min_i] = self.array[min_i], self.array[i]
            self.update_dis(self.array[i], self.array[min_i])

class BublleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            self.update_dis(self.array[i], self.array[j+1])

class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            cursor = self.array[i]
            idx -= 1
        self.array[idx] = cursor
        self.update_dis(self.array[idx], self.array[i])

class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self, array=[]):
        if array == []:
            array = self.array
        if len(array) < 2:
            return array

        mid = len(array)/2
        left = self.algorithm(array[:mid]) 
        right = self.algorithm(array[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                result.append(left[i])
                i+=1
            pass