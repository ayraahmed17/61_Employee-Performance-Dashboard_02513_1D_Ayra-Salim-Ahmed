str1 = "python programming"

count = 0

vowels = "aeiouAEIOU"
for char in str1 :
    if char in vowels:
        count +=1
        
print("count of vowels=",count)



str1 = "python programming123"

v=d=s=0

for char in str1 :
    if char in "aeiouAEIOU" :
        v +=1
    elif char.isdigit():
        d +=1
    elif char == " ":
        s +=1
    
        
print(" Vowels=", v)
print(" Digit=", d)
print(" Space=", s)





