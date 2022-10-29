import copy

stringByNumber = {2: "a,b,c", 3: "d,e,f", 4: "g,h,i", 5: "j,k,l", 6: "m,n,o", 7: "p,q,r,s", 8: "t,u,v", 9: "w,x,y,z"}


def letterCombinations(digits):
    if digits == "":
        return []
    if len(digits) == 1:
        return stringByNumber[int(digits[0])].split(",")
    return letterCombinationHelper(digits, "", [], 0)


def letterCombinationHelper(digits, subscript, solution, pointer):
    if len(digits) == len(subscript):
        solution.append(copy.copy(subscript))
        return solution
    for i in range(pointer, len(digits)):
        temp = stringByNumber[int(digits[i])].split(",")
        pointer = i + 1
        for j in range(len(temp)):
            subscript += temp[j]
            letterCombinationHelper(digits, subscript, solution, pointer)
            subscript = subscript[:-1]
    return solution


print(letterCombinations("234"))
