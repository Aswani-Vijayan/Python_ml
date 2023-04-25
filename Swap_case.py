# n = input("Enter the string :")
# m = n.swapcase()
# print(m)

#another method

k = ''
x = input("Enter the word : ")
for i in x:
    if i.islower():
        k += i.upper()
    else:
        k += i.lower()
print(k)
