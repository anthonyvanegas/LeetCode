valueList = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbolList = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
def integerToRomanHelper(num, result):
    if num == 0:
        return result
    for i in range(13):
        if num >= valueList[i]:
            result += symbolList[i]
            result = integerToRomanHelper(num - valueList[i], result)
            break
    return result

print(integerToRomanHelper(3, ""))