#List in python
numbers =[10,20,30,40,20]
print(numbers)
print(numbers[0])

# add the element in the list
numbers.append(50)
print(numbers)

# insertion at position
numbers.insert(1, 99)
print(numbers)

# remove the element
numbers.remove(20)
print(numbers)

# Loop through list
for num in numbers:
    print(num)

# tuples
data=(10,20,30)
print(data[2])

#dictonaries(key value pair)

student={
    "name":"Amit",
    "age":"25",
    "city":"HP"
}

print(student["name"])
print(student["age"])

# add new key
student["marks"]=90

print(student["marks"])

# update the value in dictonaries
student["age"]=28

print(student["age"])

# Loop in dictionary
for key, value in student.items():
    # print("The key  is", key,  " and the value is", value)
    print(f"The key  is {key} and the value is {value}")
    
#  set 
numss={1,2,3,4,3,5};
print(numss)

numss.add(6);
print(numss)


a={1,2,3,4,7}
b={3,4,5,7}

print(a.union(b))# discards the duplicate value
print(a.intersection(b)) # give the common value in set


#Loops in python
i=1
while i<=5:
    print(i)
    i+=1 # i=i+1;

#loops throug the list
names=["Amit","Rahul", "Neha"]
for name in names:
    print(name)

# functions (block of reuseable code)
def greet():
    print("Hello first fxn")

greet()

# function with parameter
def greet(name):
    print(f"Hello {name}")

greet("Amit")

#  function with return value 
def add(a,b):
    return a+b;

result= add(4,5)
print(result)


# built in functions

print(len("Hello"))
print(type(1.1))
print(max(10,5,11))
print(min(-1,0,9,-10))
print(sum([1,2,3]))
print(sorted([3,-1,2]))

for i in range(1,7):
    print(i)

# TypeCasting
e="1"
print(type(e))

b=(int(e))
print(type(b))

print(b+5)

# commom conversion
f=int("10")
print(type(f))
g=float("10.5")
print(type(g))
j=str(100)
print(type(j))
t=list((1,2,3))
print(t)
print(type(t))
y=tuple([1,2,3,4])
print(y)
print(type(y))
o=set([1,5,6,8])
print(o)
print(type(o))

#  small question 
numbers= [1,2,3,4,5,6,7]

def square_list (lst):
    result =[]
    for num in lst:
        result.append(num*num)
    return result;

print(square_list(numbers))
