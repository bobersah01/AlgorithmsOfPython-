#25-01-2023 | UDEMY PYTHON ALGORITHM COURSES
#SORTING ALGORITHM:
"""emptyList = list()
name = str(input("Please enter your name: "))
print("Welcome Our Bubble Sort Algorithm: {}\nIf you want to exit press q, otherwise go ahead!".format(name))
while(True):
    addInteger = str(input("Please enter a number: "))
    if (addInteger == "q" or addInteger == "Q"):
        print("Exiting from the program.")
        break
    else:
        emptyList.append(int(addInteger))

totalList = [3,10,0,-5,11,7,9]
first = [3,0,-5,10,7,9,11]
second = [0,-5,3,7,9,10,11]
third = [-5,0,3,7,9,10,11] #algoritma burada sıralı hale geliyor ancak bubble sort algoritması, -5 değerini 0,3 ve 7 değerleriyle karşılaştırmaya devam ediyor çünkü for döngüsünde
                                    #karşılaştırma işlemi bitmedi ve algoritma, var olan sıralamanın bittiğini anlayamıyor. 


for i in range(len(emptyList)): #total karşılaştırma işlemi
    for j in range(len(emptyList)-1-i): #kaşılaştırılan eleman sayısı
        if (emptyList[j] > emptyList[j+1]):
            emptyList[j] , emptyList[j+1] = emptyList[j+1], emptyList[j]
            
            temp = emptyList[j]
            emptyList[j+1] = emptyList[j]
            emptyList[j] = temp
            
for index, element in enumerate(emptyList):
    print("Index: {} Element: {}".format(index,element))
"""



"""
#BUBBLE SORTING ALGORITHM
def bubbleSort(integerList):
    for i in range(len(integerList)): #total karşılaştırma işlemi
        for j in range(len(integerList)-1-i): #kaşılaştırılan eleman sayısı
            if (integerList[j] > integerList[j+1]):
                integerList[j] , integerList[j+1] = integerList[j+1], integerList[j]
    #return (integerList)

#SELECTION  SORTING
#emptyList = [3,10,0,-5,7,11,9]
def selectionSort(integerList):
    for i in range(len(integerList)):
        minimumIndex = i
        for j in range(i+1, len(integerList)):
            if (integerList[j] < integerList[minimumIndex]):
                minimumIndex = j
        integerList[i], integerList[minimumIndex] = integerList[minimumIndex], integerList[i]

    #return(integerList)

#emptyList = [1,8,4,9,15,-5,-3]
#INSERTION SORTING
def insertionSort(integerList):
    for i in range(1,len(integerList)):
        key = integerList[i]
        j = i-1

        while(key < integerList[j] and j >= 0):
            integerList[j+1] = integerList[j]
            j = j-1
        integerList[j+1] = key
    #return(integerList)

#MERGE SORTING ALGORITHM:
#DIVIDING
def merging(integerList): #This function only takes a list that will be converted into as left and right list.
    if (len(integerList) > 1): #1  den büyük olduğunda parçalayacağız.
        mid = len(integerList) // 2 #orta indeksi bulunacak.
        leftList = integerList[ :mid] #creating left list that goes until midpoint of the integerList.
        rightList = integerList[mid: ] #creating right list that goes until the end of the integerList.

        #bölünen diziyi de sonradan, tekrardan bölmek için fonksiyon içerisinde çağırmam gerekiyor.
        merging(leftList)
        merging(rightList)

        #oluşturduğum dizileri birleştirmek için ise ayrı bir fonksiyon oluşturuyorum.
        mergeSort(integerList, leftList, rightList) #aynı zamanda oluşturduğum fonksiyonu çağırıyorum.

#FORMING
def mergeSort(integerList, leftList,rightList):
    i = 0 #left right indeksini tutar
    j = 0 #right left indeksini tutar.
    k = 0 #birlesik indeksin değerini tutar.

    while ((i < len(leftList)) and (j < len(rightList))): #i ve j listelerinin uzunluğundan küçük  olduğu sürece devam eder.

        if (leftList[i] < rightList[j]):
            integerList[k] = leftList[i]
            i = i+1 #i yi bir arttırıyorum ki leftListte sağa doğru geçeyim.

        else:
            integerList[k] = rightList[j]
            j = j+1

        k = k+1 #her seferinde aynı değere, değerlerin  atanmamasıiçin k değerini 1 arttıyorum.

    while (i < len(leftList)):
        integerList[k] = leftList[i]
        i = i+1
        k = k+1

    while (j < len(rightList)): #Amacı, solda veya sağda tek bir eleman kaldığında kontrol eder ve dizinin k nın elemanını o listedeki değere eşitler.
        integerList[k] = rightList[j]
        j = j+1
        k = k+1

    #return(integerList)
#integerList = [10,20,-5,6,3,2,55,7,11,13]
#merging(integerList)


#working hours of algorithms:
from random import seed
from random import randint
import time
seed(1) #seed kütüphanesini kullanmak için versiyonunu belirtmemiz gerekecektir.
#Her bir algoritma için ayrı ayrı olacak biçimde arrange,rearrange ve random olacak şekilde çalıştırıcaz ve çalışma sürelerine bakacağız.
def createArrange(amount): #sıralı dizi oluşturuyoruz. 0 dan amount değerine kadar.
    emptyList = list()
    for i in range(amount):
        emptyList.append(i)
    return emptyList

def createRearrange(amount): #tersten dizi oluşturuyoruz. Yani amountdan 0 a kadar.
    emptyList = list()
    for i in range(amount):
        emptyList.append(amount - i)
    return emptyList

def createRandom(amount):
    emptyList = list()
    for i in range(amount):
        emptyList.append(randint(0, amount)) #o la amount arasındaki sayı değeri arasında randomsayı oluşturarak, amount kadar listemde, random sayı oluşur.
    return emptyList

operationList = createRearrange(100) #Eğer aynı listeyi 4 farklı fonksiyon için kullanırsam sıralı listeler üzerinden işlem yapabilirler. Dolayısıyla
                                                        #listenin sabit kalmasını istiyorum ve aynısını oluşturmuş oluyorum aslında.
bubbleOperationList = operationList[ : ] #yukarıdaki işlemin kopyasını almamak için yani referansını almamak için bu işlemi yapıyorum.
selectionOperationList = operationList[ : ]
insertionOperationList = operationList[ : ]
mergeOperationList = operationList[ : ]

bubbleStarting = int(round(time.time() * 1000)) #ms cinsinden değer görmek istediğim için 1000 ile çarpıyorum.
bubbleSort(bubbleOperationList)
bubbleFinishing = int(round(time.time())*1000)
print("Bubble Working Hour: {}".format(str(bubbleFinishing - bubbleStarting)))

selectionStarting =  int(round(time.time() * 1000))
selectionSort(selectionOperationList)
selectionFinishing =  int(round(time.time() * 1000))
print("Selection Working Hour: {}".format(str(bubbleFinishing - bubbleStarting)))

insertionStarting =  int(round(time.time() * 1000))
insertionSort(insertionOperationList)
insertionFinishing =  int(round(time.time() * 1000))
print("Insertion Working Hour: {}".format(str(insertionFinishing - insertionStarting)))

mergeStarting =  int(round(time.time() * 1000))
merging(mergeOperationList)
mergeFinishing =  int(round(time.time() * 1000))
print("Merge Working Hour: {}".format(str(bubbleFinishing - bubbleStarting)))
"""
#QUICK SORT:
#quick sort uygulaması için baktığımızda, öncelikle diziyi pivottan  önce ve pivottan sonra olmak üzere iki parçaya ayırmak için parçalara ayırma fonksiyonu kullanıyoruz.
"""def divideFunction(integerList, leftIndex, rightIndex):
    i = leftIndex - 1
    pivot = integerList[rightIndex]

    for j in range(leftIndex, rightIndex): #j dizi üzerinde sürekli dolanacak.
        if (integerList[j] <= pivot):
            i += 1
            integerList[i], integerList[j] = integerList[j], integerList[i]

    integerList[i+1], integerList[rightIndex] = integerList[rightIndex], integerList[i+1]
    return i+1 #İndeksi dönüyorum.

def quickSort(integerList, leftIndex, rightIndex): #Dizinin solunda ve sağında olmak üzere iki ayrı parça olacağı için onun için bu partı yapıyoruz.
                                                                        #Üstte diziyi parçaladık ve bu durumda da parçaladığımız sol ve sağ kısım içerisinde yer değiştirme yapıyoruz.
                                                                        #Recursive function.
    if (leftIndex < rightIndex):
        pivot = divideFunction(integerList, leftIndex, rightIndex)
        quickSort(integerList, leftIndex, pivot-1) #Parçaladığımız bölümün solundaki kısmı pivota kadar sıralıyoruz.
        quickSort(integerList, pivot+1, rightIndex) #Parçaladığımız bölümün  pivotunun bir sağından  itibaren en sağ indekse kadar sıralama yapılır.

integerList = [1,5,4,8,13,5,182,2]
print("Complex list: {} ".format(integerList))
quickSort(integerList, 0, len(integerList)-1)
print("Arranged List: {}".format(integerList))"""

"""Python kodunu oluşturuken yine 2 aşamada yapıyoruz. Öncelikle max heap yapısını belirlemek için bir fomnksiyon oluşturuyoruz.
İkinci olarak ise oluşturulan maax heap yapısının listeye eklenmesini gerçekleştiriyoruz. Ancak bunu yaparken listenin en  sonundaki eleman max oluyor ve onu listeye ekliyoruz.
Aynı zamanda listenin en sonundan en başına çektiğimiz elamanı  kontrol etmek için ise bir işlem uygulamak durumundayız."""

"""def maxHeapify(integerList, sizeOf, rootIndex): #parametre olarak boyut almasının  sebebi, listedeki eleman sayısının 1 azalacağıdır. RootIndex: her zaman kontrol edilen işlem.
    leftIndex = (rootIndex*2)+1
    rightIndex = (rootIndex*2)+2
    maxIndex = rootIndex #İlk aşama olarak maximum index root index olarak kabul edilir.

    if (leftIndex < sizeOf and integerList[rootIndex] < integerList[leftIndex]): #Soldaki element roottan büyük olduğunda maximum element soldaki element olarak yer değiştirir.
        maxIndex = leftIndex
    if (rightIndex < sizeOf and integerList[maxIndex] < integerList[rightIndex]): #Sağdaki element maximum elementten büyük olduğunda, maximum elementi sağdaki element olarak yeniler.
        maxIndex = rightIndex

    if (maxIndex != rootIndex): #Kontrol işlemi yapılıyor.
        integerList[rootIndex], integerList[maxIndex] = integerList[maxIndex],  integerList[rootIndex]
        maxHeapify(integerList, sizeOf, maxIndex) #Recursive işlem olarak kendini yenileyecek.

#Şimdi ise en büyükten en küçüğe sıraladığımız ağacı, listemize ekleyelim. Maximum elementi en sona alarak, onları en sona yerleştiririz. Sonra da diğer elementi en  başa alırız.
def heapSort(integerList): #parametre olarak sadece listeyi alacak çünkü boyut her seferinde listenin 1 eksiği kadar uzayacak.
    for i in range(len(integerList), -1,-1): #listenin uzunluğundan  -1. elemente kadar gidecek 1 er azalarak. En sondan sıralıyorum çünkü listenin sonundan itibaren gidicem.
        maxHeapify(integerList,len(integerList), i)

    for i in range(len(integerList)-1, -1,-1): #listenin  uzunluğunun 1 eksiği kadar bu  sefer başlicam  çünkü en  sondaki  element gidiceği için  liste 1 azalacak.
        integerList[i], integerList[0] = integerList[0], integerList[i] #listenin en başındaki  değer  ile her seferinde azalıcak olan i değeriyle yer değiştirmem gerekiyor.
        maxHeapify(integerList, i, 0)

integerList = [1,5,2,9,15,7,3,86,45,12,56]
print("Complex List: {}".format(integerList))
heapSort(integerList)
print("Arranged List: {}".format(integerList))"""

#SEARCHING ALGORITHMS:
#LINEAR SEARCH ALGORITHM:
"""emptyList = list()
def listAppend(emptyList):
    userName = str(input("Please enter your name: "))
    print("Welcome our program {}!".format(userName))
    while (True):
        userInteger = str(input("Please enter a number {}: ".format(userName)))
        if userInteger == "q" or userInteger == "Q":
            print("You will not add any integer to the list.")
            break
        else:
            emptyList.append(int(userInteger))
    return emptyList
def searchingAlgorithm(numberFind):
    listAppend(emptyList)
    for i in range(0, len(emptyList)):
        if (emptyList[i] == numberFind):
            print("Your number was found in {}. index".format(i))
            break
searchingAlgorithm(16)"""

"""def binarySearch(integerList, leftIndex, rightIndex, numberFound):
    if (leftIndex <= rightIndex):
        midpoint = (leftIndex + rightIndex) // 2
        if (integerList[midpoint] == numberFound):
            return midpoint
        elif (numberFound < integerList[midpoint]):
            return binarySearch(integerList, leftIndex, midpoint - 1, numberFound) #RECURSIVE FUNCTION
        elif (numberFound > integerList[midpoint]):
            return binarySearch(integerList, midpoint + 1, rightIndex, numberFound) #RECURSIVE FUNCTION
    else:
        return  -1 #yani aranan numara bulunamadı, dolayısıyla liste içerisinde değil.
integerList = [15,11,30,41,10,75]
element = binarySearch(integerList,0,len(integerList) - 1, 41)
if element == -1:
    print("Your number was not found!")
else:
    print("Your number was found in {}. index".format(element))
#Eğer bu  işlem sıralı listede uygulanırsa olur diğer türlü hata verir."""

#JUMP SEARCH:
"""import math
def jumpSearch(integerList, numberFound):
    stepSize = int(math.sqrt(len(integerList)))
    prev = 0
    while (integerList[min(stepSize, len(integerList)-1)] < numberFound):
        prev = stepSize
        stepSize += stepSize
        if (prev > len(integerList)): #zaten dosyanın uzunluğunu  geçtiği için -1 döndürüyor.
            return -1
    while (integerList[prev] < numberFound):
        prev += 1
        if (integerList[min(prev, len(integerList))] > numberFound): #Linear search yapması gereken kısım aslında burası.
            return -1
    if (integerList[prev] == numberFound):
        return prev
    return -1
integerList = [1,5,8,78,80,94]
element = (jumpSearch(integerList, 78)) #return değeri olduğu için, print etmemiz gerekiyor (zaten yukarda return değeri döndürülmüş ancak print etmemiz gerekiyor)
print("Your number found in {}.index".format(element))"""

"""graph = {"A": ["B","C"], "B":["A","C","E","D"], "C": ["A","B","E"] ,"D": ["B","E","F"], "E": ["B","D","F"]}
roadsFromNodes = list()
for node, edgeList in graph.items():
    print("Node of {}, goes\n".format(node))
    for edge in edgeList:
        print(edge, " ")
        roadsFromNodes.append("{} - {}".format(node,edge))

print("Roads from the nodes can be written as like this: \n{}".format(roadsFromNodes))"""

"""graph = {"A": ["B","C"], "B":["A","C","E","D"], "C": ["A","B","E"] ,"D": ["B","E","F"], "E": ["B","D","F"]}
def findRoad(start, target, road = []):
    road += [start]

    if (start == target):
        return road

    for side in graph[start]:
        if side not in road:
            newRoad = findRoad(side, target, road)
            if (newRoad != None):
                return newRoad
    return None
element = findRoad("C", "D")
print("List of going target: {}".format(element))"""