s = "yassh"
count = 0
target = input()

for ch in s:
    if target == ch:
        count +=1
        
print(f"taget={target} have count = {count}")