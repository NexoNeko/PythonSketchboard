def collatz(number):
""" Calculates the collatz sequence of a given number """
    while (True):
        if number <= 1:
            break;
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(str(number))

print('Enter number:')
collatz(int(input()))
