secret_number = 14
num = 0

while(num!=secret_number):
    num = int(input("Please Enter the number:"))
    if(num==secret_number):
        print("Well done, muggle! You are free now.")
    else:
        print("Ha ha! You're stuck in my loop!")
