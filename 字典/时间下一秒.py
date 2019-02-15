timeStr = input()
timelist = timeStr.split(":")
h = int(timelist[0])
m = int(timelist[1])
s = int(timelist[2])
s += 1
if s == 60:
    m += 1
    s = 0
    if m == 60:
        h += 1
        m = 0
        if h == 24:
            h = 0
print("%.2d:%.2d:%.2d" % (h, m, s))
