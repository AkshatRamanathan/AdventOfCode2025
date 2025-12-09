# find 2 sets of points from input with sets x,y to form largest area possible
# rectangle area = l*b but inclusive of x1y1 and x2y2 

# Ultimately, the largest rectangle you can make in this example has area 50.
# One way to do this is between 2,5 and 11,1:
# ((11-2)+1) * ((5-1)+1) = 10*5 = 50 means area = (|y2-y1|+1)*(|x2-x1|+1) |abs| val

# with open("test.txt") as f:
with open("file.txt") as f:
    positions = [tuple(map(int,line.strip('\n').split(","))) for line in f.readlines()]
maxArea = 0
for x1,y1 in positions:
    for x2,y2 in positions:
        area = abs((x2-x1)+1)*abs((y2-y1)+1)
        maxArea=max(maxArea,area)
print(maxArea)
