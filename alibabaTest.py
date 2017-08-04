N,P,M,T = 8,2,5,1#3,2,5,1#3,2,4,2#2,1,4,1

count = 0
dis = T-P
addNum = M

ary = []

#DFS
def testFunc(nowP,addNum,subNum):
	if nowP - 1 >= 1 and subNum > 0:
		ary.append(-1)
		testFunc(nowP-1,addNum,subNum-1)
	if nowP + 1 <= N and addNum > 0:
		ary.append(1)
		testFunc(nowP+1,addNum-1,subNum)
	ary.append('T')
		
while(addNum >= 0):
	temp = addNum
	for i in range(0,(M-addNum)):
		temp -= 1
	if dis == temp :
		testFunc(P,addNum,M-addNum)
		print ary
	addNum -= 1

index = 0
oldIndex = 0
newAry = []
while index < len(ary):
	if ary[index] == 'T':
		newAry.append(ary[oldIndex:index])
		count += 1
		while index < len(ary) and ary[index] == 'T':
			index += 1
		oldIndex = index
		continue
	index += 1

print count
print newAry
tempItem = []
for index in range(0,len(newAry)):
	item = newAry[index]
	itemL = len(item)
	if itemL == M:
		tempItem = item
	if itemL < M:
		newAry[index] = tempItem[0:M-itemL]+item
print newAry
