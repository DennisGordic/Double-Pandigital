f = open("try3.txt")
num = []
for line in f:
    num.append(line.split()[0] + "\n")
f.close()

f = open("safety.txt", "w")
for i in num:
    f.write(i)
f.close()
