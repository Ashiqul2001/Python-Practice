'''for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()'''

'''for i in range(4):
    for j in range(i+1):
        print("# ", end="")
    print()'''


'''for i in range(4):
    for j in range(4-i):
        print("# ", end="")
    print()'''

'''Left half pyramid'''
'''for i in range(int(input("Enter number of rows: "))):
    for j in range(i+1):
        print("# ",end='')
    print()'''

'''down left pattern'''
'''row = (int(input("Enter number of rows: ")))
for i in range(row):
    for j in range(row-i):
        print("# ", end="")
    print()'''

'''Right half Pyramid'''
'''for i in range(5):
    for j in range(i,5):
        print(" ", end="")
    for j in range(i+1):
        print("#", end="")
    print()'''

'''Down Right half Pyramid'''
'''row = int(input("Type your Number: "))
for i in range (row):
    for j in range(i):
        print(" ",end="")
    for j in range(row-i):
        print("#", end="")
    print()'''

'''Pyramid'''
'''for i in range(5):
    for j in range(5-i):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    for j in range(i):
        print("*", end="")
    print()'''

'''Down Pyramid'''
row=int(input("Enter your number: "))
for i in range(row):
    for j in range(i):
        print(" ", end="")
    for j in range(row-i):
        print("*", end="")
    for j in range(row-1-i):
        print("#", end="")
    print()

