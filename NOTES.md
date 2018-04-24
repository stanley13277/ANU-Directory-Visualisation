# The Project
This Project contains two python scripts that can be directly ran,
before we get into the details,
please install the required modules listed below.

## The Requirements
The ANU Staff Directory Analysis requires the following Python libraries to be installed.
* fuzzywuzzy,
* threading,
* time,
* lxml,
* requests,
* sys,
* matplotlib
* pylab,
* json
* python-Levenshtein

## The Data Collector
__WARNING__ The Data_Colletor.py script is estimated to take 6.5 days to complete,
however an incomplete version of the output can still be used in the next stage.

to collect the data from the ANU Staff Directory,
run Data_Collection.py in the projects root directory.
This will crawl the ANU Staff Directory using uniIDs as its Index,
It will save the output as FinalData.txt in the Directory it ran from.

## The Presentation
The Presentation script which is also located in the project root directory,
will require the Data-Collection.txt file in the same directory it ran from,
simply run presentation.py and wait a few moments for the graphs to be presented.
estimated run time to compare all users in the dataset is 2-3 minutes.


