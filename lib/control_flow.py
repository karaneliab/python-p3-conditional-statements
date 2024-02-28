# !/usr/bin/env python3
def admin_login(username, password):
    if username == 'admin' and password == '12345':
        return "Access granted"
    elif username == 'ADMIN' and password == '12345':
        return "Access granted"
    else:
        return "Access denied"


print(admin_login("admin", "12345"))  
print(admin_login("sudo", "12345"))   
print(admin_login("ADMIN", "12345"))  


def hows_the_weather(temperature):
    # your code here
    if (temperature < 40):
        return"It's brisk out there!"
    elif (temperature >= 40 and temperature <= 65):
        return "It's a little chilly out there!"
    elif (temperature > 85):
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
   
print(hows_the_weather(33))

print(hows_the_weather(99))

print(hows_the_weather(75))


def fizzbuzz(num):
    # your code here
    if(num % 3 ==0):
        return "Fizz"
    elif(num % 5 == 0):
        return "Buzz"
    elif(num % 5 == 0 and num % 3 == 0):
        return"FizzBuzz"
    else:
        return  num

print(fizzbuzz(1))
print(fizzbuzz(0))
print(fizzbuzz(15))
print(fizzbuzz(45))

print(fizzbuzz(2))

print(fizzbuzz(3))

print(fizzbuzz(4))

print(fizzbuzz(5))

print(fizzbuzz(15))
 

def calculator(operation, num1, num2):
    # your code here
    try:
        if operation == '+':
            return num1 + num2
        elif(operation == '-'):
            return num1 - num2
        elif(operation == '*'):
            return num1 * num2
        elif(operation == '/'):
            return num1 / num2
        else:
            print("Invalid operation!")
            return None

   
    except ZeroDivisionError:
 
        print("Cannot be divided by zero.")
        return None
    


print(calculator("+", 1, 1))

print(calculator("-", 3, 1))

print(calculator("*", 3, 2))

print(calculator("/", 4, 2))

print(calculator("nope", 4, 2))
print(calculator("/", 4, 0))








# n = 4
# for i in range (n ,0,-1):
#     print( ' ' * (n-i) * 2 +"* "  * (2 * i -1))

# n=45
# result = 0
# # keep dividing  by 10 until it becomes zero,increment the result count each time
# while (n != 0):
#     n = n // 10
#     result += 1
#     # print(n)
# print(result)
  