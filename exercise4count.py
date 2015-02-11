file_name = "pg1513.txt"
cd
my_file = open( "pg1513.txt", "r")
linenum=0
wordnum=0
letternum=0
for line in my_file:
	linenum=linenum+1
	wordlist = line.split()
	wordnum=wordnum+len(wordlist)
	for element in wordlist:
		letternum =letternum+len(element)
	
print linenum
print wordnum
print letternum
my_flie.close()