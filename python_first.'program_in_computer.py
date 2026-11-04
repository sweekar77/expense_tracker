student = {
    "name": "sweekar",
    "age" : "14",
    "grade" : "8"
    }
print(student["name"])

print(student.items())

def add(age,grade):
    return age + grade
result = add( 14, 8 )
print(result)

for key, value in student.items():
    print(key , value)

my_set = {"orange", "apple", "banana"}
print(len(my_set))
my_set.remove("orange")
print(my_set)
my_set.add("pineapple")
print(my_set)
a = {1,2,3}
b = {4,5,6,3}
print(a - b)
name = "sweekar"
numbers = [i for i in range(1, 21,1)]
print(numbers)
num1 = [x**3 for x in range(1,6,1)]
print (num1)
import numpy as np
matrix = np.array([
    [1,2,3],
    [4,5,6]
])
print(matrix)
print(matrix.shape)
print(matrix[0, 1])
print(np.mean(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print("program over")
print("sike")
d = ([
    [1,2,3],
    [4,5,6]
    ])
e = ([
    [7,8,9],
    [10,11,12]
    ])
print(np.subtract(d,e))