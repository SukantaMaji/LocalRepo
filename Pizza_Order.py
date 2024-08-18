print("~~~~~`Welcome to Pizza shop~~~~~~~`")
s = 15
m = 20
l = 25
pizza = input("What type of pizza you want to eat? small:S medium:M large:L--> ")
if pizza=="S":
    print("You should pay 15$")
    extra_cheese = input("You want Extra cheese? Yes:Y or No:N--> ")
    if extra_cheese=="Y":
        s+=1
        print(f"Your Total bill with extra cheese is = ${s}")
    else:
        print("Your Total bill is = 15$")
elif pizza=="M":
    print("You should pay 20$")
    extra_cheese = input("You want Extra cheese? Yes:Y or No:N--> ")
    if extra_cheese=="Y":
        m+=1
        print(f"Your total bill with extra cheese is = ${m}")
    else:
        print("Your Total bill is = 20$")
elif pizza=="L":
    print("You should pay 25$")
    extra_cheese = input("You want Extra cheese? Yes:Y or No:N--> ")
    if extra_cheese=="Y":
        l+=1
        print(f"Your total bill with extra cheese is = ${l}")
    else:
        print("Your Total bill is = 25$")
else:
    print("Sorry!!!! please Enter a suitable input")
