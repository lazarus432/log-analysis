# Log Analysis Report

This file pulls information from three tables in the database news. Displays a report
with the three most popular articles, the most popular authors, and the days where error
request are greater than 1%.

## Prerequisites

* Vagrant will need to be installed. Here is a link: [Vagrant](https://www.vagrantup.com/)

## Installation

1. Download the file `newsdata.sql`
2. Place the file inside vagrant folder
3. Log into terminal and the vagrant directory
4. Type `vagrant up` in terminal to open virtual machine
5. Type `vagrant ssh` in terminal to sign in
6. To load the data, use the command `psql -d news -f newsdata.sql` in terminal
7. Type `psql news` to access the database inside terminal

## Built With

* [PostgreSQL](https://www.postgresql.org/)
* [Psycopg](http://initd.org/psycopg/) - PostgreSQL adapter for Python
* [Vagrant](https://www.vagrantup.com/intro/index.html) - Introduction to Vagrant

## Author

* **Nicolas Bolduc** _-Initial Work-_ [Lazarus](https://github.com/lazarus432)