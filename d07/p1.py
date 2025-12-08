
ans = 0
beamTracking = set()
with open("file.txt") as f:
# with open("test.txt") as f:
    beams = [line.strip() for line in f.readlines()]
beamTracking.add(beams[0].find('S'))
for row in beams[1:]:
    for i in range(len(row)):
        if row[i]=='^' and i in beamTracking:
            beamTracking.remove(i)
            beamTracking.add(i-1)
            beamTracking.add(i+1)
            ans+=1


print(ans)
