import math
def main():
    print("-Hypotenuse Calculator-")
    l1= float(input("Enter the length of the first leg of your triangle:\n"))
    l2= float(input("Enter the length of the second leg of your triangle:\n"))
    hypo= math.sqrt((pow(l1,2)+pow(l2,2)))
    print(f"\nThe hypotenuse of your triangle is {hypo:.3f}")
if __name__ == '__main__':
    main()
