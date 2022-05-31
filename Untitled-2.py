n = int(input())
k = n
m = 1
a = 1
for i in range (n):
    while m < k:
        print (" ", end="")
        m+=1

    if i == 0:
        print("*" *a)
    else:
        a+=2
        print("*" *a)

    k-=1
    m= 1
