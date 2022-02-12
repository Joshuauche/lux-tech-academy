

def fib():
    number = int(input("enter your number here... "))
    fib_list = []
    num1, num2 = 0, 1
    # check_number = int(input(number))
    count = 0

    # check for negative number
    if number < 0:
        print("Incorrect input")
    elif number == 0:
        print('0')
    else:

        while count < 40:
            fib_list.append(num1)
            num3 = num1 + num2
            # updating the fib sequence
            num1 = num2
            num2 = num3
            count +=1
        print(fib_list)
        if number in fib_list:
            print("True")
        else:
            print("False")

if __name__ == "__main__":
    fib()