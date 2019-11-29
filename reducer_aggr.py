import sys
def reducer_1(count,maxm,minm,key,value):
	query = key
	value = [value]
	mapp = dict([['Name',0],['0',1], ['1',2], ['2',3], ['3',4]])
	if(len(value)>0):
		value = [x.split(",") for x in value]
		if('COUNT' in query):
			count= count+1
		if('MAX' in query):
			colmn_name = query[query.index("MAX")+len("MAX")+1:query.index(")",query.index("MAX")+len("MAX")+1)]
			index = mapp[colmn_name]
			maxm.append(value[0][index])
		if('MIN' in query):
			colmn_name = query[query.index("MIN")+len("MIN")+1:query.index(")",query.index("MIN")+len("MIN")+1)]
			index = mapp[colmn_name]
			minm.append(value[0][index])
		slct = query[query.index("SELECT")+len("SELECT"):query.index("FROM")]
		slct = slct.strip().split(",")
		slct = [x for x in slct if('COUNT' not in x and 'MAX' not in x and 'MIN' not in x)]
		if(len(slct)<=0):
			return count,maxm,minm
		if(slct[0].strip() == "*"):
			print(value)
			return count,maxm,minm
		if(len(slct)>0):
			final = []
			for i in range(len(value)):
				if(value[i] not in final):
				    final.append(value[i])
			print(final)
		else:
			print([])
	return count,maxm,minm

if __name__ == "__main__":
	content = sys.stdin
	i = 0
	count = 0
	maxm = []
	minm = []
	key = ""
	value = ""
	for line in content:
		if(i%2==0):
			key = line.split("&&*&&")[0]
			value = line.split("&&*&&")[1]
			count,maxm,minm = reducer_1(count,maxm,minm,key,value)
		i =i+1
	if("COUNT" in key):
		print("count: ",count)
	if("MAX" in key):
		print("max: ",max(maxm))
	if("MIN" in key):
		print("min: ",min(minm))
