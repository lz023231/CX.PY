num = 23
print("guess how old the girl i am missing is")
bingo = False

while bingo == False:
    answer = int(input())
    if answer < num:
        print("too small")
    elif answer > num:
        print("too old")
    else:
        print("bingo")
        bingo = True