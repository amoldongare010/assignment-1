# Write a program to print your name.

print ("amol")

# Write a program for a Single line comment and multi-line comments.

print("single line comment ")


#multi line comment
#task  to add 
#two number 
#a and b
a=10
b=20
print (a+b)



# Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
a = 10
print(type(a))

b = True
print(type(b))

c = 1.234
print( type(c))

String = 'amoldongare'
print( type(String))

# Define the local and Global variables with the same name and print both variables and understand the scope of the variables.

a=5
def funct2():
    a=10
    print ("local a :",a)


print("global a :",a )
funct2()
print ("global a:",a)
