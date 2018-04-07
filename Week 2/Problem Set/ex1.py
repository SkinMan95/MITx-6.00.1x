balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

months = 12
actualBalance = 0
previousBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
for i in range(months):
    monthlyUnpaidBalance = (1.0 - monthlyPaymentRate) * previousBalance
    actualBalance = (1.0 + monthlyInterestRate) * monthlyUnpaidBalance
    previousBalance = actualBalance
    # print(("%.2f" % actualBalance).strip("0"))

print(("%.2f" % previousBalance).strip("0"))
