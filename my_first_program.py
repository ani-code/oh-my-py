#BUILD A CALC with 4 functions and 2 numbers
fn=input("What do you want to do?")

#only asks for a number if input in below 4
if fn in ('+','-','/','*'):
    num1 = float(input("Enter number 1"))
    num2 = float(input("Enter number 2"))

    if fn == '+':
        print(num1 ,fn, num2," = ")
        print(num1+num2) 
        
    elif fn == '-':
        print(num1 ,fn, num2," = ")
        print(num1-num2)
    elif fn == '*':
        print(num1 ,fn, num2," = ")
        print(num1*num2)
    elif fn == '/':
        print(num1 ,fn, num2," = ")
        print(num1/num2)
else:
    print("Invalid input! select + - / or *")