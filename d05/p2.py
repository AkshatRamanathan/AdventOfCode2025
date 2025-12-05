ans=0
with open("file.txt") as f:
# with open("test.txt") as f:
    freshRanges = f.read().split('\n\n')[0] #only first half for ranges
    freshRanges = [list(map(int,x.split('-'))) for x in freshRanges.split('\n')] #map into ints
    freshRanges.sort() #sort on first val in tuple
    merged = [freshRanges[0]] #array to keep merged ranges
    for item in freshRanges[1:]: #loop over items and merge
        prev_x,prev_y=merged[-1]
        curr_x,curr_y=item
        if curr_x<=prev_y+1: #if overlap
            merged[-1]=(prev_x,max(prev_y,curr_y)) #edit latest item in merge list with new inclusive vals
        else:
            merged.append(item) #if no overlap, add
# print(merged)
for start,end in merged:
    ans+=(end-start)+1 #count inclusive of both limits for fresh items
print(ans)
#WORKED -> 353863745078671!!!