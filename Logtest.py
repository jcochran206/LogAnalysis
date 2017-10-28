#!/usr/bin/env python Logtest.py
# -*- coding: utf-8 -*-

# Created by Jonathan Cochran
# Description: Develop a console tool to print out log status
# Connedtion string tester
# try:
# conn = psycopg2.connect("dbname=news")
# print("connected")
# except:
# print "I am unable to connect to the database"

import psycopg2
from datetime import datetime

DBNAME = 'news'


def print_articles():
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    c.execute("""select title, count(title) as views
        from articles,log where log.path = concat('/article/',articles.slug)
        group by title order by views desc limit 3;""")
    query1 = c.fetchall()
    print("popular articles:")
    for record in query1:
        print(
            '\t' + '"' + str(record[0]) + '"' + '---' +
            str(record[1]) + 'views')
    conn.close()


def print_authors():
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    c.execute("""select authors.name, count(articles.author)
    from log, articles, authors
    where log.path = concat('/article/',articles.slug)
    and authors.id = articles.author
    group by authors.name order by authors.name desc;""")
    query2 = c.fetchall()
    print("popular authors:")
    for record in query2:
        print(
            '\t' + '"' + str(record[0]) + '"' + '---' +
            str(record[1]) + 'views')
    conn.close()


def print_error():
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    # execute query
    c.execute("""select date, round(errors * 100.00/total,2)percent
    from (select to_char("time", 'Month DD YYYY') date, count(*) total,
    count(*) filter(where log.status != '200 OK') errors
    from log group by date) sub where round(errors * 100.00/total,2) > 1
    order by percent;""")
    # fecth data
    query3 = c.fetchall()
    print("error log:")
    for record in query3:
        print(
            ""'\t' + '"' + str(record[0]) + '"' + '---' +
            str(record[1]) + '%errors'"")
    conn.close()


if __name__ == '__main__':
    print_articles()
    print_authors()
    print_error()
