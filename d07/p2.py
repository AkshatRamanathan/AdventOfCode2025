ans = 0
with open("file.txt") as f:
# with open("test.txt") as f:
    beams = [line.strip() for line in f.readlines()] #get tachyon beams
timelines = [0]*len(beams[0]) #create timelines
timelines[beams[0].find('S')]=1 #starting timeline (origin)
for row in beams[1:]:
    for i in range(len(row)):
        # if split in timeline, adjacent timelines gets the current value added and current one resets (consumed by ^)
        if row[i]=="^" and timelines[i]>0: 
            timelines[i-1]+=timelines[i]
            timelines[i+1]+=timelines[i] #clutch move
            timelines[i]=0

print(sum(timelines))

#WORKED!!! HOLY SHIT NO DFS BFS, CRAZY PASCAL TRIANGLE thanks to -> https://www.reddit.com/r/adventofcode/comments/1pgbg8a/2025_day_7_part_2_visualization_for_the_sample/#lightbox
# for the hint and epiphany
# answer -> 221371496188107