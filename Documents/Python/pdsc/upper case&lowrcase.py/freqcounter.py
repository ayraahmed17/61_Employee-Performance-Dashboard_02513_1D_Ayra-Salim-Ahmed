s = "yaash"
max_count = 0
max_char =""

for i in s: 
    count = 0
    for j in s:
        if j == i:
            count +=1
            
            
if count>max_count:
    max_count = count
    max_char = i
    
print("The element with miost freq= ", max_char)
        
