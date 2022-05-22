# Automated-Resume-Parser

## DESCRIPTION: 

* Automating the task of extracting data from resumes and sending a concise report of candidate compatibility. 
* This project will go through the resumes that are in pdf format and convert them to individual text files first using the pdfminer library and store them in a folder. 
* Then it will extract only the info that we need using the Named Entity Recognition feature of Natural Language Processing offered by the spaCy library and Pattern Matching using the (re) Regular Expression library to extract phone numbers and skillsets. 
* Once the parsing is done only relevant information is left in a structured format, and with the help of pandas DataFrame, that can be saved in CSV file type and also stored in a database. 
* This final resulting file will contain all the extracted info in one place that can be easily accessed. After a successful run, an Excel file will open automatically.

## THEORY:

### spaCy:
* spaCy is a free and open-source library for Natural Language Processing (NLP) in Python with a lot of in-built capabilities. It’s becoming increasingly popular for processing and analyzing data in NLP. spaCy is a free, open-source library for NLP in Python. It’s written in Cython and is designed to build information extraction or natural language understanding systems.
* Sentence Detection is the process of locating the start and end of sentences in a given text. This allows you to divide a text into linguistically meaningful units. You’ll use these units when you’re processing your text to perform tasks such as part of speech tagging and entity extraction.
spaCy has different types of models. 
* The default model for the English language is en_core_web_sm.

### Pandas:
* Pandas is an open-source library that is made mainly for working with relational or labelled data both easily and intuitively. It provides various data structures and operations for manipulating numerical data and time series. This library is built on top of the NumPy library. Pandas is fast and it has high performance & productivity for users.
* Pandas DataFrame is a two-dimensional size-mutable, potentially heterogeneous tabular data structure with labelled axes (rows and columns). A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. Pandas DataFrame consists of three principal components, the data, rows, and columns.
* Fast and efficient for manipulating and analyzing data.
* Data from different file objects can be loaded.
* Easy handling of missing data (represented as NaN) in floating point as well as non-floating point data
* Size mutability: columns can be inserted and deleted from DataFrame and higher dimensional objects
* Data set merging and joining.
* Flexible reshaping and pivoting of data sets
* Provides time-series functionality.
* Powerful group by functionality for performing split-apply-combine operations on data sets
* The DataFrame can easily then be exported to a CSV file using the to_csv command.


## INSTALLING DEPENDENCIES:
pip3 install spacy
pip3 install pandas
python3 -m spacy download en_core_web_sm
pip3 install pdfminer

Github File: https://github.com/pdfminer/pdfminer.six/blob/master/tools/pdf2txt.py
→ Load the file in the repository
