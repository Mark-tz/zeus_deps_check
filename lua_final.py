print('digraph G {\n\trankdir=LR;')

s0 = set()
playName = "ERROR PLAY NAME!"
for line in open('lr0.txt').readlines():
	pure = line.replace('\n','').replace('\r','').replace(' ','')
	if pure.startswith('\t'):
		deps = '"task:'+pure.replace('\t','')+'"'
		key = playName+' -> '+deps
		if key not in s0:
			print('\t',key,sep='',end=';\n')
			s0.add(key)
	else:
		playName = '"play:'+pure+'"'
		print('subgraph cluster_0 { '+playName+'}')

s1 = set()
for line in open('lr1.txt').readlines():
	pure = line.replace('\n','').replace('\r','').replace(' ','')
	tv = pure.split('\t')
	task = '"task:'+tv[0]+'"'
	print('subgraph cluster_1 { '+task+'}')
	skill = '"skill:'+tv[1]+'"'
	key = task+' -> '+skill
	if key not in s1:
		print('\t',key,sep='',end=';\n')
		s1.add(key)

skillName = "ERROR SKILL NAME"
s2 = set()
for line in open('lr2.txt').readlines():
	pure = line.replace('\n','').replace('\r','').replace(' ','')
	if pure.startswith('\t'):
		deps = '"csearch:'+pure.replace('\t','')+'"'
		key = skillName+' -> '+deps
		if key not in s2:
			print('\t',key,sep='',end=';\n')
			s2.add(key)
	else:
		skillName = '"skill:'+pure+'"'
		print('subgraph cluster_2 { '+skillName+'}')

s3 = set()
for line in open('lr3.txt').readlines():
	pure = line.replace('\n','').replace('\r','').replace(' ','')
	tv = pure.split('\t')
	task = '"csearch:'+tv[0]+'"'
	print('subgraph cluster_3 { '+task+'}')
	skill = '"cfunc:'+tv[1]+'"'
	key = task+' -> '+skill
	if key not in s3:
		print('\t',key,sep='',end=';\n')
		s3.add(key)

cFuncName = "ERROR SKILL NAME"
s4 = set()
for line in open('lr4.txt').readlines():
	pure = line.replace('\n','').replace('\r','').replace(' ','')
	if pure.startswith('\t'):
		pre = ''
		if pure.replace('\t','').startswith('makeIt'):
			pre = 'factory:'
		else:
			pre = 'ftask:'
		deps = '"' + pre +pure.replace('\t','')+'"'
		key = cFuncName+' -> '+deps
		if key not in s4:
			print('\t',key,sep='',end=';\n')
			s4.add(key)
	else:
		cFuncName = '"cfunc:'+pure+'"'
		print('subgraph cluster_4 { '+cFuncName+'}')

s5 = set()
factorySet = set()
for line in open('cr1.txt').readlines():
	pure = line.replace('\n','').replace('\r','')
	tv = pure.split('\t')
	key = '"factory:'+tv[0]+'"'
	value = '"ftask:'+tv[1]+'"'
	g = key + ' -> ' + value
	if g not in s5:
		print('subgraph cluster_5 { '+key+'}')
		print('\t',g,sep='',end=';\n')
		s5.add(g)

for line in open('cr2.txt').readlines():
	pure = line.replace('\n','').replace('\r','')
	tv = pure.split('\t')
	key = '"ftask:'+tv[0]+'"'
	value = '"cskill:'+tv[1]+'"'
	g = key + ' -> ' + value
	print('subgraph cluster_6 { '+key+'}')
	print('\t',g,sep='',end=';\n')

for line in open('cr3.txt').readlines():
	pure = line.replace('\n','').replace('\r','')
	tv = pure.split('\t')
	key = '"cskill:'+tv[0]+'"'
	value = '"sfile:'+tv[1]+'"'
	g = key + ' -> ' + value
	print('subgraph cluster_7 { '+key+'}')
	print('subgraph cluster_8 { '+value+'}')
	print('\t',g,sep='',end=';\n')

skillName = "ERROR NAME"
s6 = set()
for line in open('cdeps.txt'):
	if line.startswith('\t'):
		pure = line.replace(' ','').replace('\t','').replace('\n','').replace('\r','')
		skill = ''
		if 'PlayerRole::' in pure:
			skill = '"'+'factory:'+pure.replace('PlayerRole::','')+'"'
		elif 'TaskFactoryV2::Instance()->' in pure:
			skill = '"'+'ftask:'+pure.replace('TaskFactoryV2::Instance()->','')+'"'
		else:
			skill = "ERROR!!!!!!!!!!!!!"
		out = skillName+' -> '+skill
		if out not in s6:
			print(out)
			s6.add(out)
	else:
		pure = line.replace(' ','').replace('\t','').replace('\n','').replace('\r','')
		skillName = '"sfile:' + pure + '"'	

print('}')