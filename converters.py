#Learning about Modules Practice.
numbers = [10, 3, 6, 2]
max = numbers [0]
for number in numbers:
    if number > max:
        max = number 
print(max) 

#I'm going to creat a function out of the code above.
def find_max(numbers):
    maximum = [0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


'''
#Learning about Modules.
def lbs_to_kg(weight):
    return weight * 0.45

def kg_to_lbs(weight):
    return weight / 0.45
'''