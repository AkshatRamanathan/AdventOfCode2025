fresh=0
with open("file.txt") as f:
# with open("test.txt") as f:
    freshRanges,available = f.read().split('\n\n')
    freshRanges = [list(map(int,x.split('-'))) for x in freshRanges.split('\n')]
    available = [int(x) for x in available.split('\n') if x] #if x hack coz maybe last line empty?
    for id in available:
        for start,end in freshRanges:
            if id>=start and id<=end:
                fresh+=1
                break
print(fresh)

#WORKED FIRST TRY!!!! -> 782