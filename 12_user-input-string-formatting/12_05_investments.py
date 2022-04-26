# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

    
principal = float(input(f"Enter Investment Amount:\n    "))
rate = float(input(f"Enter Interest Rate:\n    "))
years_compounded = int(input(f"Enter Number of Years to Invest:\n    "))
roi = (principal * rate) * years_compounded

print(f"If you invest ${principal:.2f} at a rate of %{rate:.2f}, compounded yearly for {years_compounded} years,\nthen you will realize a return of ${roi:.2f}")
