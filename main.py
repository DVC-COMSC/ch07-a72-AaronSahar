num1 = list(map(int, input("Enter the numbers ").split()))
num2 = list(map(int, input("Enter the numbers ").split()))
match = False
for i in range (len(num2)):
    for j in range (len(num1)):
        if num2[i] == num1[j]:
            match = True
            break
        else:
            match = False
    if match == False:
        print(match)
if match == True:
    print(match)