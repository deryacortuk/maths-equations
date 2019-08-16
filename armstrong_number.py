number = input("number:")
digit_number = len(number)
number = int(number)
digit = 0
result = 0

momentary_number = number

while (momentary_number > 0):
    digit = momentary_number % 10

    result += digit ** digit_number

    momentary_number //= 10

if (result == number):
    print("{} is an armstrong number".format(number))

else:
    print("{} is not an armstrong number".format(number))