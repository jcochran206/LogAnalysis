# LogAnalysis

this small project requires me to utilize vagrant and virtualbox to analize a postgresql database.  
the questions are:
 1) What are the most popular three articles of all time?
 2) Who are the most popular article authors of all time?
 3) On which days did more than 1% of requests lead to errors?

# requirements
virtualbox
vagrant 
upload newsdata.sql in vagrant virtual machine

#configuration 
-install virtualbox and vagrant 
-open vagrant folder in git
-execute these cmds:
  1) vagrant up
  2) vagrant ssh
-upload newsdata.spl 
  1) psql -d news -f newsdata.sql
#How to execute in python
python3 LogTestTool.py ~ or yourfilename.py
