# https://open.kattis.com/problems/sortofsort

n = int(input())

res = [int(x) for x in input().split()]

resd = []
currele = res[0]
resd.append(currele)

for i in range(1, n):
    if currele > res[i]:
        continue
    
    currele = res[i]
    resd.append(currele)
    
            
print(*resd)