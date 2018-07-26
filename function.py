# n1 = 1
# n2 = 2

# print(n1+n2)
# print(n1-n2)
# print(n1*n2)

def hello(name='G7yi', age='10'):
    print("Hello, " + name)
    print(age + "years old")

# typing = input("What is your namr? ")
# hello(typing)

name = input("Your Name: ")
age = input("How old are you? ")
hello(name, age)
hello(name)
hello()
hello(age='60', name='artrun')
