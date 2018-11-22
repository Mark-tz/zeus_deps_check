import os
import re
FILE = os.environ.get('ZROOT')+'Medusa/src/Strategy/skill/Factory.cpp'

STATE = False
for code in open(FILE).readlines():
	pure = code.replace(' ','').replace('\t','')
	if STATE:
		if "MakeTask<" in pure:
			print(re.search('MakeTask<(.+?)>',pure).group(1))
			STATE = False
	else:
		if "CTaskFactoryV2::" in pure and 'CTaskFactoryV2::MakeTask' not in pure:
			print(re.search('CTaskFactoryV2::(.+?)\(',pure).group(1),end='\t')
			STATE = True
