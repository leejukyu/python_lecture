# 짝수 찾기
even_list = []
for i in range(11):
    if (i %2==1):
        continue
    even_list.append(i)
print(even_list)

even_list = []
for i in range(11):
    if (i %2==0):
        even_list.append(i)
print(even_list)