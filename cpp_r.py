dict1 = {}
dict2 = {}
dict3 = {}
dict13 = {}
dict23 = {}
for line in open('cr1.txt').readlines():
	pure = line.replace('\n','').replace('\r','')
	key,value = pure.split('\t')
	dict1[key] = value

for line in open('cr2.txt').readlines():
	pure = line.replace('\n','').replace('\r','')
	key,value = pure.split('\t')
	dict2[key] = value

for line in open('cr3.txt').readlines():
	pure = line.replace('\n','').replace('\r','')
	key,value = pure.split('\t')
	dict3[key] = value

for key,key2 in dict1.items():
	key3 = dict2.get(key2)
	if key3:
		value = dict3.get(key3)
		if value:
			dict13['PlayerRole::'+key] = value
		else:
			print("ERROR in 2->3 : ",key3)
	else:
		print("ERROR in 1->2 : ",key2)
# for key,value
for key,key2 in dict2.items():
	value = dict3.get(key2)
	if value:
		dict23['TaskFactoryV2::Instance()->'+key] = value
	else:
		print("ERROR in 2->3 : ",key2)

for line in open('cdeps.txt'):
	if line.startswith('\t'):
		pure = line.replace(' ','').replace('\t','').replace('\n','').replace('\r','')
		if dict13.get(pure):
			print('\t',dict13.get(pure),sep='')
		elif dict23.get(pure):
			print('\t',dict23.get(pure),sep='')
		else:
			print(line,end='')
	else:
		print(line,end='')