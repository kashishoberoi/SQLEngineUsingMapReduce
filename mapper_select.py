import csv
import sys
def mapper_1(df,query):
	df = df.split(",")
	mapp = dict([['Name',0],['0',1], ['1',2], ['2',3], ['3',4]])
	if("WHERE" in query):
		whr = query[query.index("WHERE")+len("WHERE"):]
		whr = whr.split(",")
		whr = [x.split("=") for x in whr]
		for whrindex in range(len(whr)):
			if (df[mapp[whr[whrindex][0].strip()]] == whr[whrindex][1].strip().strip('"')):
				slct = query[query.index("SELECT")+len("SELECT"):query.index("FROM")]
				if(slct.strip() == "*"):
					return query,",".join(df)
				else:
					slct = slct.strip().split(",")
					slct = [x for x in slct if('COUNT' not in x and 'MAX' not in x and 'MIN' not in x)]
					if(len(slct)>0):
						slct = [mapp[x] for x in slct]
						df = [df[index] for index in slct]
						return query,",".join(df)
					else:
						return query,",".join(df)
		return "\n","\n"
	else:
		slct = query[query.index("SELECT")+len("SELECT"):query.index("FROM")]
		slct = slct.strip().split(",")
		slct = [x for x in slct if('COUNT' not in x and 'MAX' not in x and 'MIN' not in x)]
		if(len(slct)<=0):
			return query,",".join(df)
		if(slct[0].strip() == "*"):
		    return query,",".join(df)
		else:
		    if(len(slct)>0):
		        slct = [mapp[x] for x in slct]
		        df = [df[index] for index in slct]
		        return query,",".join(df)
		    else:
		       	return query,",".join(df)

                
if __name__ == "__main__":
	content = sys.stdin
	query = "SELECT COUNT(2),MIN(1),MAX(1) FROM music-scales WHERE 1=2"
	for df in content:
		key,value = mapper_1(df,query)
		if(key != "\n" and value !="\n"):
			print(key,"&&*&&",value)
