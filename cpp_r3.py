import glob
import os
import re

FILTER = os.environ.get('ZROOT')+'Medusa/src/Strategy/skill/*.h'

for name in glob.glob(FILTER):
	skillName = os.path.splitext(os.path.basename(name))[0]
	# print(skillName)
	for code in open(name).readlines():
		pure = code.replace(' ','').replace('\t','')
		if re.search('class(.+?):',pure):
			print(re.search('class(.+?):',pure).group(1),skillName,sep='\t');

