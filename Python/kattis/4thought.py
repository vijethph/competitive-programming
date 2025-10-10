# https://open.kattis.com/problems/4thought

test_cases = int(input())

ops = ['+', '-', '*', '/']

poss = {}

for i in range(len(ops)):
    for j in range(len(ops)):
        for k in range(len(ops)):
            curop1 = ops[i]
            curop2 = ops[j]
            curop3 = ops[k]
            
            strda = f"4 {curop1} 4 {curop2} 4 {curop3} 4"
            strdb = strda.replace("/","//")
            
            ps = int(eval(strdb))
            poss[ps] = strda + f" = {int(ps)}"


for tst in range(test_cases):
    num = int(input())
    
    if num > 256:
        print("no solution")
    elif num in poss.keys():
        print(poss[num])
    else:
        print("no solution")
