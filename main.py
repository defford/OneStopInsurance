# Add in needed libraries
import datetime
import json
import sys
import time
from functions import PPrint, FirstNextMonth, WaitSave, ProgressBar, SaveToFileBar

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

# Pull Customer Data in as a list and 
with open("CustData.dat", "r") as cdr:
    cdrContent = cdr.read()

cdrList = cdrContent.split(", ")

firstName = cdrList[0]

curDate = datetime.datetime.now()
curDateDsp = curDate.strftime("%Y-%m-%d")
firstPaymentDate = FirstNextMonth(curDate)

menu = ["Add New Policy", "Generate Policy Report", "Exit"]
provinces = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
PayOptions = ["Full", "Monthly"]
prevClaims = []

customerData = []

while True:    
    
    print()
    PPrint(60, ("+", "left"), (f"{'-' * 58}", "center"), ("+", "right"))
    PPrint(60, ("|", "left"), ("ONE STOP INSURANCE COMPANY", "center"), ("|", "right"))
    PPrint(60, ("+", "left"), (f"{'-' * 58}", "center"), ("+", "right"))
    print()
    print("Please choose from the following 3 options:")
    print()
    print("1. Create a new policy and generate report")
    print("2. Generate a policy report from an existing customer")
    print("3. Exit")
    print()

    menuOption = int(input("Please choose an option (1, 2, or 3): "))

    if menuOption == 3:
        print()
        PPrint(60, ("Thank You For Choosing One Stop Insurance!", "center"))
        time.sleep(1)
        break
    elif menuOption == 2:
        polId = int(input("Please enter the policy number of the customer you want to generate a report for (or type SHOW to see a list of customers): "))

        if polId == "SHOW":
            PPrint(60, (f"{'-' * 60}", "center"))
            print()

            for id in customerData:
                print()
        else:
            print("Please enter a valid option.")

    elif menuOption == 1:

        while True:
            print()
            print()
            welcomeMessage = "Initiating Policy Entry System."
            seconds = 10
            for dot in range(1, seconds + 1):
                sys.stdout.write('\r' + welcomeMessage)
                sys.stdout.flush()

                time.sleep(0.2)
                welcomeMessage += "."
                if len(welcomeMessage) > 32:
                    welcomeMessage = "Initiating Policy Entry System"

            time.sleep(1)
            print()    
            print()

            time.sleep(1)
            PPrint(60, ("Please enter customer information below", "center"))
            time.sleep(1)
            print()
            firstName = input("Enter customer's first name: ").lower().title()
            lastName = input("Enter customer's last name: ").lower().title()    
            address = input("Enter customer's address: ").lower().title()
            city = input("Enter customer's city: ").lower().title()

            while True:
                province = input("Enter customer's province (XX): ").upper()
                if province in provinces:
                    break
                else:
                    print("Please enter a valid province.")

            postalCode = input("Enter customer's postal code (X0X 0X0): ").upper()
            phoneNum = input("Enter customer's phone number (000-000-0000): ")
            numCars = int(input("How many cars are being added to insurance?: "))
            carCoverageDetails = []

            print()
            print(f"Entering car coverage information...")            
            time.sleep(1)

            
            while True:
                for carNum in range(1, numCars + 1):
                    print()
                    print(f"Now entering information for car {carNum}/{numCars}...")
                    time.sleep(1)
                    print()
                    while True:
                        extraLiability = input(f"Does this car need extra Liability (Y/N)? ").upper()
                        if extraLiability == "Y" or extraLiability == "N":
                            break
                        else:
                            print("Please enter a valid option.")
                    
                    while True:
                        glassCoverage = input(f"Does this car need glass coverage (Y/N)?: ").upper()
                        if glassCoverage == "Y" or glassCoverage == "N":
                            break
                        else:
                            print("Please enter a valid option.")
                    
                    while True:
                        loanerCar = input(f"Does this car need loaner car coverage (Y/N)?: ").upper()
                        if loanerCar == "Y" or loanerCar == "N":
                            break
                        else:
                            print("Please enter a valid option.")  
                    
                    print()
                    print("Saving...")

                    carCoverageDetails.append((POLICY_NUM, carNum, extraLiability, glassCoverage, loanerCar))
                    time.sleep(1)

                print()
                PPrint(60, ("Extra", 12), ("Glass", 30), ("Loaner Car", 50))
                PPrint(60, ("Car #", "left"), ("Liability", 12), ("Coverage", 30), ("Coverage", 50))
                print("-" * 60)

                for carNum in range(1, numCars + 1):
                    PPrint(60, (f"{carNum}", 2), (f"{extraLiability}", 15), (f"{glassCoverage}", 33), (f"{loanerCar}", 54))
                print("-" * 60)

                continueCoverage = input("Please confirm vehicle coverage details (Y/N): ").upper()

                if continueCoverage not in ["Y", "N"]:
                    print("Please enter a valid option.")
                elif continueCoverage == "Y":
                    print()
                    SaveToFileBar(carCoverageDetails, "CarCoverageDetails.dat", filePathAlias="ccd")
                    time.sleep(1)
                    print()
                    break
                elif "N":
                    carCoverageDetails = []

                

            while True:
                payOption = input(f"How would the customer like to pay (Full or Monthly)?: ").lower().title()
                downPayment = int(input("Enter down payment amount (Enter 0 if no down payment): "))
                if payOption in PayOptions:
                    break
                else:
                    print("Please enter a valid option.")



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
            

            print()
            PPrint(60, ("Now entering previous claim information...", "center"))
            time.sleep(1)
            print()

            while True:
                prevClaim = []
                claimNum = int(input(f"Enter previous claim number: "))
                claimDate = input(f"Enter date for claim #{claimNum} (YYYY-MM-DD): ")
                claimAmt = float(input("Enter the claim amount: "))
                prevClaim.append([claimNum, claimDate, claimAmt])

                prevClaims.append(prevClaim)
                
                while True:
                    continuePrevClaims = input("Would you like to enter another claim (Y/N)?: ").upper()

                    if continuePrevClaims not in ["Y", "N"]:
                        print("Please enter a valid option")
                    else:
                        break

                if continuePrevClaims == "N":
                    print()
                    PPrint(46, (f"Previous claims", "center"))
                    PPrint(46, (f"{'-' * 18}", "center"))
                    PPrint(46, ("Claim #", "left"),("Claim Date", "center"),("Amount", 46, "right"))      
                    PPrint(46, ("-" * 46, "center"))  

                    for prevClaim in prevClaims:
                        for claimDetails in prevClaim:    
                            PPrint(46, (f"{claimDetails[0]}", 5, "right"),(f"{claimDetails[1]}", "center"),(f"${claimDetails[2]:,.2f}", 46, "right"))

                    print()

                    while True:
                        confirmPrevClaims = input("Confirm previous claims entry (Y/N)?: ").upper()
                        if confirmPrevClaims == "Y":
                            print()
                            SaveToFileBar(prevClaims, "PrevClaims.dat", filePathAlias="ccd")
                            break
                        elif confirmPrevClaims == "N":
                            prevClaims = []
                            break
                        else:
                            print("Please enter a valid option.")
                    
                break
            
            # Add Loading Bar Here
            customerData.append([POLICY_NUM, firstName, lastName, address, city, province, postalCode, phoneNum, numCars, carCoverageDetails, payOption, downPayment])
            
            with open("CustData.dat", "a") as cdw:
                cdw.write(f"{customerData}\n")

            continueScript = input("Do you want to add another policy (Y/N)?: ").upper()
            
            if continueScript == "N":
                break
        #     elif continueScript == "Y":


# Display all output values into a nicely formatted receipt

    print()
    PPrint(60, ("+", "left"), (f"{'-' * 58}", "center"), ("+", "right"))
    PPrint(60, ("|", "left"), ("ONE STOP INSURANCE COMPANY", "center"), ("|", "right"))
    PPrint(60, ("+", "left"), (f"{'-' * 58}", "center"), ("+", "right"))
    print()
    PPrint(60, ("CUSTOMER DETAILS", "center"))
    print()
    PPrint(60, (f"Policy #: {POLICY_NUM}", "left"), (f"Date: {curDateDsp}", "right"))
    print()
    PPrint(60, (f"{firstName} {lastName}", "left"), (f"{address}", "right"))
    PPrint(60, (f"{phoneNum}", "left"), (f"{city}, {province}  {postalCode}", "right"))
    print()
    print()
    PPrint(60, (f"POLICY COVERAGE DETAILS", "center"))
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
    PPrint(60, (f"PAYMENT DETAILS", "center"))
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
    PPrint(60, ("-" * 60, "center")) 
    print()
    returnToMenu = input("Would you like to return to the main menu or exit the program (Y/Exit)?: ").title()

    if returnToMenu not in ["Y", "Exit"]:
        print("Please choose a valid option.")
    elif returnToMenu == "Exit":
        print()
        print("Have a Great Day!")
        break




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

