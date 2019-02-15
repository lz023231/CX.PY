import time
musicLrc = '''
输入需要的歌词和歌词第一个字出现的时间
[00:20:60]演唱：王菲


'''
lrcDict = {}
musicLrclist = musicLrc.splitlines()
for lrcLine in musicLrclist:
    lrcLinelist = lrcLine.split("]")
    for index in range(len(lrcLinelist) - 1):
        timeStr = lrcLinelist[index][1:]
        timeList = timeStr.split(":")
        time1 = float(timeList[0] * 60) + float(timeList[1])
        lrcDict[time1] = lrcLinelist[-1]
allTimeList = []
for t in lrcDict:
    allTimeList.append(t)
allTimeList.sort()
getTime = 0
while 1:
    for n in range(len(allTimeList)):
        tempTime = allTimeList[n]
        if getTime < tempTime:
            break
    lrc = lrcDict.get(allTimeList[n - 1])
    if lrc == None:
        pass
    else:
        print(lrc)
    time.sleep(1)
    getTime += 1
