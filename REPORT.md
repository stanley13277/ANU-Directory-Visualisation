 # ANU Staff Directory Map

## Group Members
Luke Tinker - u5318579  
Kim To - u5371962  
Yen Wei Li - u6149684

## Overview


__The Idea__  
The starting goal of this project was to collect, transform and present,
Publicly available information from the Australian National University,
after some other impractical ideas were put to rest it was decided,
we would use the Australian National Universities Staff Directory.


## Planning

The Directory did not provide the data in a ready to consume easy access method,
resulting in there being a bit of additional work to collect the data,
due to identifying this we decided we would break the responsibility of the
components in the project to the individual members of the project,
This resulted in Yen Wei Li being responsible for the Collection of data,
Kim To responsible for Transforming the data for it to be presented and
Luke Tinker responsible for the presentation of the data.



## Outcome

__Use of the presented data__  
The final outcome of the project was the production of two different graphs,
each showing a different method of viewing the data collected in a meaningful
way, the first a bar graph which shows stand alone organizational units with
a count of members from the unit,
The other showing the relationship between organizational units and staff,
this revealed relationships where staff were a member of two or more roles at the ANU.





## Challenges

__About Meetings Milestones__  
With the allocation of work being done as each member being responsible for
a specific task within the project it became evident that there were bottlenecks
in our ability to plan certain components, however we were able to do a small
amount of sudo code and researching the tools we were to use in the first week,
with the core coding and refactoring spanning into the final week of the project.


### The Collector
The data is collected from ANU official Staff directory website
(http://www.anu.edu.au/_anu/staffdir/search.php). 
The collector sys module was used for inserting all the data into FinalData.txt 
file, request module for getting HTML from the website, and lxml-html 
module for extracting useful data from the website. 

Overall all the function run very smoothly and collect all the excepted 
data from the website. 
However, due to the function only requesting one webpage at a time,
it runs very slow.
Due to this an attempt was made to speed it up by using the multi-thread
module "threading" to request multiple website at once, but due to 
time limitation, this functionality could not be completed.
as a result of this, A work around was done to get the date faster,
this was achieved by  dividing uni_id crawled per instance of the
Data_Collection.py script into various ranges.
For example, 0000000-2000000, 2000000-3000000, 3000000-4000000.....etc. 
Doing this significantly increases the efficiency,
but required all the data to be merged together,
Once, all the data is collected and transferred into single file.
It was ready to analyse. 

There are some small issues while collecting the data. 
For example, from the ANU staff directories search website, some uni_id 
will have name, but do not have any role at university, this will cause 
the data-set to record and empty list for the University ID.
This was resolved by handling it in the data parsing stage.

### The Parser
Once the data-set from the Data-Collector is generated,
the next task was to identify which roles are part of the hierarchy
and which roles are not.
To do this data parse was created,
this would filter out the roles not part of the heirachy 
and partition people into groups depending on which roles they have listed 
in the ANU data.
The next challenges found,
was that there were spelling mistakes in the data provided by ANU. 
There were also inconsistencies in the use of special symbols such as &. 
These were problems for the initial implementation as people were being 
placed in different roles when they should placed in the same role. To 
solve this we implemented fussy string matching using the library fuzzy 
wuzzy. This allowed us to compare misspelled rolls with all of the expected 
roles and rectify the spelling mistakes.

### The Presenter

The overall presentation of both the graphs was a challenge,
initially both graphs were designed to be drawn in a single matplotlib window.
however due to the amount of information being shown by both graphs,
the code was changed to draw both graphs in separate windows,
this allowed for more flexibility when displaying the final data,
There was also some work made to statically enforce the size of the bar graph,
this was to try to and ensure it presented better.
however due to the possible differences in resolution of the computers
this it was decided to not be developed to heavily.

Due to the massive number of nodes being placed on the networkx diagram,
it was a challenge to try and make the data readable,
after several refactors of the code it was decided to go with the approach,
Labels for the staff will not be displayed as there were to many nodes,
Labels for the hierarchy would be shown to visually allow reference of public presence,
Nodes for Staff would be coloured green and made circular while Node for hierarchy
would coloured red and made squares, sizing of the individual nodes was also adjusted,
this is to help reduce the overlap of nodes, edges lines were also changed to grey,
this is to make it easier to read the hierarchy nodes labels.

Matching users was initially a challenge,
this was due to originally trying to do dictionary to nested dictionary iteration,
which was not only very computationally heavy but time consuming to write,
this was later changed to simply building node edge lists
using the previously iterated hierarchy construction made to build node edge
relationships between the university hierarchy json file.





 ### Other Challengers
 One of the Key lessons learned with this project is,
 it is best to know as much of the data sets source you are dealing with,
 before starting or learning about it as early on as possible.
 another lesson learned is deciding on presentation before having a good sense
 of the data being presented is not the best approach,
 typically it is better to analyse the data set first then work through different
 presentation methods until you find the best fit for the data set.

