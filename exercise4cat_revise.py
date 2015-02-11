
file_name = "pg1513.txt"

#read the file
my_file = open ( "pg1513.txt", "r")

#generate line, word, letter number variables
linenum = 0
wordnum = 0
letternum = 0

#generate a empty dict
dict = {}

#using loop commands
for line in my_file:
	
	#remove all the punctuation from the file
	noa = line.replace( ",", "" )
	nob = noa.replace( ".", "" )
	noc = nob.replace( "!", "" )
	nod = noc.replace( "?", "" )
	noe = nod.replace( "-", "" )
	nof = noe.replace( "/", "" )
	nog = nof.replace( ":", "" )
	noh = nog.replace( ";", "" )
	
	#split the file from lines into words
	wordlist = noh.split()
	
    #count the word and put them into dict
	for element in wordlist:
		if ( element in dict ):
			dict[element] += 1
		else:
			dict[element] = 1
		
#print the results 
for name, value in dict.items():
print ( name + "    " + str(value) )
