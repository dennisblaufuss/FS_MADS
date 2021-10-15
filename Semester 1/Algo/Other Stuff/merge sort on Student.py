# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
" """
def merge(r_list, l_list):
    return_list = []
    i = 0
    j = 0
    while i < len(r_list) and j < len(l_list):
        if r_list[i] < l_list[j]:
            return_list.append(r_list[i])
            i += 1
        elif r_list[i] > l_list[j]:
            return_list.append(l_list[j])
            j += 1
        else:
            return "list cannot contain duplicates"
            break
    return_list += r_list[i:]
    return_list += l_list[j:]
    return return_list
    
def merge_sort(input_list):
    if len(input_list) < 2:
        return input_list
    mid = len(input_list)//2
    r_list = merge_sort(input_list[mid:])
    l_list = merge_sort(input_list[:mid])
    return merge(r_list, l_list)

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def set_last_name(self, last_name):
        self.last_name = last_name
        
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def __lt__(self, other):
        if self.last_name == other.last_name:
            return self.first_name < other.first_name
        return self.last_name < other.last_name
     
    def __gt__(self, other):
        if self.last_name == other.last_name:
            return self.first_name > other.first_name
        return self.last_name > other.last_name
    
kilian = Student("Kilian", "Verweyen")
vahe = Student("Vahe", "Andonians")
dennis = Student("Dennis", "Blaufss")
sophie = Student("Sophie", "Merl")
merlin = Student("Merlin", "Merl")

in_l = [kilian, vahe, dennis, sophie, merlin]

temp = merge_sort(in_l)

in_l[0].__str__()

out_l = []

i = 0
while i < len(temp):
    out_l.append(temp[i].__str__())
    i += 1

