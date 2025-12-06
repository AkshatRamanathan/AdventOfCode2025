ans=0
with open('file.txt') as f:
# with open('test.txt') as f:
    lines = f.readlines()
    values,operations = lines[:-1],lines[-1] #split em
    values = [list(map(int,x.strip().split())) for x in values] #convert
    operations = [x for x in operations.split()] #cleanup
    l = len(values[0]) #columns
    for i in range(l): #column wise looping
        o = operations[i] 
        temp = 0 if o=='+' else 1 #set based on operation
        for j in range(len(values)): #rows
            if o=='+':
                temp+=values[j][i] #column values
            else:
                temp*=values[j][i]
        ans+=int(temp) #accumulate
print(ans)