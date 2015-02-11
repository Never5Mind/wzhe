file_name = "pg1513.txt"

cd

#read the file
my_file = open ("pg1513.txt", "r")

#generate line number, work number, and letter number variables
linenum = 0
wordnum = 0
letternum = 0

#using loop command to calculate 
for line in my_file:
	linenum = linenum + 1
	wordlist = line.split()
	wordnum = wordnum + len(wordlist)
	for element in wordlist:
		letternum = letternum + len(element)

#print the results	
print linenum
print wordnum
print letternum

#close the file
my_flie.close()