
# 987654321111111 -> 987654321111 
# 811111111111119 -> 811111111119 
# 234234234234278 -> 434234234278 
# 818181911112111 -> 888911112111 
# 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.

# DONE!!!!!! my answer -> 172162399742349

with open('file.txt') as f:
# with open('test.txt') as f:
    banks = f.readlines()
    ans=0
    for bank in banks:
        jolts=""
        start = 0
        offset = -11 # ensure 11 pending to be added worst case
        batteries = list(map(int,bank.strip()))
        while start<len(batteries)+offset and offset<0:
            # python makes copy hence can assign to temo vars and find index coz wrong
            # hence manually enumerate start->offset and find big val with its index wrt to start
            maxVal = float('-Inf')
            maxIndex = -1
            for i,x in enumerate(batteries[start:offset]):
                if x>maxVal:
                    maxVal=x
                    maxIndex=start+i
            jolts+=str(maxVal) #add to jolts
            start=maxIndex+1 #push start
            offset+=1 #reduce offset
        jolts+=str(max(batteries[start:]))  # add pending max guy from batteries[start:offset]
        # print(jolts)
        ans+=int(jolts)

print(ans)