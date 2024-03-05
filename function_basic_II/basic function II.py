#1
def countdown(n):
    return list(range(n, -1, -1))

result = countdown(5)
print(result)  

#2
def print_and_return(nums):
    print(nums[0])
    return nums[1]

#3
def first_plus_length(list):
    return list[0] + len(list)

#4
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    
    second_value = lst[1]
    new_list = [value for value in lst if value > second_value]
    
    print(len(new_list))
    return new_list

#5
def length_and_value(size, value):
    return [value] * size
