file = open("day5s.txt",'r')
total = 0
status = 0
first_l = False
seeds = []
stos = None
stof = None
ftow = None
wtol = None
ltot = None
ttoh = None
htol = None

class Node:
    def __init__(self, key, key1, start):
        self.key = key
        self.key1 = key1
        self.start = start
        self.left = None
        self.right = None

def insert(node, key, key1, start):
    if node is None:
        return Node(key, key1, start)
    if key < node.key:
        node.left = insert(node.left, key, key1, start)
    elif key > node.key:
        node.right = insert(node.right, key, key1, start)
    return node
 
def search(root, key):
    if root is None or root.key <= key <= root.key1:
        return root
 
    if root.key < key:
        return search(root.right, key)
    
    return search(root.left, key)

def out(p: str)->list:
    return p

for line in file:
    if line.startswith("\n"):
        status=0
    if line.startswith("seeds: "):
        seeds = list(map(int,line.lstrip("seeds: ").rstrip().split(' ')))
    elif line.startswith("seed-to-soil map:") or status == 1:
        if status==1:
            ss = list(map(int, line.rstrip().split(' ')))
            if first_l:
                stos = insert(stos, ss[1], ss[1]+ss[2]-1, ss[0])
                first_l = False
            else:
                insert(stos, ss[1], ss[1]+ss[2]-1, ss[0])
            #stos[range(ss[1],ss[1]+ss[2]-1)] = ss
        else:
            first_l = True
            status = 1
    elif line.startswith("soil-to-fertilizer map:") or status == 2:
        if status==2:
            ss = list(map(int, line.rstrip().split(' ')))
            if first_l:
                stof = insert(stof, ss[1], ss[1]+ss[2]-1, ss[0])
                first_l = False
            else:
                insert(stof, ss[1], ss[1]+ss[2]-1, ss[0])
        else:
            first_l = True
            status = 2
    elif line.startswith("fertilizer-to-water map:") or status == 3:
        if status==3:
            ss = list(map(int, line.rstrip().split(' ')))
            if first_l:
                ftow = insert(ftow, ss[1], ss[1]+ss[2]-1, ss[0])
                first_l = False
            else:
                insert(ftow, ss[1], ss[1]+ss[2]-1, ss[0])
        else:
            first_l = True
            status = 3
    elif line.startswith("water-to-light map:") or status == 4:
        if status==4:
            ss = list(map(int, line.rstrip().split(' ')))
            if first_l:
                wtol = insert(wtol, ss[1], ss[1]+ss[2]-1, ss[0])
                first_l = False
            else:
                insert(wtol, ss[1], ss[1]+ss[2]-1, ss[0])
        else:
            first_l = True
            status = 4
    elif line.startswith("light-to-temperature map:") or status == 5:
        if status==5:
            ss = list(map(int, line.rstrip().split(' ')))
            if first_l:
                ltot = insert(ltot, ss[1], ss[1]+ss[2]-1, ss[0])
                first_l = False
            else:
                insert(ltot, ss[1], ss[1]+ss[2]-1, ss[0])
        else:
            first_l = True
            status = 5  
    elif line.startswith("temperature-to-humidity map:") or status == 6:
        if status==6:
            ss = list(map(int, line.rstrip().split(' ')))
            if first_l:
                ttoh = insert(ttoh, ss[1], ss[1]+ss[2]-1, ss[0])
                first_l = False
            else:
                insert(ttoh, ss[1], ss[1]+ss[2]-1, ss[0])
        else:
            first_l = True
            status = 6  
    elif line.startswith("humidity-to-location map:") or status == 7:
        if status==7:
            ss = list(map(int, line.rstrip().split(' ')))
            if first_l:
                htol = insert(htol, ss[1], ss[1]+ss[2]-1, ss[0])
                first_l = False
            else:
                insert(htol, ss[1], ss[1]+ss[2]-1, ss[0])
        else:
            first_l = True
            status = 7    


print(stos.start)
    
#print(out())
seeds = []
for i in range(79, 93):
    seeds.append(i)
for i in range(55, 68):
    seeds.append(i)
temp = []
for seed in seeds:
    x = search(stos, seed)
    if x is None:
        temp.append(seed)
    else:
        nn = (seed - x.key) + x.start
        temp.append(nn)
print(temp)
seeds = []
seeds = temp
temp = []
for seed in seeds:
    x = search(stof, seed)
    if x is None:
        temp.append(seed)
    else:
        nn = (seed - x.key) + x.start
        temp.append(nn)
print(temp)
seeds = []
seeds = temp
temp = []
for seed in seeds:
    x = search(ftow, seed)
    if x is None:
        temp.append(seed)
    else:
        nn = (seed - x.key) + x.start
        temp.append(nn)
print(temp)
seeds = []
seeds = temp
temp = []
for seed in seeds:
    x = search(wtol, seed)
    if x is None:
        temp.append(seed)
    else:
        nn = (seed - x.key) + x.start
        temp.append(nn)
print(temp)
seeds = []
seeds = temp
temp = []
for seed in seeds:
    x = search(ltot, seed)
    if x is None:
        temp.append(seed)
    else:
        nn = (seed - x.key) + x.start
        temp.append(nn)
print(temp)
seeds = []
seeds = temp
temp = []
for seed in seeds:
    x = search(ttoh, seed)
    if x is None:
        temp.append(seed)
    else:
        nn = (seed - x.key) + x.start
        temp.append(nn)
print(temp)
seeds = []
seeds = temp
temp = []
for seed in seeds:
    x = search(htol, seed)
    if x is None:
        temp.append(seed)
    else:
        nn = (seed - x.key) + x.start
        temp.append(nn)
print(temp)
print(sorted(temp)[0])


