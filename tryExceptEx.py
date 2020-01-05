#example for using try, except and if statement
try:
    num = int(input("put your random number"))
except:
    print("you forgot to put your number")
if num > 100:
    print("the number is greater than 100")
if num % 2 == 0:
    print("the number is even")
else:
    print("thanks for putting your number. bye!")
