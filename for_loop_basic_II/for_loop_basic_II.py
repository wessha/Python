#1
def biggie_size(list):
    for i in range(0, len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list

result = biggie_size([-1, 3, 5, -5])
print(result)  

#2
def count_positives(list):
    count = sum(1 for num in list if num > 0)
    list[-1] = count
    return list


result1 = count_positives([-1, 1, 1, 1])
print(result1)  

result2 = count_positives([1, 6, -4, -2, -7, -2])
print(result2)  

#3
def sum_total(list):
    return sum(list)


result1 = sum_total([1, 2, 3, 4])
print(result1)  

result2 = sum_total([6, 3, -2])
print(result2)  

#4
def average(list):
    if not list: 
        return 0 
    return sum(list) / len(list)


result = average([1, 2, 3, 4])
print(result)  

#5
def length(list):
    return len(list)

result1 = length([37, 2, 1, -9])
print(result1)  

result2 = length([])
print(result2)  

#6
def minimum(list):
    if not list:  
        return False
    return min(list)

result1 = minimum([37, 2, 1, -9])
print(result1)  

result2 = minimum([])
print(result2)  

#7
def maximum(list):
    if not list:  
        return False
    return max(list)

result1 = maximum([37, 2, 1, -9])
print(result1)  

result2 = maximum([])
print(result2)  

#8
def ultimate_analysis(lst):
    if not lst:  
        return {}

    result = {
        'sumTotal': sum(lst),
        'average': sum(lst) / len(lst),
        'minimum': min(lst),
        'maximum': max(lst),
        'length': len(lst)
    }
    return result

result = ultimate_analysis([37, 2, 1, -9])
print(result)  

#9
def reverse_list(lst):
    lst[:] = lst[::-1]
    return lst

result = reverse_list([37, 2, 1, -9])
print(result) 
