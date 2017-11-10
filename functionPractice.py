# Function that prints the result
def sum_print(a, b):
    result = a + b
    print(result)
 
# Function that returns the results
def sum_return(a, b):
    result = a + b
    return result
 
# This prints the sum of 4+4
sum_print(4, 4)
 
# This does not
sum_return(4, 4)
 
# This will not set x1 to the sum
# It actually gets a value of 'None'
x1 = sum_print(4, 4)
 
# This will
x2 = sum_return(4, 4)

def volume_cylinder(radius, height):
    """Returns volume of a cylinder given radius, height."""
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume
