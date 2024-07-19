# Add in needed libraries
import datetime
from functions import PPrint, FirstNextMonth

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
curDateDsp = curDate.strftime("%Y-%m-%d")

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
    carCoverageDetails = []

    for carNum in range(1, numCars + 1):
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
        
        carCoverageDetails.append((carNum, extraLiability, glassCoverage))

    print(carCoverageDetails)

    while True:
        loanerCar = "Y" # input(f"Does {firstName} need a loaner (Y/N)?: ").upper()
        if loanerCar == "Y" or loanerCar == "N":
            break
        else:
            print("Please enter a valid option.")            

    while True:
        payOption = "Monthly" # input(f"How would firstName like to pay (Full or Monthly)?: ").lower().title()
        downPayment = 500 # int(input("Enter firstName's down payment amount (Enter 0 if no down payment): "))
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

    premiumCost = BASIC_PREM + BASIC_PREM * (1 - ADD_CAR_DISCOUNT) * (numCars - 1)

    totalExtraCost = 0
    totalExtraCost += EXTRA_LIABILITY_COST * numCars if extraLiability == "Y" else 0
    totalExtraCost += GLASS_COST * numCars if glassCoverage == "Y" else 0
    totalExtraCost += LOANER_CAR_COST * numCars if loanerCar == "Y" else 0

    totalInsurancePremium = premiumCost + totalExtraCost

    hstCost = totalInsurancePremium * HST_RATE

    totalCost = totalInsurancePremium + hstCost

    if downPayment > totalCost:
        downPayment = float(input(f"Please enter a down payment less than ${totalCost:,.2f}: "))
    totalOwing = totalCost - downPayment

    monthlyPayment = (totalOwing + PROCESSING_FEE) / 8
    
    firstPaymentDate = FirstNextMonth(curDate)

    continueScript = input("Do you want to continue (Y/N)?: ").upper()
    if continueScript == "N":
        break


# Display all output values into a nicely formatted receipt

print()
PPrint(60, ("+", "left"), (f"{'-' * 58}", "center"), ("+", "right"))
PPrint(60, ("|", "left"), ("ONE STOP INSURANCE COMPANY", "center"), ("|", "right"))
PPrint(60, ("+", "left"), (f"{'-' * 58}", "center"), ("+", "right"))
print()
# PPrint(60, ("+", 17), ("-" * 24, "center"), ("+", 41))
PPrint(60, ("CUSTOMER DETAILS", "center"))
# PPrint(60, ("-" * 20, "center"))
print()
PPrint(60, (f"Policy #: {POLICY_NUM}", "left"), (f"Date: {curDateDsp}", "right"))
print()
PPrint(60, (f"{firstName} {lastName}", "left"), (f"{address}", "right"))
PPrint(60, (f"{phoneNum}", "left"), (f"{city}, {province}  {postalCode}", "right"))
print()
print()
# PPrint(60, ("+", 14), ("-" * 30, "center"), ("+", 45))
PPrint(60, (f"POLICY COVERAGE DETAILS", "center"))
# PPrint(60, ("+", 14), ("-" * 30, "center"), ("+", 45))
print()
print()
PPrint(60, ("Extra", 12), ("Glass", 30), ("Loaner Car", 50))
PPrint(60, ("Car #", "left"), ("Liability", 12), ("Coverage", 30), ("Coverage", 50))
print("-" * 60)

for carNum in range(1, numCars + 1):
    PPrint(60, (f"{carNum}", 2), (f"{extraLiability}", 15), (f"{glassCoverage}", 33), (f"{loanerCar}", 54))
print("-" * 60)

print()
print()
# PPrint(60, ("+", 14), ("-" * 30, "center"), ("+", 45))
PPrint(60, (f"PAYMENT DETAILS", "center"))
# PPrint(60, ("+", 14), ("-" * 30, "center"), ("+", 45))
print()
print()
PPrint(60, (f"Premium for {numCars} vehicles:", "left"), (f"${premiumCost:,.2f}", "right"))
PPrint(60, (f"Extra coverage costs:", "left"), (f"${totalExtraCost:,.2f}", "right"))
PPrint(60, (f"{'-' * 25}", "left"), (f"{'-' * 10}", "right"))
PPrint(60, ("Subtotal:", "left"), (f"${totalInsurancePremium:,.2f}", "right"))
PPrint(60, ("HST:", "left"), (f"${hstCost:,.2f}", "right"))
PPrint(60, (f"{'-' * 25}", "left"), (f"{'-' * 10}", "right"))
PPrint(60, ("Total:", "left"), (f"${totalCost:,.2f}", "right"))
print()
PPrint(60, (f"Payment Option:", "left"), (f"{payOption}", "right"))
PPrint(60, (f"Down payment:", "left"), (f"-${downPayment:,.2f}", "right"))

PPrint(60, (f"{'-' * 25}", "left"), (f"{'-' * 10}", "right"))
PPrint(60, ("Total Owing:", "left"), (f"${totalOwing:,.2f}", "right"))
if payOption == "Monthly":
    PPrint(60, ("Processing Fee:", "left"), (f"${PROCESSING_FEE:,.2f}", "right"))
    print()
    PPrint(60, ("Monthly Payment:", "left"), (f"${monthlyPayment:,.2f}", "right"))
    PPrint(60, ("First Payment Due:", "left"), (f"{firstPaymentDate.date()}", "right"))
print("-" * 60)
print()
PPrint(60, (f"PREVIOUS CLAIMS" , "center"))
print()
PPrint(60, ("Claim #", "left"),("Claim Date", "center"),("Amount", 60, "right"))      
PPrint(60, ("-" * 60, "center"))  

for prevClaim in prevClaims:
    for claimDetails in prevClaim:    
        PPrint(60, (f"{claimDetails[0]}", 5, "right"),(f"{claimDetails[1]}", "center"),(f"${claimDetails[2]:,.2f}", 60, "right"))

print("-" * 60)
print()
PPrint(60, ("Thank You For Choosing One Stop Insurance!", "center"))
print()
print()


# Payment Method
# Down Deposit
# HST
# Total Premium
# Total Extra Costs
# Total Insurance Prem
# HST
# Total Cost
# (If Monthly) Monthly Payment
# (If Full) Payment Owed
# Pay method = Monthly, so show 

