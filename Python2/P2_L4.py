def main():
    print("-Mixed Number Version 1-")
    num= int(input("Enter the numerator: "))
    den = int(input("Enter the denominator: "))
    whole= int(num/den)
    frac= num%den
    print("\n"+str(num)+"/"+str(den)+" as a mixed number is "+str(whole)+" "+str(frac)+"/"+str(den))
if __name__ == '__main__':
    main()