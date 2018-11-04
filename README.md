# Programming Skills -- Coursework 1
This is a full development framework that implements a sequential version of a two-dimensional predator-prey model with spatial diffusion using Python. <br> 
## Getting started
### Prerequisites
Python 3.0 and up 
### Installing
1. The version of code is **python 3.6**, you need to load module at first using the command line as below 
```
   $ module load anaconda/python3
```

2. To implement test you need to install **pytest**. Type the following command at the command line
```		
   $ pip install -U pytest
```
## Deployment
`step1:module_index.py` It can read XML file and provide a print version of the index in text format called index.txt. Please put the xml file in the same directory as the .py file at first.<br>
`step2:module_search.py` It can load index.txt and queries.boolean.txt, allowing Boolean search, Phrase search and Proximity search and will output a file called results.boolean.txt.<br>
`step3:module_ranked.py` It can load index.txt and queries.ranked.txt ,allowing Ranked IR based on TFIDF and will output a file called results.boolean.txt.<br> 

## Author
This software was developed by Yajuan Zhang. <br>
For any question and for reporting bugs please send an email to Yajuan Zhang at: s1883916@ed.ac.uk<br>
