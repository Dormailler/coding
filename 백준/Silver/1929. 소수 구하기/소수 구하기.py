minn,max = map(int,input().split())
for i in range(minn,max+1):
    if i ==1:
        continue
    for j in range(2,int(i**0.5)+1):       
        if i%j == 0 and i != j:
            break
    else:
        print(i)
