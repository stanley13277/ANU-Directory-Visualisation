import parser
import networkx as nx
import matplotlib.pyplot as plt
import pylab as pl
import json


def json2list(file):
	"""
	function takes a json file and returns a pyton readable representation of its data.
	:param file: path to json file
	:return: json files data
	"""

	with open(file, 'r') as f:
		data = json.load(f)

	return data
UniHiera = json2list('UniversityHierarchy.json')

G = nx.Graph() # create networkx graph for University Positions

def walker(node, parent=None):
	"""
	function walks the input dictionary,
	if the key of the parent dictionary is know,
	it will append both the parent key and each dictionary key,
	as a tuple to the organization_edges list
	e.g. (ParentKey, Localkey0), (ParentKey, Localkey1)

	:param node: dictionary
	:param parent: defaults to None to allow for recursive use of the walker function.
	:return: None
	"""

	if isinstance(node, dict):
		for k, v in node.items():
			if isinstance(v, dict):
				if parent:
					G.add_node(k,)
					G.add_edge(parent, k)
				walker(v, k)
			elif isinstance(v, list):
				if parent:  # if parent is known pass it in
					for staff in v:
						G.add_edge(staff, parent)



walker(UniHiera)

staff_nodes = []
org_nodes = []
labels = {} # Empty dictionary to use to list what labels should be shown

for n in G.nodes( data=True ):
		org_nodes.append(n[0])
		labels[n[0]] = n[0]

staff_bucket = parser.parse_data('FinalData.txt')

for key, value in staff_bucket.items():
	for n in G.nodes( data=True):
		if key == n[0]:
			for user in value:
				G.add_edge(user, n[0])
				staff_nodes.append(user)

pos = nx.spring_layout(G) # Set layout type to use for positioning Nodes

# Draw Nodes, Edges and Labels
nx.draw_networkx_nodes(G, pos, nodelist=org_nodes,
                       node_color='r', node_shape='s',
                       node_size=25).set_edgecolor('w')
nx.draw_networkx_nodes(G, pos, nodelist=staff_nodes,
                       node_color='g', node_shape='o',
                       node_size=10, with_labels=False)
nx.draw_networkx_edges(G, pos, edge_color='grey')
nx.draw_networkx_labels(G,pos, labels, label_pos=20, font_size=8)

#plt.axis('equal') # make things look a little more symmetrical


def histogram(roles):
	"""

	:param roles: dictionary with list as key value for university IDs
	:return: histogram bin
	"""
	plt.figure() # creates a new pyplot window
	bucket = {}
	for k, v in roles.items():
		bucket[k] = len(v)

	# plt.bar(range(len(bucket)), bucket.values(), align='center')
	pos = pl.arange(len(bucket))
	plt.barh(pos, bucket.values(), height=0.25)
	plt.yticks(pos, bucket.keys())

	plt.xlabel('Staff')
	plt.ylabel('Position')
	plt.title('Distribution of Positions')
	plt.gcf().subplots_adjust(bottom=0.08, left=0.6)



histogram(staff_bucket)



if __name__ == '__main__':
	plt.show()