"""
original 12345
p0 >> p1 21345 d
p0 >> p2 31245 c
p0 >> p1 13245 d
p0 >> p2 23145 c
p0 >> p1 32145 d
p0 >> p3 42135 b
p0 >> p1 24135 d
p0 >> p2 14235 c
p0 >> p1 41235 d
p0 >> p2 21435 c
p0 >> p1 12435 d
p0 >> p3 32415 b
p0 >> p1 23415 d
p0 >> p2 43215 c
p0 >> p1 34215 d
p0 >> p2 24315 c
p0 >> p1 42315...
"""
import time
def heap(num, i, c, found):
    num[0],num[i] = num[i],num[0]
    if num[0] != "0":
        new = ''.join(num)
        if int(new)%11 == 0 and new not in found:
            c += 1
            found.append(new)
            print(new,"\t",c)
    return c, found

def cont(num, count, found):
    for a in range(10):
        for b in range(9):
            for c in range(8):
                for d in range(7):
                    for e in range(6):
                        for f in range(5):
                            for g in range(4):
                                for h in range(3):
                                    for i in range(2):
                                        for j in range(1):
                                            count, found = heap(num, 0, count, found)
                                        count, found = heap(num, 1, count, found)
                                    count, found = heap(num, 2, count, found)
                                count, found = heap(num, 3, count, found)
                            count, found = heap(num, 4, count, found)
                        count, found = heap(num, 5, count, found)
                    count, found = heap(num, 6, count, found)
                count, found = heap(num, 7, count, found)
            count, found = heap(num, 8, count, found)
    return count, found, num

num = "10012233445566778899"
num = list(num)
count = 0
found = []
for a in range(21):
    for b in range(20):
        for c in range(19):
            for d in range(18):
                for e in range(17):
                    for f in range(16):
                        for g in range(15):
                            for h in range(14):
                                for i in range(13):
                                    for j in range(12):
                                        for k in range(11):
                                            count, found, num = cont(num,count,found)
                                            count, found = heap(num, 9, count, found)
                                        count, found = heap(num, 10, count, found)
                                    count, found = heap(num, 11, count, found)
                                count, found = heap(num, 12, count, found)
                            count, found = heap(num, 13, count, found)
                        count, found = heap(num, 14, count, found)
                    count, found = heap(num, 15, count, found)
                count, found = heap(num, 16, count, found)
            count, found = heap(num, 17, count, found)
        count, found = heap(num, 18, count, found)
