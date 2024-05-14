num = 10
for i in range(2,num):
    if num % i == 0:
        print("It's not Prime")
        break
else:
    print("Prime")