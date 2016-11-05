def add(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum = sum + number
    return sum


def average(list_of_numbers):
    result = add(list_of_numbers) / len(list_of_numbers)
    return int(result)


def main():
    list_of_numbers = [int(input("Enter a number: ")) for num in range(5)]

    result = average(list_of_numbers)
    print("Average equal {}".format(result))

main()