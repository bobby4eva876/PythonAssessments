def getEven():
    list_of_numbers = []
    no_of_even_numbers = 0

    while no_of_even_numbers < 5:
        num = int(input("Enter even number: "))
        if num % 2 == 0:
            list_of_numbers.append(num)
            no_of_even_numbers = no_of_even_numbers + 1

    return list_of_numbers


def main():
    sum = 0
    for number in getEven():
        sum = sum + number
    print("The total of even numbers is {}".format(sum))

main()