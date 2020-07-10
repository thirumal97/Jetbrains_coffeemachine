"""
print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")
# Write your code here
print("Write how many cups of coffee you will need: ")
a = int(input())
print("For ", a ," cups of coffee you will need:")
print(200*a, "ml of water")
print(50*a, "ml of milk")
print(15*a, "g of coffeee beans")


print("Write how many ml of water the coffee machine has:")
n= int(input())
print("Write how many ml of milk the coffee machine has:")
a = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
b =int(input())
print("Write how many cups of coffee you will need:")
c= int(input())
if n//200 <= a//50 and n//200 <= b//15:    
    N = n//200
elif a//50 <= b//15 and a//50 <= n//200:
    N = a//50
else:
    N =b//15                                                                                                                                                                       
if n//200 == c and a//50 == c and b//15 ==c:
    print("Yes, I can make that amount of coffee")
elif n//200 >= c and a//50 >= c and b//15 >=c:  
    print("Yes, I can make that amount of coffee (and even",N-c,"more than that)") 
    
else:
     print("No, I can make only",N,"cups of coffee")   
     
"""

water = 400
milk = 540
coffee_beans=120
cups = 9
money = 550

def coffee_machine():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee_beans,"of coffee beans")
    print(cups,"of disposable cups")
    print("${} of money".format(money))    

def buy():
    global money
    global water
    global coffee_beans
    global cups
    global milk
    print()
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu:")
    n = (input())
    if n == "1":
       if water >= 250 and coffee_beans >=16 and cups >=1 :
           water = water -250
           coffee_beans = coffee_beans -16
           money = money + 4
           cups = cups-1
           print("I have enough resources, making you a coffee!")
                        
    elif n == "2":
        if water >= 350 and milk >=75 and coffee_beans >=20 and cups >=1:
            money = money + 7
            water =water -350
            milk = milk - 75
            cups = cups -1
            coffee_beans = coffee_beans -20
            print("I have enough resources, making you a coffee!")
            
        else:
            print("Sorry not enough water!")    
    elif n == "3":
        if water >= 200 and milk >= 100 and coffee_beans>=12 and cups >=1:
            money = money + 6
            water =water -200
            cups = cups -1
            milk = milk -100
            coffee_beans = coffee_beans -12
            print("I have enough resources, making you a coffee!")
    #elif n == "back":
         
            
        
def fill():
    global money
    global water
    global coffee_beans
    global cups
    global milk
    print()
    print("Write how many ml of water do you want to add:")
    b = int(input())
    water = water + b
    print("Write how many ml of milk do you want to add:")
    c= int(input())
    milk = c +milk
    print("Write how many grams of coffee beans do you want to add:")
    d = int(input())
    coffee_beans = coffee_beans + d
    print("Write how many disposable cups of coffee do you want to add:")
    e =int(input())
    cups =cups+e
    print()
    #coffee_machine()
       
def take():
    global money
    print()
    print("I gave you ${}".format(money))
    money = 0
    

def remaining():
    print()
    coffee_machine()

def exit():
    pass
            
    
    
while True: 
    print("Write action (buy, fill, take, remaining, exit):")
    n = input()
    if n=="buy":
        buy()
        print()
    if n=="take":
        take() 
        print()
    if n=="fill":
        fill()
        print()
    if n=="remaining":
        remaining()   
        print()
    if n=="exit":
        
       break
    if n == "Back":
       continue   
        