from math import prod,dist

# with open("test.txt") as f:
with open("file.txt") as f:
    junctions = [tuple(map(int,l.strip().split(','))) for l in f.readlines()]
    distances=[]
    n=len(junctions)
    for i in range(n-1):
        for j in range(i+1,n):
            d = dist(junctions[i],junctions[j])
            distances.append((d,{i,j}))
    circuits=[] 
    for _,connection in sorted(distances): 
        overlapIndexes=[] 
        for i,crt in enumerate(circuits): 
            if crt & connection: 
                overlapIndexes.append(i)
        
        if not overlapIndexes: 
            circuits.append(connection)
        elif len(overlapIndexes)==1:
            circuits[overlapIndexes[0]] |= connection
        else:
            circuits[overlapIndexes[0]] |= circuits.pop(overlapIndexes[1])
        if len(circuits[0])==n:
            i,j = connection
            print(junctions[i][0]*junctions[j][0])
            break

    # print(prod(sorted(map(len,circuits),reverse=True)[:3]))


# #WORKED->
# THIS is black magic. thanks -> https://github.com/mgtezak/Advent_of_Code/blob/master/2025/08/p1.py and p2.py
# logic same as part 1 only change in last line

# other way to do it is disjoint set or union find but
# im yet to learn that shit
# pure black magic wtf
# sorry i cheated again