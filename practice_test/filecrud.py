import csv

# opening the CSV file
# path = r"C:\\Users\\prite\\OneDrive\\Desktop\\post.csv"
with open('post.csv') as file:
		
	# reading the CSV file
	# csvFile = csv.reader(file, delimiter=",")
	csvFile = csv.DictReader(file)

	# displaying the contents of the CSV file
	for lines in csvFile:
			print(lines)
