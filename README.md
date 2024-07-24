# One Stop Insurance Program

## Overview

The One Stop Insurance program is designed to assist The One Stop Insurance Company in entering and calculating new insurance policy information for customers. The program is interactive and allows the user to input various customer details, calculate insurance premiums, and generate a well-designed receipt. The user can input multiple customers and process their insurance details in a loop.

## Features

- Input customer information including name, address, city, province, postal code, phone number, and number of cars being insured.
- Options for extra liability coverage, glass coverage, and loaner car coverage.
- Payment options including Full, Monthly, and Down Payment.
- Calculation of insurance premiums based on basic rates and selected options.
- Display of all input and calculated values in a formatted receipt.
- Storage of previous claims for each customer.
- Progress bar or blinking message indicating the policy data has been saved.
- Incremental policy number for each new policy.

## Default Values

The following default values are read from a file called `Const.dat`:

- Next policy number: 1944
- Basic premium: $869.00
- Additional car discount: 25%
- Extra liability cost: $130.00 per car
- Glass coverage cost: $86.00 per car
- Loaner car cost: $58.00 per car
- HST rate: 15%
- Processing fee for monthly payments: $39.99

## Requirements

- Python 3.x
- A `Const.dat` file containing the default values.
- The `functions.py` file containing the necessary functions for the program.

## Input Validation

- Valid provinces: AB, BC, MB, NB, NL, NS, NT, NU, ON, PE, QC, SK, YT
- Valid payment options: Full, Monthly, Down Pay
- Extra liability, glass coverage, and loaner car options: Y or N

## Functions

The program includes at least three functions, including a new function added to the `functions.py` library. One of the functions returns multiple values.

## Calculations

- Basic premium for the first car: $869.00
- Additional cars: 25% discount on the basic premium
- Extra costs for each car based on selected options (liability, glass, loaner car)
- Total insurance premium: sum of basic premium and extra costs
- HST: 15% of the total insurance premium
- Total cost: total insurance premium plus HST
- Monthly payment: total cost divided by 8 plus a processing fee of $39.99
- If a down payment is made, the monthly payment is calculated based on the remaining amount after the down payment.

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Create a `Const.dat` file with the default values separated by commas.
3. Place the `functions.py` file in the same directory as your main script.
4. Run the main script.
5. Follow the prompts to enter customer details and insurance options.
6. Review the formatted receipt and previous claims.
7. Confirm the information to save the policy data.
