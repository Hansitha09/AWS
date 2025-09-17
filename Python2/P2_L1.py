def main():
    print(f"-ID Badge-")
    fname=input("Enter your first name:\n")
    lname = input("Enter your last name:\n")
    age = input("Enter your age:\n")
    iD = input("Enter your employee ID number:\n")
    dep = input("Enter your department:\n\n")
    print(f"{"Employee:"}{lname+", "+fname+" ("+age+")":>21}")
    print(f"{"Department:"}{dep:>19}")
    print(f"{"ID Number:"}{iD:>20}")
if __name__ == '__main__':
    main()
