import os
import re
FILE = os.environ.get('ZROOT')+'ZBin/lua_scripts/worldmodel/task.lua'
STATE = False
for line in open(FILE):
	pure = line.replace('\t','').replace(' ','').replace('\n','').replace('\t','')
	if STATE:
		if re.search('localmexe,mpos=(.+?){',pure):
			print(re.search('localmexe,mpos=(.+?){',pure).group(1))
			STATE = False
	else:
		if re.search('function(.+?)\(',pure):
			res = re.search('function(.+?)\(',pure).group(1)
			if res != 'continue' and res != 'universal':
				print(res,end='\t')
				STATE = True
