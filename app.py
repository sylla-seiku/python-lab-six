#Learning about Modules.
import converters # this imports an entire module.
from converters import kg_to_lbs # this imports a spicefic class from a module.
from converters import find_max


print(converters.kg_to_lbs(70)) #on this line we have to prefix this object call with a name of an object.

print(kg_to_lbs(10)) # in this example we dont 

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
#print(max(numbers))
print(maximum)
