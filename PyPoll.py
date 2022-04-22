#The data we need to retrieve.
#1. The total number if votes cast.
#2. A complete list of candidates whoe received votes.
#3. The percentage of votes each candidate won.
#4 the total number of votes each candidate won.
#5 The winner of the election based on popular vote.

#Add dependencies
import csv
from distutils import text_file
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
    


     # To do: perform analysis.
     #Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     #Print the header row.
     headers = next(file_reader)
     print (headers)
     
     #Print each row in the CSV file.
     #for row in file_reader:
         #print(row)










#Create a filename variable to direct or indirect path to save the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the opn() function with the "w" mode will write data to the file.
#open(file_to_save, "w")
#Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")
#Write Hello World to file.
#outfile.write("Hello World")
#close the file
#outfile.close()
#Using the with statement to open the file as text file.
#with open(file_to_save,"w") as txt_file:
    #Write Hello World
    #txt_file.write("Hello World")
#Write 3 counties to the file
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")
#Write 3 counties to file at one time
    #txt_file.write("Arapahoe, Denver, Jefferson")
#Add \n to create each county on its own line
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

