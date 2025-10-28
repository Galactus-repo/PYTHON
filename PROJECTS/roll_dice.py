import random

while True:
    choice=input("Do you want me to roll a dice? (Y/N)").lower()
    if choice == 'y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"({die1},{die2})")
    elif choice== 'n':
        print("Ok then, thanks for playing")    
        break
    else:
        print("INVALID INPUT")
        