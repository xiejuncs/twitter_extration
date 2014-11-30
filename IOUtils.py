path = "/home/jun/open_source/credentials/twitter/twitter_credential.txt"


"""
return files as a list of lines:
"""
def readFiles(path):
	f = open(path, "r")
	lines = f.readlines()

	ret = []
	for line in lines:
		print line.strip()
		ret.append(line.strip())

	return ret 
