# Webscraping-Project For Care Opinion

## Introduction 

The aim of this project is to scrape all the information from the roughly 11,000 reviews at https://www.careopinion.org.au/. The information will be used in a NLP program to see the emotional affect in different aspects of the healthcare field. The information is available in both a database and as text files. The project also requires a Graphical User Interface so a client can scrape new files and search the database for specific words. 

## The Database 

The database is coded in sqlite as it needed to be persistent. Basic SQL queries can be used to retrieve data with specific characteristics. For example retreiving all reviews that claimed nurses where good at communication. The database contains three tables, review, response and update. 

## The GUI

The GUI is coded in TKinter, a simple python interface. While it can be used both to scrape and search the database, we would advise using *DB Browser* to do database searching. This is beacause *DB Browser* has optimised functions, is possible to search by mulitple terms and can export to an excel file. 

## Using this code

Make a virtual environment:
On Mac:

```
$ python3 -m venv venv
$ source venv/bin/activate
```

On Windows:
```
$ python3 -m venv venv
$ venv/Scripts/activate
```

And make sure all packages are up to date:

```
(venv) $ pip3 install -r requirements.txt
```
