# 13. Take 10 integers from keyboard using loop and print their average value on the screen.

sum=0
for _ in range(10):
    sum+=int(input())
print(sum/10)    