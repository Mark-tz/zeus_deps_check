import glob
import os
import re

FILTER = os.environ.get('ZROOT')+'Medusa/src/Strategy/skill/*.cpp'

for name in glob.glob(FILTER):
	skillName = os.path.splitext(os.path.basename(name))[0]
	if skillName == 'Factory':
		continue
	print(skillName)
	for code in open(name).readlines():
		pure = code.replace(' ','').replace('\t','')
		if 'setSubTask' in pure and '//setSubTask' not in pure:
			print('\t' , re.search('setSubTask\((.+?)\((?!\)).*',pure).group(1),sep='');
