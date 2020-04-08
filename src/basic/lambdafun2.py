double = lambda x:x * 2

sequence = [1, 3, 5, 7, 9]
# doubled = [double(x) for x in sequence] # 1. called list comprehension
#OR
# doubled = [(lambda x:x * 2)(x) for x in sequence] #2 Use lambda function in list comprehension
#OR
# doubled = map(double, sequence) #3. map funtion(javascript like program)
#OR
doubled = map(lambda x:x * 2, sequence) #4. map funtion with lambda function


print(list(doubled))


"""
***NOTE: List comprehension is faster than map
"""