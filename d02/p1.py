ranges = open("file.txt").readlines()[0].split(",")
ranges = [(int(r.split('-')[0]),int(r.split('-')[1])) for r in ranges]
# print(len(ranges))
# print(ranges)
for r in ranges:
    pass
