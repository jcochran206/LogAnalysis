# LogAnalysis

this small project requires me to utilize vagrant and virtualbox to analize a postgresql database.  
the questions are:
 1) What are the most popular three articles of all time?
 2) Who are the most popular article authors of all time?
 3) On which days did more than 1% of requests lead to errors?

## requirements

1) [virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
2) [vagrant](https://www.vagrantup.com/)
3) [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## configuration 

* install virtualbox and vagrant 
* open vagrant folder in git
* execute these cmds:
  1) vagrant up
  2) vagrant ssh
* upload newsdata.spl 
  1) psql -d news -f newsdata.sql
  
### How to execute in python
python3 LogTestTool.py ~ or yourfilename.py

### expected Output

### question 1
-popular articles:

	-"Candidate is jerk, alleges rival"---338647views
	-"Bears love berries, alleges bear"---253801views
	-"Bad things gone, say good people"---170098views
### question 2 
-popular authors:

	-"Ursula La Multa"---507594views
	-"Rudolf von Treppenwitz"---423457views
	-"Markoff Chaney"---84557views
	-"Anonymous Contributor"---170098views
 ### question 3
-popular authors:

	-"July      17 2016"---2.26% errors
