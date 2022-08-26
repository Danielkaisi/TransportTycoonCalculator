import random

OnePickupUW = float(1)
OnePickupTW = float(0.25)
OnePickupLogs = float(1)
OnePickupQR = float(1)
FourOrMore = True

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

while FourOrMore == True:
    HowMuchConcreteDoYouWant = input("How much concrete do you want to make? Numbers only ")
    
    if isfloat(HowMuchConcreteDoYouWant) == False:
        print("Please use numbers only (ex. 17)")
        continue
    
    HowMuchConcreteDoYouWantFloat = float(HowMuchConcreteDoYouWant)
    
    if HowMuchConcreteDoYouWantFloat < 3:
        print("Please input at least 4")
        FourOrMore = True
    
    elif HowMuchConcreteDoYouWantFloat >= 4:
        HowMuchConcreteDoYouWantFloat = float(HowMuchConcreteDoYouWant)
        print("You need to pick up ")
        print(OnePickupUW*HowMuchConcreteDoYouWantFloat, "Unfiltered Water", HowMuchConcreteDoYouWantFloat*100, "kg Total")
        print(OnePickupTW*HowMuchConcreteDoYouWantFloat,"Toxic Waste", HowMuchConcreteDoYouWantFloat*27.5, "kg Total")
        print(OnePickupLogs*HowMuchConcreteDoYouWantFloat,"Logs", HowMuchConcreteDoYouWantFloat*60, "kg Total")
        print(OnePickupQR*HowMuchConcreteDoYouWantFloat,"Quarry Rubble", HowMuchConcreteDoYouWantFloat*150, "kg Total")
        print("That's", (HowMuchConcreteDoYouWantFloat*150)+(HowMuchConcreteDoYouWantFloat*60)+(HowMuchConcreteDoYouWantFloat*27.5)+(HowMuchConcreteDoYouWantFloat*100), "kg Total" )
        FourOrMore = False