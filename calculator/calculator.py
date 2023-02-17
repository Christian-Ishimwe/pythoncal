'''this programn created calculator
which allow continuous calculatiotion using while loop!
'''
from logo import logo
print(logo)
operators={"+":"add",
   "-":"sub" ,
   "*":"multi",
   "/": "div"
   
   }
new_calc=True
while new_calc is True:
    num1=int(input("Enter the first number: "))
    for i in operators:
        print(i)
    oper=input("Enter the operator: ")
    num2= int(input("Enter the second number: "))
    def add(num1,num2):
        return num1+num2
    def sub(num1,num2):
        return num1-num2
    def multi(num1,num2):
        return num1*num2
    def div(num1,num2):
        return num1/num2
    if oper=="+":
        val=add(num1,num2)
    elif oper=="-":
        val=sub(num1,num2)
    elif oper=="*":
        val=multi(num1,num2)
    elif oper=="/":
        val=div(num1,num2)
    print(f"{num1} {oper} {num2} = {val}")
    dec = input(f"Want to use  new inputs: 'yes' or 'no'\n")
    if dec =="no":
        new_calc=False
def new_function():
    num1=int(input("Enter the first number: "))
    for i in operators:
        print(i)
    oper=input("Enter the operator: ")
    num2= int(input("Enter the second number: "))
    def add(num1,num2):
        return num1+num2
    def sub(num1,num2):
        return num1-num2
    def multi(num1,num2):
        return num1*num2
    def div(num1,num2):
        return num1/num2
    if oper=="+":
        val=add(num1,num2)
    elif oper=="-":
        val=sub(num1,num2)
    elif oper=="*":
        val=multi(num1,num2)
    elif oper=="/":
        val=div(num1,num2)
    print(f"{num1} {oper} {num2} = {val}")
    dec = input("Want to Enter new inputs: 'yes' or 'no'\n")
    if dec =="no":
        new_calc=False
while new_calc==False:
    num1=val
    print(f"perform operations on {val}")
    oper=input("Enter the operator: ")
    num2= int(input("Enter the second number: "))
    def add(num1,num2):
        return num1+num2
    def sub(num1,num2):
        return num1-num2
    def multi(num1,num2):
        return num1*num2
    def div(num1,num2):
        return num1/num2
    if oper=="+":
        val=add(num1,num2)
    elif oper=="-":
        val=sub(num1,num2)
    elif oper=="*":
        val=multi(num1,num2)
    elif oper=="/":
        val=div(num1,num2)
    print(f"{num1} {oper} {num2} = {val}")
    dec = input("Want to inputs new values: 'yes' or 'no'\n")
    if dec =="yes":
        new_calc=True
    while new_calc is True:
        new_function()
        
    
    

# game = fun(num1,num2)
# print(game)

