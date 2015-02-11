# IPython log file

#generate heights list
heights = (158, 174, 175, 176, 177, 179)

#generate summation and number of terms
sum = sum(heights)
num = len(heights)

#using loop to calculate
for height in heights:
    sum = sum + height
    num = num + 1
    print sum/num 

#generate average    
ave = sum/num

#print the results
print ave


#[Out]# u'C:\\Users\\Andrew\\Documents\\Python Scripts'
