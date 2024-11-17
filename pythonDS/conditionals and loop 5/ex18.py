# 18. From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.

odd=[]
even=[]
prime=[]

for i in range(1,101):
    flag=0
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
    for j in range(2,(i//2)+1):
        if i%j==0:
            flag=1
            break   
    if flag==0:
        prime.append(i)

for num in even:
    if num%4==0 and num%6==0 and num%8==0 and num%10==0 and num%3==0 and num%5==0 and num%7==0 and num%9==0:
        print(num,end=",")

for num in odd:
    if num%4==0 and num%6==0 and num%8==0 and num%10==0 and num%3==0 and num%5==0 and num%7==0 and num%9==0:
        print(num,end=",")        