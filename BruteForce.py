import time
import string

maxattempts = 10000000 #max of retry
start       = time.time()
chars       = list(string.printable)[:30] #max password chars
base        = len(chars)
n           = 0
solved      = False
password    = input("Enter your password:")


print(chars)


def numberToBase(n, b):
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]



if password == '':
    print('Your password is empty')
    solved = True
    
elif password == chars[n]:
    print('Your password is ' + chars[n])
    solved = True
    
else:
    n = 1

if not solved:
    while n < maxattempts:
        lst = numberToBase(n, base)
        print(lst)
        word = ''
        for x in lst:
            word += str(chars[x])
        print(word)
        if password == word:
            solved = True
            print('-Stats-')
            print('Pass: ' + word)
            print('Attempts: ' + str(n))
            print('time: ' + str((time.time() - start)) + ' sec')
            break
        else:
            n += 1


if not solved:
    print('Unsolved after ' + str(n) + ' attempts!')