# #made by me calculator
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
    print(val)
    dec = input("Want to continue: 'yes' or 'no'\n")
    if dec =="no":
        new_calc=False
print("Thank you!")

# game = fun(num1,num2)
# print(game)

