# CPSC-449-Final-Project

## team members

Guang Chen kp82611@csu.fullerton.edu  
Sami Bajwa samibajwa@csu.fullerton.edu

## Description:

An online bookstore API that allows users to view, search, and purchase books. The API will is built using FastAPI and the book data is stored in MongoDB.

## Setup

1. create a virtual environment  
   `python -m venv venv`

2. enter virtual environment  
   windows: `venv\Scripts\activate`  
   linux: `venv/bin/activate`

3. install requirements  
   `pip install -r requirements.txt`

4. set up mongoDB create database and collection  
   run`python mongo.py`
5. run the main file to start api  
   `uvicorn app:app --reload`
