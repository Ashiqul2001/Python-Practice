av = 6
x = int(input("How many candies you want? "))
i=1
while i<=x:
    if i>av:
        print('Out of stock')
        break
    print('Candy')
    i+=1

print("No more")

'''for i in range(5):
    if i==3:
        break
    print("Hello",i)'''
