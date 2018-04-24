Luke Tinker (u5318579) -- 2016-08-27

# Purpose
Use this file to keep a record of any insights, techniques, tips, or references.
### Insights
In order to analysis the directory in a meaningful way,
we will need to build records of hierarchy elements, e.g. Office of the Vice Chancellor,
as some records may not match exactly with each other we will need to employ a method of close grouping,
e.g. Vice Chancellor Office, Office of the Vice Chancellor or Office of the Vice-Chancellor.

once the logic above has been implemented,
two databases will exist,
one that contains hierarchy elements, the other personnel elements,
it is these two databases that will be used to build the graph dataset.
some examples are,
edge['u5318579', Information Technology Services] # example of personnels relation with hierarchy element
edge['Information Technology Services', 'Office of the Vice Chancellor'] # example of hierarchy elements relationship with another hierarchy element.

When visualizing the nodes
Personnel nodes should be represented as a green coloured circle,
hierarchy nodes should be represented as a red coloured square,




### ANU Directory Analysis


### Techniques


### Tips
when using NetworkX, there is no need to add a node as well as the edges,
as if you add the edges the nodes will be created.


### References
Read content [NetworkX official website](https://networkx.github.io/) to better understand using NetworkX.
Read [Documentation from python.org](https://docs.python.org/3/) for any refreshers or clarification on functions.
