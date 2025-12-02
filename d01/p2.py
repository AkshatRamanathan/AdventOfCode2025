# circular dial, 0-99
# dial starts at 50
# L10 -> spin 10 clicks left (40)
# The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.
# part1 pass, part2 left
# you're actually supposed to count the number of times any click causes the dial to point at 0, 
# regardless of whether it happens during a rotation or at the end of one.

f = open("file.txt")
turns = f.readlines()
ans=0
curr = 50
f.close()
for turn in turns:
    dir,steps=turn[0],int(turn[1:])
    if dir=="L":
        new = (curr-steps)%100
        if new > curr and curr!=0:
            ans+=1
    elif dir=="R":
        new = (curr+steps)%100
        if new < curr and new!=0:
            ans+=1
    curr = new
    if curr==0:
        ans+=1
    ans+=steps//100
    

print(ans)


# 50 -> R80 => 130 -> 30,1 30<50 means crossover +1zero
# 50 -> L80 => -30 -> 70,1 70>50 means crossover +1zero
