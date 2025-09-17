def main():
    print("-Time-")
    fullmin=int(input("Enter total minutes: "))
    hours=int(fullmin/60)
    min= fullmin-hours*60
    print("\nThe time is "+str(hours)+" hours and "+str(min)+" minutes.")
if __name__ == '__main__':
    main()