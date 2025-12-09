from math import prod,dist

# with open("test.txt") as f:
with open("file.txt") as f:
    junctions = [tuple(map(int,l.strip().split(','))) for l in f.readlines()] #get and transform data into (x,y,z) tuples
    distances=[]
    n=len(junctions)
    # starting at each point, calc distance from itself to the remaining ones and save into array as (distance,{x,y})
    # x and y are the points indexes relative to main data 
    for i in range(n-1):
        for j in range(i+1,n):
            d = dist(junctions[i],junctions[j])
            distances.append((d,{i,j}))

    flip = 10 if False else 1000 #for example/real
    
    circuits=[] #start circuit generation
    #sort the distances based on distance
    for _,connection in sorted(distances)[:flip]: #for every pair of indexes
        overlapIndexes=[] #check if there is overlap 
        for i,crt in enumerate(circuits): #for every preexisting circuit 
            if crt & connection: #if common elements in both sets add to overlap array
                overlapIndexes.append(i)
        
        if not overlapIndexes: #if no overlap consider new circuit
            circuits.append(connection)
        elif len(overlapIndexes)==1: #if only 1 overlap merge both sets with boolean OR
            circuits[overlapIndexes[0]] |= connection
        else:
            circuits[overlapIndexes[0]] |= circuits.pop(overlapIndexes[1]) #fallback for all cases, merge into first occurance
            # this is done so second is deleted with pop() and merged into first with boolean OR 
            # even if more than 2, each iteration will handle same first occurance and merge others into itself

    # map all circuits to their lengths and reverse sort it. only need biggst 3's products
    print(prod(sorted(map(len,circuits),reverse=True)[:3]))



# #WORKED->
# THIS is black magic. thanks -> https://github.com/mgtezak/Advent_of_Code/blob/master/2025/08/p2.py
# logic defined in comments (easier there)

# other way to do it is disjoint set or union find but
# im yet to learn that shit
# pure black magic wtf