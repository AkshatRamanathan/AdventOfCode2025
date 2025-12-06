
# CRAZY BULLSHITTERY!!!
# LOGIC -> 
# loop a feeder from the rightmost column and consume each column
# if empty ignore (whitespace seperators)
# if last value in feeder is an operation (+ or *) then reduce the temp array based on that operation 
# and reset the temp array
# add reduced value to answer
# if normal number, add it to a temp list

# WORKS -> 10189959087258

from functools import reduce

ans = 0
# with open("test.txt") as f:
with open("file.txt") as f:
    vals = f.readlines()
vals = [row.rstrip("\n") for row in vals]
rows = len(vals)
cols = len(vals[0])
nums=[]
for c in range(cols-1,-1,-1):
    feed=""
    for r in range(rows):
       feed+=vals[r][c]
    if len(feed.strip())>0:
        if feed[-1]=='+':
            nums.append(int(feed[:-1]))
            ans+=reduce(lambda x,y: x+y,nums)
            nums = []
        elif feed[-1]=="*":
            nums.append(int(feed[:-1]))
            ans+=reduce(lambda x,y: x*y,nums)
            nums = []
        else:
            nums.append(int(feed))
print(ans)