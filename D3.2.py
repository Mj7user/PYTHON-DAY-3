first=int(input("Enter first number :"))
second=int(input("Enter second number :"))
third=int(input("Enter third number :"))
List=[]
List.append(first)
List.append(second)
List.append(third)
for i in range(3):
    for j in range(3):
        for k in range(3):
            if (i != j and j != k and i != k):
                print(List[i], List[j], List[k])
