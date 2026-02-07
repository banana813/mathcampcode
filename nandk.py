#actually this is just for n = 2; Q5. not super helpful, but did help me realize how 2 is impossible
digits = []
n = int(input("N: "))
k = int(input("K: "))
for i in range(n):
    digits.append(0)

def increaseDigit(place):
    if(digits[place]<k-1):
        digits[place]+=1
    elif(digits[place] == k-1):
        digits[place] = 0

for i in range(k):
    for i in range(k-1):
        print(digits[0], digits[1])
        increaseDigit(1)
    increaseDigit(0)
    print(digits[0], digits[1])