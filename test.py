import random

def bozosort(list):
    bozolist = list
    while True:
        #Shuffla listan
        for i in range(len(bozolist)):
            bozoentry = list.pop(random.randint(0,(len(list)-1)))
            bozolist.append(bozoentry)
        #Kolla om listan är sorterad
        print(bozolist)
        for i in range(len(bozolist)):
            if i != len(bozolist)-1:
                if bozolist[i] > bozolist[i+1]:
                    break
        else:
            break
    return bozolist

testlista = [1,8,7,9,2,2,7, 31, 18, 102]
testlista = bozosort(testlista)
print(testlista)