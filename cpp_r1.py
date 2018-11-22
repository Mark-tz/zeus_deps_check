import re
import os
FILE = os.environ.get('ZROOT')+'Medusa/src/Strategy/skill/Factory.cpp'

STATE = False
for code in open(FILE).readlines():
	pure = code.replace(' ','').replace('\t','')
	if STATE:
		if "TaskFactoryV2::Instance()->" in pure:
			print(re.search('->(.+?)\(',pure).group(1))
			STATE = False
	else:
		if "makeIt" in pure:
			print(re.search('\*(.+?)\(',pure).group(1),end='\t')
			STATE = True
