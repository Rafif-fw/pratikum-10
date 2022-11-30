# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:04:20 2022

@author: Rafif Fernanda
"""

def insertion_sort(array):
    # perulangan pertama 
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array
unordered = [91, 21, 37, 77, 82]
print(insertion_sort(unordered))