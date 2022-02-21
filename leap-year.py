
def check_leap_year():
    number = int(input("enter the number you wanna check: "))
    if number % 400 == 0 or number % 100 != 0 and  number % 4 == 0:
        print("the number you entered is a leap year")
    else:
        print("the number you entered isn't a leap year")


if __name__ == "__main__":
    check_leap_year()
