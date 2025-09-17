from math import ceil
def main():
    print("-Pizza Order-")
    adults= int(input("How many adults?"))
    adSli = int(input(" How many slices will an adult eat?"))
    children = int(input(" How many children?"))
    chiSli = int(input(" How many slice will a child eat? "))
    piz= ((adults*adSli) + (children*chiSli))/12
    pizza=ceil(piz)
    print("\nYou need to order "+str(int(pizza))+" pizzas.")
if __name__ == '__main__':
    main()