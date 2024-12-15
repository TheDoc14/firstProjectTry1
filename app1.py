def print_until_zero(x: int):
    while x>0:
        print(x)
        x=x-1
        if x>0:
            print('we gone less 1')

n=int(input('Enter a number: '))
print_until_zero(n)