import re 

#open file and read it 
name = input("Enter file name: ") 
text = open(name, "r") 

#to store data 
count = 0 
total = 0 

#count the numbers and their sum 
for line in text: 
    n = re.findall("[0-9]+", line)

    for num in n: 
        count += 1 
        total += int(num) 

#print the result 
print("There is ", count, "numbers in the file") 
print("The sum of those", count, "numbers is", total)