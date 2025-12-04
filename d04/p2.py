ans = 0
# grid is a square in both cases
with open("file.txt") as f:
# with open("test.txt") as f:
    dirs = {(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)}
    lines = f.readlines()
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    s = len(grid)
    for i in range(s):
        for j in range(s):
            if grid[i][j]=='.': continue
            neighbours=0
            for dx,dy in dirs:
                nx,ny=i+dx,j+dy
                if nx in range(s) and ny in range(s) and grid[nx][ny]=='@':
                    neighbours+=1
            if neighbours<4:
                ans+=1
            
    # print(type(grid))

print(ans)