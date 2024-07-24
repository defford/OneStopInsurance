#  Title: Policy Entry Program for One Stop Insurance Company
#  Description: This program allows a One Stop employee to enter in new customer information (policy coverage, previous claims) and then display a receipt at the end
#  By: Daniel Efford
#  Date: Jul 18 - Jul 25

# Add in needed libraries
import datetime
import sys
import time
from functions import PPrint, FirstNextMonth, WaitSave, ProgressBar, SaveToFileBar, WaitingMessage

while True:

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
    firstPaymentDate = FirstNextMonth(curDate)

    provinces = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
    PayOptions = ["Full", "Monthly"]

    while True:    
        
        print()
        PPrint(60, ("+", "left"), (f"{'-' * 58}", "center"), ("+", "right"))
        PPrint(60, ("|", "left"), ("ONE STOP INSURANCE COMPANY", "center"), ("|", "right"))
        PPrint(60, ("+", "left"), (f"{'-' * 58}", "center"), ("+", "right"))

        while True:

            prevClaims = []
            carCoverageDetails = []
            customerData = []

            print()
            print()

            WaitingMessage("Initiating Policy Entry System", 12)

            print()
            print()
            PPrint(60, ("Please enter customer information below...", "center"))
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

            print()
            print(f"Entering car coverage information...")            
            time.sleep(1)
            print()
            
            while True:

                while True:

                    numCars = int(input("How many cars are being added to insurance?: "))
                    if numCars >= 1:
                        break
                    else:
                        print("At least 1 vehicle must be entered.")

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

                    carCoverageDetails.append([POLICY_NUM, carNum, extraLiability, glassCoverage, loanerCar])
                    time.sleep(1)

                print()
                PPrint(60, ("Please review the following coverage details...", 6))
                print()
                PPrint(60, ("Extra", 12), ("Glass", 30), ("Loaner Car", 50))
                PPrint(60, ("Car #", "left"), ("Liability", 12), ("Coverage", 30), ("Coverage", 50))
                print("-" * 60)

                for carNum in range(0, numCars):
                    PPrint(60, (f"{carCoverageDetails[carNum][1]}", 2), (f"{carCoverageDetails[carNum][2]}", 15), (f"{carCoverageDetails[carNum][3]}", 33), (f"{carCoverageDetails[carNum][4]}", 54))
                print("-" * 60)

                print()
                
                while True:

                    continueCoverage = input("Is this correct (Y/N)?: ").upper()

                    if continueCoverage not in ["Y", "N"]:
                        print("Please enter a valid option.")

                    break

                if continueCoverage == "Y":
                    print()
                    SaveToFileBar(carCoverageDetails, "CarCoverageDetails.dat", filePathAlias="ccd")
                    time.sleep(1)
                    print()
                    break
                elif "N":
                    carCoverageDetails = []

            while True:

                payOption = input(f"How would the customer like to pay (Full or Monthly)?: ").lower().title()
                if payOption in PayOptions:
                    break
                else:
                    print("Please enter a valid option.")
            
            downPayment = int(input("Enter down payment amount (Enter 0 if no down payment): "))
            print()


            # Perform calculations
            premiumCost = BASIC_PREM + BASIC_PREM * (1 - ADD_CAR_DISCOUNT) * (numCars - 1)

            totalExtraCost = 0

            for i in range(0, numCars):
                totalExtraCost += EXTRA_LIABILITY_COST if carCoverageDetails[i][2] == "Y" else 0
                totalExtraCost += GLASS_COST if carCoverageDetails[i][3] == "Y" else 0
                totalExtraCost += LOANER_CAR_COST if carCoverageDetails[i][4] == "Y" else 0

            totalInsurancePremium = premiumCost + totalExtraCost

            hstCost = totalInsurancePremium * HST_RATE

            totalCost = totalInsurancePremium + hstCost

            if downPayment > totalCost:
                downPayment = float(input(f"Please enter a down payment less than ${totalCost:,.2f}: "))

            totalOwing = totalCost - downPayment
            monthlyPayment = (totalOwing + PROCESSING_FEE) / 8      

            while True:

                prevClaimsOption = input(f"Would you like to enter previous claims information for {firstName} {lastName} (Y/N)?: ").upper()


                if prevClaimsOption == "N":
                    break
                elif prevClaimsOption == "Y":

                    print()
                    PPrint(60, ("Now entering previous claim information...", "center"))
                    time.sleep(1)
                    print()

                    prevClaim = []

                    while True:

                        claimNum = int(input(f"Enter previous claim number: "))
                        claimDate = input(f"Enter date for claim #{claimNum} (YYYY-MM-DD): ")
                        claimAmt = float(input("Enter the claim amount: "))
                        prevClaim.append([POLICY_NUM, claimNum, claimDate, claimAmt])

                        prevClaims.append(prevClaim)

                        print()

                        while True:

                            continuePrevClaims = input("Would you like to enter another claim (Y/N)?: ").upper()

                            if continuePrevClaims not in ["Y", "N"]:
                                print("Please enter a valid option")
                            elif continuePrevClaims == "Y":
                                print()
                                break
                            elif continuePrevClaims == "N":
                                print()
                                PPrint(46, ("Please review previous claims...", "center"))
                                print()
                                PPrint(46, (f"Previous claims", "center"))
                                PPrint(46, (f"{'-' * 18}", "center"))
                                PPrint(46, ("Claim #", "left"),("Claim Date", "center"),("Amount", 46, "right"))      
                                PPrint(46, ("-" * 46, "center"))  

                                for claimDetails in prevClaim:    
                                    PPrint(46, (f"{claimDetails[1]}", 5, "right"),(f"{claimDetails[2]}", "center"),(f"${claimDetails[3]:,.2f}", 46, "right"))

                                print()

                                while True:

                                    confirmPrevClaims = input("Confirm previous claims entry (Y/N)?: ").upper()

                                    if confirmPrevClaims == "Y":
                                        print()

                                        with open("PrevClaims.dat", "w") as pc:

                                            SaveToFileBar(prevClaim, "PrevClaims.dat", filePathAlias="pc")
                                            time.sleep(1)
                                            print()
                                            break

                                    elif confirmPrevClaims == "N":
                                        prevClaims = []
                                        break
                                    else:
                                        print("Please enter a valid option.")

                                break
                        
                        if continuePrevClaims == "Y":
                            continue
                        elif confirmPrevClaims == "Y":
                            break

                    break

                break
            
            # Add user input into customerData to eventually write it all back into a CustData.dat file
            customerData.append([POLICY_NUM, firstName, lastName, address, city, province, postalCode, phoneNum, numCars, payOption, downPayment])
            
            PPrint(60, ("Saving Policy To Database...", "center"))

            with open("CustData.dat", "w") as cd:
                print()
                SaveToFileBar(customerData, "CustData.dat", filePathAlias="cd")

            cd.close()


            # Display all output values into a nicely formatted receipt
            print()
            WaitingMessage(f"Generating Report for Policy # {POLICY_NUM} ({firstName} {lastName})", 6)            
            time.sleep(1.5)
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

            for i in range(0, numCars):
                PPrint(60, (f"{carCoverageDetails[i][1]}", 2), (f"{carCoverageDetails[i][2]}", 15), (f"{carCoverageDetails[i][3]}", 33), (f"{carCoverageDetails[i][4]}", 54))
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
                print("-" * 60)
                PPrint(60, ("Monthly Payment:", "left"), (f"${monthlyPayment:,.2f}", "right"))
                PPrint(60, ("First Payment Due:", "left"), (f"{firstPaymentDate.date()}", "right"))

            print("-" * 60)
            print()
            PPrint(60, (f"PREVIOUS CLAIMS" , "center"))
            print()

            if prevClaimsOption == "N":
                PPrint(60, ("No previous claims in file.", "center"))
            elif prevClaimsOption == "Y":
                PPrint(60, ("Claim #", "left"),("Claim Date", "center"),("Amount", 60, "right"))      
                PPrint(60, ("-" * 60, "center"))  

                for claimDetails in prevClaim:    
                    PPrint(60, (f"{claimDetails[1]}", 5, "right"),(f"{claimDetails[2]}", "center"),(f"${claimDetails[3]:,.2f}", 60, "right"))

                print("-" * 60)

            print()

            continueScript = input("Do you want to add another policy (Y/N)?: ").upper()
            
            if continueScript == "N":
                print()
                PPrint(60, ("Have a great day!", "center"))
                print()
                print()
                time.sleep(1)
                break
            elif continueScript == "Y":
                carCoverageDetails = []
                prevClaims = []
                customerData = []
                
                # Increment Policy number and write all constants back into const.dat
                POLICY_NUM += 1
                fList[0] = str(POLICY_NUM)            
                updatedContent = ",".join(fList)

                with open("Const.dat", "w") as f:
                    f.write(updatedContent)
                
                f.close()
        
        break
    
    break


