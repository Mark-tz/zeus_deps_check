import os
import re
FILE = os.environ.get('ZROOT')+'Medusa/src/LuaModule/LuaModule.cpp'

for code in open(FILE).readlines():
	pure = code.replace(' ','').replace('\t','').replace('\n','').replace('\r','')
	res = re.search('{"(.+?)",(.+?)},',pure)
	if res:
		print(res.group(1),res.group(2),sep='\t')