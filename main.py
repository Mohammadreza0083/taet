print('Welcome to this program')

def Facto():
    num = int(input('Enter a valid number: '))
    factoriel = 1
    for number in range(1, num + 1):
        factoriel = number * factoriel
    print(factoriel)

def Fibo():
    for num in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]:
        print(num, end=" * ")

def Primary():
    adad = int(input('Enter valid number: '))
    if adad > 1:
        for num in range(2, int(adad**0.5) + 1):
            if adad % num == 0:
                print('this number is not prime.')
                break
        else:
            print('this number is prime.')
    else:
        print('this number is not prime.')

def Mltiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            result = i * j
            print(f"{result}\t", end="")
        print()

print('What do you want? Choose a number:')
print('1. Factorial')
print('2. Fibonacci')
print('3. Check Prime')
print('4. Multiplication table')
print('5.Exit')

List_number = int(input())
if List_number == 1:
    Facto()
elif List_number == 2:
    Fibo()
elif List_number == 3:
    Primary()
elif List_number == 4:
    Mltiplication_table()
elif List_number== 5:
    print('have a good day ... ');
else:
    print('enter a valid number');

print('hiiii')