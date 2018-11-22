import os
import re
FILE = os.environ.get('ZROOT')+'Medusa/src/LuaModule/LuaModule.cpp'
for code in open(FILE).readlines():
	pure = code.replace(' ','').replace('\t','').replace('\n','').replace('\r','')
	if "extern\"C\"intSkill_" in pure:
		print(re.search('extern"C"int(.+?)\(',pure).group(1))
	elif 'PlayerRole::' in pure:
		print('\t',re.search('PlayerRole::(.+?)\(',pure).group(1),sep='')
	elif 'TaskFactoryV2::Instance()->' in pure:
		print('\t',re.search('TaskFactoryV2::Instance\(\)->(.+?)\(',pure).group(1),sep='')
