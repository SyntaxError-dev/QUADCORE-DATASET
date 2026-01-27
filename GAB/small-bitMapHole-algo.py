count = 0
def BitmapHoles(strArr):
    newList = []
    
    def horizontalCount(ourList):  
        global count
        for each in ourList:
            z = list(each)
            index = 0
            while index < len(z)-1:
                if z[index] == '0' and z[index+1] == '0':
                    count += 1
                    break
                index +=1

    def transpose():
        newStr = ""
        i = 0
        while i < len(strArr[0]):
            for each in strArr:
                newStr += each[i]
            # print(newStr)
            newList.append(newStr)
            newStr = ""
            i += 1


    horizontalCount(strArr)
    transpose()
    horizontalCount(newList)
    return count

print(BitmapHoles(["01111", "01101", "00011", "11110"]))
