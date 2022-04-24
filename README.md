# Election_Analysis

##Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. The total number of votes cast.
2. The number of votes for each county.
3. Calculate percenatage of votes from each county.
4. Determine county with the highest turnout.
5. A complete list of candidates who received votes.
6. Calculate the percentage of votes each candidate received.
7. Calculate the percentage of votes each candidate won.
8. Determine the winner of the election based on popular vote.

##Resources
- Data Source: election_results.csv
- Software Python 3.6.1, Visual Code, 1.38.1

##Summary
The analysis of the elections show that:
There were 369,711 votes cast in the election.

There are 3 counties in the election.
  - Denver
  - Jefferson
  - Arapahoe
  
The county results were:
  - Jefferson county had 10.5% of voters for 38,855 voters.
  - Denver county had 82.8% of voters for 306,055 voters.
  - Arapahoe county had 6.7% of voters for 24,801 voters.

The follwoing code was used to find county percentage:

![Get_Votes_Calculate_Percentage](https://github.com/joeapodaca/stock-analysis/blob/main/2018%20Analyze.PNG)
  
The county with highest turnout was:
 - Denver

The follwoing code was used to find the turnout:

![Determine_Winning_County](https://github.com/joeapodaca/stock-analysis/blob/main/2018%20Analyze.PNG)

The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
  
 The candidate resutls were:
  - Charles Casper Stockham recieved 23.0% of the vote and 85,213 number of the votes.
  - Diana DeGette recieved 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote  and 11,606 of votes.
  
 The winner of the election was:
 - Diana DeGette, who recieved 73.8% of the vote and 272,892 number of votes.
 
 ##Challenge Overview
 For the challenge portion of this project the county information had to be added to the analysis.
 
 ##Challenge Summary
 This code is written to be easily changed for the next election.  As long as the election results are saved as election_results.csv, the candidate is in colum C and     the county is column B.
