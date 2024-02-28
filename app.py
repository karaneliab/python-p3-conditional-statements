dog = "cuddly"
if dog == "hungry":
    owner = "refilling food bowl"
elif dog == "thirsty":
    owner = "Refiling water bowl"
elif dog == "playful":
    owner = "plying-tug-of-war"
elif dog == "cuddly":
    owner = "Snugling"
else:
    owner = "Reading newspaper"
   

def control_flow(value):
    if value:
        print("yep!")
    else:
        print("nope!")
control_flow(False)
control_flow("0")

def show_age(age):
    if age < 5:
      is_baby = 'baby'
    else:
      is_baby = 'not a baby'
    
    print(is_baby)
show_age(7)
show_age(3)

def show_age(age):
    if age < 5:
        is_baby = 'baby'
    else:
        is_baby = 'not a baby'
    
    print(is_baby)
show_age(3)  
show_age(7)  

def divide(num1,num2):
    try:
        quotient = num1/num2
        print(quotient)
    except ZeroDivisionError:
        print('Error; num2 cannot be equal to zero')
    except TypeError:
        print("Error:input must be type int or float")
    finally:
        print("Isn't division fun?")
divide(5,0)
divide(10,2)


#  an else example
def serve_coffee(coffee):
    if coffee == "empty":
        print("refill")
    elif coffee == "half_full":
        print("fill the coffee cup")
    else :
        print("Leave it that way")
serve_coffee("empty")
serve_coffee("half_full")
serve_coffee("full")  

def grading_display(grade):
    if grade == 'A':
        print('excellent score')
    


    