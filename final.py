s = set([])
print('digraph G {\n\trankdir=LR;')
skill = 'ERROR_SKILL_NAME'
for line in open('cr.txt'):
	pure = line.replace('\n','').replace('\r','')
	if pure.startswith('\t'):
		deps = pure.replace(' ','').replace('\t','')
		key = deps+' -> '+skill
		if key not in s:
			print('\t',key,sep='')
			s.add(key)
	else:
		skill = pure
print('}')
# print(sorted(s))