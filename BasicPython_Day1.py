# a=10
# b=10.5
# c="Amit"
# d=True;

# print(a);
# print(b);
# print(c);
# print(d);

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# # list and Dict

# nums =[1,2,3,4]
# print(nums[0]);

# nums.append(5);
# print(nums)
# print(nums[4])


# user={"name": "Amit", "age":"29", "car":"Altroz", "home": "Himachal"}
# print(user);
# #  pop method remove the specified item from the dictionary
# # user.pop("home")
# # print(user);

# # get method retunr the value of the item with the specifed ket
# # x= user.get("name")  
# # print(x)

# # Functions

# def green(name):
#     return f"Hello {name}"
    
# print(green("Amit"))

#----------------------------------------------#

print("Hello word")

name="Amit"
age =15

print("my name is", name);
print("my age is", age);


#Variables and Data Types
a= 10
b=10.5
c="Amit"
d=True

print(type(a))
print(type(b))
print(type(c))
print(type(d))


#Basic Operations and Expressions

print("Basic Operations and Expressions: ")
e=10
f=3
 #Arithmetic Operators

print("addition", e+f)
print("Subtraction", e-f)
print("Multiplication", e*f)
print("Divison", e/f)
print("floor divison", e//f) #quotient
print("Modulus", e%f) #reminder
print("Power", e**f)

#Comparison Operators
g=20
h=4

print(g>h)
print(g<h)
print(g == h)
print(g!=h)

# Logical operator 
x=10;
y=20;
print(x>5 and y>15)
print(x>5 or y<10)
print(not(x>5))



# Conditional Statements (if, elif, else)

age =17

if age>=18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")


   #Multiple Conditions (elif)
marks =75
if marks>=90:
    print("Garde A")
elif marks>=75:
    print("Grade B")
elif marks>=70:
    print("Garde C")
else:
    print("Fail")

    #Nested if

num=-13

if num>0:
    if num%2 == 0:
        print("Postive Even number")
    else:
        print("Postive Odd number")
else:
    print("Negative number")

num = int(input("Enter the number to check even or odd: "))

if num%2==0:
    print("Even number")
else:
    print("Odd number")
    
