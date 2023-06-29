#sign in
import math
print(" Welcome to the online banking applications ")
name = ''
pin = ''
cb = 0
def signin():
    global name, pin  #username
    name = str(input("Please create your username = ")).lower()
    pin = str(input("Please create your 4 digits pin = "))
    if len(pin) ==4:
        pin= pin
    else:
        print(" The pin has to be in 4 digits")
        newpin = str(input("Please create your 4 digits pin = "))
        if len(newpin)!=4:
            print("The pin has to be in 4 digits")
            signin()
        else:
            pin= newpin
    print(" Thanks for creating your bank account")

#for recoverpin
def forgetpin():
    recoverpin = str(input("Please create your new 4 digits pin "))
    if len(recoverpin) !=4:
        print("The pin has to be in 4 digits")
        forgetpin()
    else:
        print(" Then new pin has been stored. Please login ")    
        pin = recoverpin
        login()


def depositinterest(p,r,t):  #p=principle  #r= interest rate # t=time
    #A= Pe^rt formula to calculate compound interest
    p=float(p)
    r=float(r)
    t=float(t)
    rt = r*t
    e= math.exp(rt)
    #calculations
    a= p*e  # Future value of your investement
    return a
    
def login():
    global cb
    # make1 represents username
    # pin1  represents user's pin
    name1 = str(input("Please enter your username = ")).lower()
    pin1 = str(input("Please enter your pin = "))
    #check if the name and pin matched
    if name1 == name and pin1 == pin :
        print("Welcome to the online banking application" + " " + name)
        print(" Please choose the menu down here : ")
        listmenu = ["1-Deposit", "2-withdraw", "3-Transfer amount", "4-Check balance","5-Deposit interest rate", "6- calculate compound interest"]
        for b in listmenu:
            print(b)
        choose = int(input(" Please enter the number of your choice = "))
        d = 0  #d represent deposit
        w =0   #w represents withdraw
          #cb is current balance
        if choose ==1:
            d = int(input(" Enter the amount of your deposit = "))
            cb= d
            print(" Your current balance is" +" "+ str(cb))
        elif choose ==2:
            w = int(input(" Enter the amount of money that yau want to withdraw= "))
            if w > cb:
                print(" Your current balance is not sufficient for this transcation! ")
                login()
            else:
                cb -= w
                print(str(w) +" "+ "has been withdrawn from your account" +" "+ "  and  your current balance is" + " "+ str(cb) )
        elif choose ==3:
            destination =str(input(" Please enter the account number of your destination in 8 digits "))
            if len(destination) ==8:
                amount= int(input("Please enter the amount of money you wants to transfer "))
                if amount > cb:
                    print("Your current balance is not sufficient for this transcation ")
                    login()
                else:
                    cb -= amount
                    print(" The transaction of " + " "+ str(amount) + " " + "has been transfered to" + " " +str(dest) +" " +" your current balance is" + str(cb))
            else:
                print("The transaction has been rejected since the destination account number is invalid!! ")
                login()
        elif choose ==4:
            print("Your current balance is" +" "+ str(cb))
        elif choose ==5:
            if d > 50000:
                rate =3
            elif d > 30000:
                rate =2
            else:
                rate =1.5   
            print("Your current deposit interest rate is" +" "+ str(rate) + " %")
        elif choose== 6:
            listoption = ["1-Calculate your deposit compound interest based on your CB", "2-Calculate your deposit compound interest based on your deposit input"]
            for n in listoption:
                print(n)
            choice = int(input("Please enter your choice from the option above"))
            if choice ==1:
                timing = str(input(" How many years you want to invest your money" ))
                if d > 50000:
                    ratex = 3/100
                elif d > 30000:
                    ratex = 2/100
                else:
                    ratex = 1.5/100
                print("Your current balance in" + " "+ "timing" +" " + "Years will be")
                print(depositinterest(cb, ratex, timing))

            elif choice ==2:
                timing1 = str(input("How many years you want to invest your money "))
                money = str(input(" Please enter the amount of money you would like to deposit = "))
                money = int(money)
                if d > 50000:
                    ratex = 3/100
                elif d > 30000:
                    ratex = 2/100
                else:
                    ratex = 1.5/100
                print("Your current balance in" + " "+ "timing" +" " + "Years will be")
                print(depositinterest(money, ratex, timing))
        else:
            print(" Option you have entered is invalid,  back to main menu")
            login()
    else:
        print("Either of your username or pin is wrong, did you create your account ")
        list1 = ["1=yes", "2-no"]
        for i in list1:
            print(i)
        inp = int(input("Enter your choice below= "))
        if inp == 1:
            list2 = ["1-Do you want to attempt to login again?", "2-You forget your pin"]
            for e in list2:
                print(e)
            theanswer = str(input(" Please enter your choice = "))
            theanswer = int(theanswer)
            if theanswer ==1:
                login()
            elif theanswer ==2:
                forgetpin()
            else:
                print("Option is not available!")
                login()
        elif inp ==2:
            print(" Please create your account first!! ")
            signin()
    exit()       

def mainmenu():
    optionone = int(input("Choose 1 to signin and choose 2 to login"))
    if optionone ==1:
        signin()
    elif optionone ==2:
        login()
    else:
        print("Option is not available")
        mainmenu()
    exit()

def exit():
    answer = str(input("Do you still want to conduct transaction? yes or no")).lower()
    if answer == "yes":
        login()
    elif answer =="no":
        print("Thank you for using this app")
    else:
        print("Option is not available")
        mainmenu()
mainmenu()
