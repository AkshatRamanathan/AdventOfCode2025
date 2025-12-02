# circular dial, 0-99
# dial starts at 50
# L10 -> spin 10 clicks left (40)
# The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.
# part1 pass, part2 left
# you're actually supposed to count the number of times any click causes the dial to point at 0, 
# regardless of whether it happens during a rotation or at the end of one.

dial = range(100)
s = len(dial)//2
sign = 1
ans1=0
file = open('file.txt')
lines = file.readlines()
file.close()
for step in lines:
    dir,clicks=step[0],int(step[1:])
    sign = -1 if dir=="L" else 1
    clicks*=sign
    s+=clicks
    s%=100
    if s==0:
        ans1+=1

print(ans1)
