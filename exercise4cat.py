file_name = "pg1513.txt"
my_file = open( "pg1513.txt", "r")
linenum=0
wordnum=0
letternum=0
dict = {}
for line in my_file:
	linenum=linenum+1
	noa=line.replace(",","")
	nob=noa.replace(".","")
	noc=nob.replace("!","")
	nod=noc.replace("?","")
	noe=nod.replace("-","")
	nof=noe.replace("/","")
	nog=nof.replace(":","")
	noh=nog.replace(";","")
	wordlist=noh.split()
	wordnum=wordnum+len(wordlist)
	for element in wordlist:
		if( element in dict ):
			dict[element] += 1
		else:
			dict[element] = 1
		letternum =letternum+len(element)
for name, value in dict.items():
print ( name + "    " + str(value))
