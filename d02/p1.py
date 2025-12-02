# Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking 
# for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice),
#  6464 (64 twice), and 123123 (123 twice) would all be invalid IDs. 

# "1111" find middle, 11 and 11 then compare both if equal, invalid add to running sum 
# but multi loop needed????

ranges = open("file.txt").read().split(",")
ranges = [ tuple(r.split("-")) for r in ranges]
ans=0
for start,end in ranges: #values intentionally kept as strings for pattern finding
    for num in range(int(start),int(end)+1):
        temp = str(num)
        mid = len(temp)//2
        p1,p2=temp[:mid],temp[mid:]
        if(p1==p2):
            ans+=num
print(ans)    
