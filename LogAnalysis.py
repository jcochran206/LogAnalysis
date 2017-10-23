import psycopg2

DBNAME = "news"

POSTS = [""]

def get_articles():
  """What are the most popular three articles of all time?"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("")
  posts = c.fetchall()
  db.close()
  return posts 

def get_authors():
  """Who are the most popular article authors of all time?"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("")
  posts = c.fetchall()
  db.close()
  return posts 

def get_HTTPErrors():
  """On which days did more than 1% of requests lead to errors?"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("")
  posts = c.fetchall()
  db.close()
  return posts 

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("insert into posts values (%s)", (bleach.clean(content),))
  db.commit()
  db.close()