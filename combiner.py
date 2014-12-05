global new

def add(file):
    f = open(file+".txt")
    for line in f:
        if line not in new:
            new.append(line)
    print(len(new))
    f.close()
new = []
files = ["try1","try2","try3"]
for i in files:
    add(i)

f = open("combined"+str(len(new))+".txt", "w")
for i in new:
    f.write(i)
f.close()
