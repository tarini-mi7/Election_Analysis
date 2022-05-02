# Election_Analysis
## Project Overview
A Colorado Board of Elections employee assigned the following tasks to complete the election audit of a recent local congressional election.

* Calculate the total number of votes cast.
* Get a complete list of candidates who received votes.
* Calculate the total number of votes for each candidate received.
* Calculate the percentage of votes each candidate won.
* Determine the winner of the election based on popular vote.
* Calculate the voter turnout for each county.
* Calculate the percentage of votes from each county out of the total.
* Determine the county with the highest turnout.
## Resources
Data Source: election_results.csv
Software: Python 3.9.1, Visual Studio Code 1.52.1
## Summary
The analysis of the election shows that:

There were 369,711 votes cast in the election.

## The candidates were:

* Charles Casper Stockham
* Diana DeGette
* Raymon Anthony Doane

## The candidate results were:

* Charles Casper Stockham received 23.0% of the vote, for a total of 85,213 votes.
* Diana DeGette received 73.8% of the vote, for a total of 272,892 votes.
* Raymon Anthony Doane received 3.1% of the vote, for a total of 11,606 votes.

The winner of the election was:
**Diana DeGette**, who received 73.8% of the vote for a total of 272,892 votes.
## The voter turnout for each county was:

* Jefferson produced 10.5% of voters, for a total of 38,855 voters.
* Denver produced 82.8% of voters, for a total of 306,055 voters.
* Arapahoe produced 6.7% of voters, for a total of 24,801 voters.

The county with the largest voter turnout was:
**Denver**, which produced 82.8% of voters, for a total of 306,055 voters.

Election Results Snapshot

![alt text](https://github.com/tarini-mi7/Election_Analysis/blob/main/resources/output.png)

# Election-Audit Summary
We were able to easily expand our script to include voter turnout by county once we had the logic for candidate results in place. The combined insight was more informative for decision making in terms of allocating election resources. This script can be an important aid in on demand election analysis. One may run this script again and again at any phase of the election to track live progress.

We can modify the script further to determine what percentage of each county voted for each candidate by adding an if-statement. 

Similarly, if this were a federal election, we could use the same script and change the county to states.

In short, no matter the number of candidates or counties, the script used to perform the Election Audit can be a valuable resource for the board.
