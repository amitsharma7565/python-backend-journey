a=10
b=10.5
c="Amit"
d=True;

print(a);
print(b);
print(c);
print(d);

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# list and Dict

nums =[1,2,3,4]
print(nums[0]);

nums.append(5);
print(nums)
print(nums[4])


user={"name": "Amit", "age":"29", "car":"Altroz", "home": "Himachal"}
print(user);
#  pop method remove the specified item from the dictionary
# user.pop("home")
# print(user);

# get method retunr the value of the item with the specifed ket
# x= user.get("name")  
# print(x)

# Functions

def green(name):
    return f"Hello {name}"
    
print(green("Amit"))

