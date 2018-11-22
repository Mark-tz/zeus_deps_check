import glob
import os
import re

FILTER = os.environ.get('ZROOT')+'ZBin/lua_scripts/play/*/*.lua'
FILTER2 = os.environ.get('ZROOT')+'ZBin/lua_scripts/play/*/*/*.lua'

for name in glob.glob(FILTER)+glob.glob(FILTER2):
	skillName = os.path.splitext(os.path.basename(name))[0]
	print(skillName)
	s = set()
	for code in open(name).readlines():
		pure = code.replace(' ','').replace('\t','').replace('\n','').replace('\r','')
		if re.search('=task\.(.+?)\(',pure):
			res = re.search('=task\.(.+?)\(',pure).group(1)
			if res not in s:
				print('\t',res,sep='')
				s.add(res)