import glob
import os
import re

FILTER = os.environ.get('ZROOT')+'ZBin/lua_scripts/skill/*.lua'

for name in glob.glob(FILTER):
	skillName = os.path.splitext(os.path.basename(name))[0]
	print(skillName)
	for code in open(name).readlines():
		pure = code.replace(' ','').replace('\t','').replace('\n','').replace('\r','')
		if re.search('return(.+?)\(',pure):
			skill = re.search('return(.+?)\(',pure).group(1)
			if '.' not in skill and ':' not in skill:
				print('\t',skill,sep='');
