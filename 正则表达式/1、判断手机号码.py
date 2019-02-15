import re

'''
给你一串字符串，判断这是否是手机号码

'''
def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] != "1":
        return False
    elif str[1:3] != "30" and str[1:3] != "31":
        return False
    for i in range(3,11):
        if str[i] < "0" or str[i] > "9":
            return False
    return True

def checkPhone2(str):
    pat = r"^1(([3578]\d)|(47))\d{8}$"
    res = re.match(pat,str)
    return res

print(checkPhone2("13083738873"))
print(checkPhone2("134837388a73"))
pat = r"^1(([3578]\d)|(47))\d{8}$"



