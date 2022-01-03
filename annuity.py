initialAmount = int(input("Enter the loan amount: "))
time = float(input("How many years will you pay for the loan: "))
intRate = float(input("What is the interest rate? : "))

def pVAnnuity(initialAmount, time, intRate):
    intRate = intRate / 100
    noOfPay = time * 12
    intRate =   intRate / 12
    n = 1 + intRate
    month = (initialAmount * intRate) / (1 - (n ** (noOfPay * -1)))
    #return month
    i = str(round(month, 2))
    print("you will pay R" + i + " a month")

    totalAmount = month * noOfPay
    s = str(round(totalAmount, 2))
    print("The loan will cost you " + s + " in total")

pVAnnuity(initialAmount, time, intRate)
#print(pVAnnuity(initialAmount, time, intRate))
degvd
