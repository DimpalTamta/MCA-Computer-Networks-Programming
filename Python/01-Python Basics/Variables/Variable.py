# A variable is a container used to store data that can be referenced and modified in a program.
# Declaring Variables
age = 25          # integer
height = 5.9      # float
name = "Dimpal"   # string
is_student = True # boolean

# Printing variables
print("Age:", age)
print("Height:", height)
print("Name:", name)
print("Is Student:", is_student)

# Variable Types (Dynamic Typing)
print(type(age))        # int
print(type(height))     # float
print(type(name))       # str
print(type(is_student)) # bool

# Type Conversion
age_str = str(age)
print(age_str, type(age_str))  # '25' <class 'str'>

height_str = "6.1"
print(float(height_str), type(float(height_str)))  # 6.1 <class 'float'>

# Dynamic Typing
var = 10
print(var, type(var))   # int

var = "Hello"
print(var, type(var))   # str

var = 3.14
print(var, type(var))   # float

