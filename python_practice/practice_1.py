print 'input a number'
num = input()
for i in range(num):
    for j in range(num):
        if j > i:
            print '*'
        else:
            print' '
