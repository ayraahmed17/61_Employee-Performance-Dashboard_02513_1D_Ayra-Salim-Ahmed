test = {}

test["name"] = "viki"
test["age"] = 25

print(test)



sq = {}
for i in range (1,6) :
    sq[i] = i**2
print(sq)



s = "banana"
freq = {}
for i in s :
    freq[i] = 0
    for j in s:
        if i == j :
            freq[i]=+1
        else:
            freq[i]=1
print(freq)
        


s = "educaton"
v= "aeiouAEIOU"
freq = {}

for i in s:
     freq[i] = 0
     for j in s:
        if i == j :
            freq[i]=+1
        else:
            freq[i]=1
print(freq)



