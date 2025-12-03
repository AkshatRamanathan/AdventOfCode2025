with open('file.txt') as f:
# with open('test.txt') as f:
    banks = f.readlines()
    ans=0
    for bank in banks:
        batteries = list(map(int,bank.strip()))
        m = max(batteries[:-1])
        mi = batteries[:-1].index(m)
        ans += (m*10)+max(batteries[mi+1:])
print(ans)


