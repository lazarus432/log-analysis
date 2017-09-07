#Synopsis

This file pulls information from three tables in the database news. And displays a report
with the three most popular articles, the most popular authors, and the days where error
request are greater than 1%.

#Installation

1. Download the file `newsdata.sql`
2. Place the file inside vagrant folder
3. Log into terminal and the vagrant directory
4. Type `vagrant up` in terminal to open virtual machine
5. Type `vagrant ssh` in terminal to sign in
6. To load the data, use the command `psql -d news -f newsdata.sql` in terminal
7. Type `psql news` to access the database inside terminal

#Created Views

##Question 1


###Gather important information from log table

`CREATE VIEW vlog AS
SELECT path, count(*) as num from log
group by path;`

###Joins vlog with articles where the slug matches path from vlog

`CREATE VIEW logCorrect AS
SELECT (regexp_split_to_array(path, E'/article/')) [2] AS path, author, num as num
FROM vlog, articles
WHERE path <> '/' and (regexp_split_to_array(path, E'/article/')) [2] = articles.slug and path <> ' '
ORDER BY num desc;`

###Appropriate author name with article and number of views

`CREATE VIEW authorview AS
SELECT authors.name, logCorrect.path, logCorrect.num
FROM authors, logCorrect
WHERE logCorrect.author = authors.id
GROUP BY logCorrect.path, authors.id, logCorrect.num
ORDER BY logCorrect.num desc;`

###QUESTION 1 FINAL VIEW

`CREATE VIEW titleFinal AS
SELECT title, num
FROM authorview, articles
WHERE authorview.path = articles.slug
ORDER BY num desc limit 3;`


##Question 2

###QUESTION 2 FINAL

`CREATE VIEW authorFinal AS
SELECT authorview.name, SUM(authorview.num) AS views
FROM authorview
GROUP BY authorview.name
ORDER BY views desc;`


##Question 3

###Total requests separated by dates

`CREATE VIEW totalRQT AS
SELECT time ::timestamp::date AS date, count(log.status) as requests
FROM log
GROUP by date
ORDER BY date asc;`

###Total 404 request separated by dates

`CREATE VIEW error404 AS
SELECT time ::timestamp::date AS date, count(log.status) AS error404
FROM log
WHERE log.status <> '200 OK'
GROUP BY date
ORDER BY date asc;`

###Calculation

`CREATE VIEW errorpercent AS
SELECT totalRQT.date, cast (error404.error404 AS float) / cast(totalrqt.requests AS float) AS percent
FROM totalRQT, error404
WHERE totalrqt.date = error404.date;`

###QUESTION 3 FINAL

`CREATE VIEW errorfinal AS
SELECT * FROM errorpercent
WHERE errorpercent.percent > .01;`
