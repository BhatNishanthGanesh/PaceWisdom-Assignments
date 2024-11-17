# 19. From a list containing ints, strings and floats, make three lists to store them separately

list=[]
n = int(input("Enter n"))
for _ in range(n):
    list.append(eval(input()))

int =[]
string = []
float= []

for value in list:
    if type(value)==int:
        int.append(value)
    elif type(value)==str:
        string.append(value)
    elif type(value)==float:
        float.append(value) 

print(int)
print(string)
print(float)               