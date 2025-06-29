name  = 'Paramjeet'
vowels = 'aeiouAEIOU'
count = 0
consonant = 0

for i in name:
    if(i in vowels):
        count +=1
    else:
        consonant +=1
print(count)
print(consonant)
        

    

print('Upper case: ', name.lower())