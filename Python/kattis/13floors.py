# https://open.kattis.com/problems/13floors

num = int(input())

if num == 13:
    num = 14
elif num > 13:
    num = num + 1

print(num)