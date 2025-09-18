def main():
    print("-Mortgage Calculator-")
    hc= float(input("Enter house cost:\n"))
    dp= float(input("Enter down payment:\n"))
    t= int(input("Enter number of years on the loan:\n"))
    ir= float(input("Enter annual interest rate (Value should be less that 1):\n"))
    mon= t*12
    monIn= ir/12
    padp= hc-dp
    mp=  (monIn*padp*(1+monIn)**mon)/((1+monIn)**mon-1)
    print("\nBuying a house with a cost of $"+ f"{hc:,.2f}"+" over "+str(t) +" years at an interest rate of $"+f"{ir*100:.2f}"+"% with a down payment of $"+f"{dp:,.2f}"+" would have a total cost of $"+f"{mp*mon+dp:,.2f}"+" with a monthly payment of $"+f"{mp:,.2f}"+".")
if __name__ == '__main__':
    main()
