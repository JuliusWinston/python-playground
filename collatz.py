# A simple script to generate the collatz sequence for a given # integer
#==============================================================

# defining collatz function
def collatz(number):
    if(number % 2 == 0):
        return number // 2
    else:
        return number * 3 + 1


print('Enter the number')

# Handle input error
try:
    number = int(input())
except(ValueError):
    print('Enter a valid number: ')
    number = int(input())

# A keep calling collatz till return value is 1
while(True):
    print(number)
    if(number != 1):
        number = collatz(number)
    else:
        break

