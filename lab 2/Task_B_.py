def bfSum(a,Alice,b,Bob):
    end1,right1= 0, a 
    end2,right2= 0, b
    idx= [] * (a+b)

    while end1<right1 and end2<right2:
        
        if Alice[end1]<Bob[end2]:
            idx.append(Alice[end1])
            end1+=1

        else:
            idx.append(Bob[end2])
            end2+=1

    while end1<right1:
        idx.append(Alice[end1])
        end1+=1

    while end2<right2:
        idx.append(Bob[end2])
        end2+=1


    print(str(idx)[1:-1].replace(",",""))

a=int(input())
Alice=list(map(int,input().split()))
b=int(input())
Bob=list(map(int,input().split()))
idx=bfSum(a,Alice,b,Bob)



