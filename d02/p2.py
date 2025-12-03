
ranges = open("file.txt").read().split(",")
ranges = [ r.split("-") for r in ranges]
ans=0
for start,end in ranges: 
    for num in range(int(start),int(end)+1):
        s = str(num)
        if (s+s).index(s,1)<len(s):
            ans+=num
        
print(ans)    

# we dont need to find substring that makes larger string. ab from ababab isnt needed, we only need to check if repeating
# pattern exits to consider invalid ID and add to ans for this use case
# logic -> double the input => ababab becomes abababababab (ab 6 times). inside this, starting at index 1 (b) 
# find ababab (original string). if we find the index > or = to len(ababab) it means its pointing to second replica
# and there is no repetition in first half. but if found in first hlaf means we found our repeating pattern which is invalid
# hence (s+s).index(s,1)<len(s) from https://algo.monster/liteproblems/459
# SOLVED!!!