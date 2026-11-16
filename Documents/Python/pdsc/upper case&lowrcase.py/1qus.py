s = "HelloWorld"
u=0
l=0

for char in s:
    if char.isupper():
        u += 1
    elif char.islower():
        l +=1
        
print("Uppercase  = ",u)
print("Lowercase = ", l)