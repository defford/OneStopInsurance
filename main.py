# Add in needed libraries
import datetime
from functions import PPrint, AddMonths

# 
with open("Const.dat", "r") as f:
    fContent = f.read()

fList = fContent.split(",")

POLICY_NUM = int(fList[0])
BASIC_PREM = float(fList[1])
ADD_CAR_DISCOUNT = float(fList[2])
EXTRA_LIABILITY_COST = float(fList[3])
GLASS_COST = float(fList[4])
LOANER_CAR_COST = float(fList[5])
HST_RATE = float(fList[6])
PROCESSING_FEE = float(fList[7])

curDate = datetime.datetime.now()

provinces = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
PayOptions = ["Full", "Monthly"]
prevClaims = []

while True:

    firstName = "Daniel" # input("Enter customer's first name: ").lower().title()
    lastName = "Efford" # input("Enter customer's last name: ").lower().title()    
    address = "5 Cornhole Ave" # input("Enter customer's address: ").lower().title()
    city = "Some City" # input("Enter customer's city: ").lower().title()

    while True:
        province = "NL" # input("Enter customer's province (XX): ").upper()
        if province in provinces:
            break
        else:
            print("Please enter a valid province.")

    postalCode = "A2B 1G8" # input("Enter customer's postal code: ").upper()
    phoneNum = "709-727-0484" # input("Enter customer's phone number: ")
    numCars = 3 # int(input("How many cars are being added to insurance?: "))

    while True:
        extraLiability = "N" # input(f"Does {firstName} need extra Liability (Y/N)? ").upper()
        if extraLiability == "Y" or extraLiability == "N":
            break
        else:
            print("Please enter a valid option.")
    
    
    while True:
        glassCoverage = "N" # input(f"Does {firstName} need glass coverage (Y/N)?: ").upper()
        if glassCoverage == "Y" or glassCoverage == "N":
            break
        else:
            print("Please enter a valid option.")

    while True:
        loanerCar = "Y" # input(f"Does {firstName} need a loaner (Y/N)?: ").upper()
        if loanerCar == "Y" or loanerCar == "N":
            break
        else:
            print("Please enter a valid option.")            

    while True:
        payOption = "Full" # input(f"How would firstName like to pay (Full or Monthly)?: ").lower().title()
        downPayment = 5000 # int(input("Enter firstName's down payment amount (Enter 0 if no down payment): "))
        if payOption in PayOptions:
            break
        else:
            print("Please enter a valid option.")


    while True:
        prevClaim = []
        claimNum = 41 # int(input(f"Enter claim number for {firstName} {lastName}: "))
        claimDate = "2024-02-02" # input(f"Enter date for claim #{claimNum}: ")
        claimAmt = 45000.00 # float(input("Enter the claim amount: "))
        prevClaim.append([claimNum, claimDate, claimAmt])

        prevClaims.append(prevClaim)
        
        while True:
            continuePrevClaims = "N" # input("Would you like to enter another claim (Y/N)?: ").upper()

            if continuePrevClaims not in ["Y", "N"]:
                print("Please enter a valid option")
            else:
                break

        if continuePrevClaims == "N":
            PPrint(46, ("+", "left"), (f"{'-' * 44}", "center"), ("+", "right"))
            PPrint(46, ("|", "left"), (f"Previous claims for {firstName} {lastName}", "center"), ("|", "right"))
            PPrint(46, ("+", "left"), (f"{'-' * 44}", "center"), ("+", "right"))
            PPrint(46, ("Claim #", "left"),("Claim Date", "center"),("Amount", 46, "right"))      
            PPrint(46, ("-" * 46, "center"))  

            for prevClaim in prevClaims:
                for claimDetails in prevClaim:    
                    PPrint(46, (f"{claimDetails[0]}", 5, "right"),(f"{claimDetails[1]}", "center"),(f"${claimDetails[2]:,.2f}", 46, "right"))

            print()

            while True:
                confirmPrevClaims = "Y" # input("Confirm previous claims entry (Y/N)?: ").upper()
                if confirmPrevClaims == "Y":
                    break
                elif confirmPrevClaims == "N":
                    prevClaims = []
                    break
                else:
                    print("Please enter a valid option.")
            
            break

    # Perform calculations

    premiumCost = BASIC_PREM + BASIC_PREM * ADD_CAR_DISCOUNT * (numCars - 1)

    totalExtraCost = 0
    totalExtraCost += EXTRA_LIABILITY_COST * numCars if extraLiability == "Y" else 0
    totalExtraCost += GLASS_COST * numCars if glassCoverage == "Y" else 0
    totalExtraCost += LOANER_CAR_COST * numCars if loanerCar == "Y" else 0

    totalInsurancePremium = totalExtraCost + totalExtraCost

    hstCost = totalInsurancePremium * HST_RATE

    totalCost = totalInsurancePremium + hstCost

    totalOwing = totalCost - downPayment

    monthlyPayment = (totalOwing + PROCESSING_FEE) / 8
    
    firstPaymentDate = AddMonths(curDate, 1)

    continueScript = input("Do you want to continue (Y/N)?: ").upper()
    if continueScript == "N":
        break


# Display all output values into a nicely formatted receipt

print()
PPrint(60, ("+", "left"), (f"{'-' * 58}", "center"), ("+", "right"))
PPrint(60, ("|", "left"), ("ONE STOP INSURANCE COMPANY", "center"), ("|", "right"))
PPrint(60, ("+", "left"), (f"{'-' * 58}", "center"), ("+", "right"))
print()
PPrint(60, ("+", 17), ("-" * 24, "center"), ("+", 41))
PPrint(60, ("|", 17), ("Customer Details", "center"), ("|", 41))
PPrint(60, ("+", 17), ("-" * 24, "center"), ("+", 41))
print()
PPrint(60, (f"{firstName} {lastName}", "left"), (f"{address}", "right"))
PPrint(60, (f"{phoneNum}", "left"), (f"{city}, {province}  {postalCode}", "right"))
print()
PPrint(60, (f"# of cars: {numCars}", "left"), (f"Extra liability: {extraLiability}", "right"))
PPrint(60, )



    # print(f"Policy #: {POLICY_NUM}\n"
    #     f"Basic Premium: {BASIC_PREM}\n"
    #     f"Addition Car Discount: {ADD_CAR_DISCOUNT}\n"
    #     f"Extra Liability Cost: {EXTRA_LIABILITY_COST}\n"
    #     f"Glass Coverage Cost: {GLASS_COST}\n"
    #     f"Loaner Car Cost: {LOANER_CAR_COST}\n"
    #     f"HST Rate: {HST_RATE}\n"
    #     f"Processing Fee: {PROCESSING_FEE}\n")