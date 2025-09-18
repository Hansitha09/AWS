import math
def main():
    print("-Square Right Pyramid Calculator-")
    h= float(input("Enter the height: "))
    b= float(input("Enter the base: "))
    vol= ((math.pow(b,2)*h)/3)
    slHeight= (b**2/4+h**2)**.5
    surArea= b**2+2*slHeight*b
    print("\nThe pyramid has a surface area of "+f"{surArea:.3f}"+" and a volume of "+f"{vol:.3f}")
if __name__ == '__main__':
    main()
