
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



# ANOTHER SOLUTION WITH ROHIT
# PART 1 SAME AS PART 2 WITH NO + IN REGEX -> '^(\d+)\1$'
# didnt work for me coz no ^ and $
# ^ is begin matcher and $ is end matcher
# PART 2->
# import re
# pattern = re.compile(r'^(\d+)\1+$') #only add + rest same
# key = 0
# for x in ranges:
#     l=int(x[0])
#     u=int(x[1])
#     for i in range(l,u+1):
#        if pattern.search(str(i)):
#            # print(i)
#            key+=i
# print(key)