from math import ceil
def main():
    print("-Profit Calculator-")
    oq= int(input("Order quantity: "))
    cpi= float(input("Cost per item: "))
    cs= int(input("Case size: "))
    scpc= float(input("Shipping Cost per case: "))
    tp= int(input("Tariff percentage: "))
    sp= float(input("Sale price: "))
    cases= ceil(oq/cs)
    sc= cases*scpc
    cost= (oq*cpi)*(tp/100)+(oq*cpi)+sc
    profit= (oq*sp)-cost
    print("\nThe acquisition cost of these items is $"+f"{cost:.2f}"+" with an estimated profit of $"+f"{profit:.2f}"+" once sold.")
if __name__ == '__main__':
    main()
