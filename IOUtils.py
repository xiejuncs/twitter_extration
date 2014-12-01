import codecs

"""
return files as a list of lines:
"""
def readFiles(path):
	f = open(path, "r")
	lines = f.readlines()

	ret = []
	for line in lines:
		ret.append(line.strip())

	return ret 

'''
write list to file line by line
'''
def write(path, l):
	with codecs.open(path, 'w', encoding='utf-8') as out:
		out.write('\n'.join(l))
