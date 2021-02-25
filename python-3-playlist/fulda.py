def  CheckFuldaCharacter(input):
    strLen = len(input)
    arr =[False]*256

    for i in input:
        arr[ord(i)] =True

    selectedChar = ["f", "u", "l", "d", "a"]

    for sc in selectedChar:
        val = ord(sc)
        if (arr[val]):
            continue
        else:
            return False

    return True


def CheckSubstringFulda(input):
    substr = 'fulda'
    check = substr in input
    return check


def CheckFulda(strInput):
    res1 = CheckFuldaCharacter(strInput)
    res2 = CheckSubstringFulda(strInput)
    result = 0

    if(res1 and res2):
        result = 2
    elif(res1 and not(res2)):
        result = 1
    else:
        result = 0

    print(result)


CheckFulda('somefxuxdxlxamm')
CheckFulda('someOtherValue')
CheckFulda('xyfuldaping')
CheckFulda('somefxuxdxlxammfuldav')


# print(CheckFuldaCharacter('somefxuxdxlxamm'))
#print(CheckFuldaCharacter('someOtherValue'))
#print(CheckFuldaCharacter('xyfuldaping'))
#print(CheckFuldaCharacter('somefxuxdxlxammfuldav'))

#print(CheckSubstringFulda('somefxuxdxlxamm'))
#print(CheckSubstringFulda('someOtherValue'))
#print(CheckSubstringFulda('xyfuldaping'))
#print(CheckSubstringFulda('somefxuxdxlxammfuldav'))
