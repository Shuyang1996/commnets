file_object = open("test.txt","r");
output = open("output.txt","w");
# for line in file_object: 
# 	print line, 
# print file_object.readline(3);

for line in file_object:
	for letter in line:
		output.write(bin(ord(letter)))

output.close()






# name = 'jarad'
# for letter in name:
# 	print(bin(ord(letter)))