# Sample code which will use the sample University Hieracrchy.py's hierachy structured dictionary.
import networkx as nx
import matplotlib.pyplot as plt

starter = {'Australian National University':
            {'Vice Chancellor': {
                 'Office of the Vice Chancellor': {},
                 'Alumni Relations and Philanthropy': {},
                 'Deputy Vice Chancellor Research': {
                     'Pro Vice-Chancellor Research and Research Training': {
                         'Statistical Consulting Unit': {},
                         'Research Training': {'users': ['u5318579', 'u1234567']},
                     },
                 },
                },
             },
           }

starter2 = {'Australian National University':
             {'Vice Chancellor': {
                 'Office of the Vice Chancellor': {},
                 'Alumni Relations and Philanthropy': {},
                 'Deputy Vice Chancellor Research': {
                     'Pro Vice-Chancellor Research and Research Training': {
                         'Statistical Consulting Unit': {},
                         'Research Training': {},
                     },
                     'Pro Vice-Chancellor Innovation': {
                         'Technology Transfer Office': {},
                         'Business Development Research and Education': {}
                     },
                     'Research Services': {},
                     'Strategy and Policy': {},
                     'Research Infrastructure': {},
                 },
                 'Deputy Vice Chancellor Academic': {
                     'Pro Vice-Chancellor University Experience': {
                         'Indigenous': {},
                         'Equity': {},
                         'Dean of Students': {},
                     },
                     'Pro Vice-Chancellor Education and Global Engagement Standing Deputy': {
                         'International Research and Education': {},
                         'ANU Online': {},
                         'Centre for Higher Education Learning and Teaching': {},
                         'Strategic Communications and Public Affairs': {},
                         'Curriculum Enrichment': {},
                         'Marketing': {},
                     },
                     'Student Recruitment and Admissions': {},
                     'Registrar Student Administration': {},
                     'Registrar Student Life': {},
                     'Academic Performance': {},
                 },
                 'Executive Directory Administration and Planning': {
                     'Finance and Business Services': {},
                     'Human Resources': {},
                     'Facilities and Services': {},
                     'Information Technology Services': {'users': ['u5318579', 'u1234567']},
                     'Planning and Performance Measurement': {},
                     'Service Improvement Group': {},
                     'Corporate Governance and Risk Office': {},
                     'Legal Office': {},
                     'University Librarian': {},
                     'Drill Hall Gallery': {},
                 },
                 'Dean ANU College of Arts and Social Science': {
                     'ANU College of Arts and Social Sciences': {
                         'Research School of Social Sciences': {},
                         'Research School of Humanities & the Arts': {}
                     },
                 },
                 'Dean ANU College of Asia and the Pacific': {
                     'ANU College of Asia and the Pacific': {
                         'Crawford School of Public Policy': {},
                         'Coral Bell School of Asia Pacific Affairs': {},
                         'School of Culture, History and Language': {},
                         'Regulatory Institutions Network': {},
                         'The Australian Centre on China in the World': {},
                         'Research School of Asia & the Pacific': {},

                     },
                 },
                 'Dean ANU College of Business and Economics': {
                     'ANU College of Business and Economics': {
                         'Research School of Management': {},
                         'Research School of Finance Actuarial Studies and Applied Science': {},
                         'Research School of Accounting & Business Information Systems': {},
                         'Research School of Economics': {}

                     },
                 },
                 'Dean ANU College of Engineering and Computer Science': {
                     'ANU College of Engineering and Computer Science': {
                         'Research School of Engineering': {},
                         'Research School of Computer Science': {},
                     }
                 },
                 'Dean ANU College of Law': {
                     'ANU College of Law': {
                         'Faculty of Law': {},
                     },
                 },
                 'Dean ANU College of Medicine Biology and the Environment': {
                     'ANU College of Medicine Biology and Environment': {
                         'John Curtin School of Medical Research': {},
                         'ANU Medical School': {},
                         'Research School of Population Health': {},
                         'Research School of Biology': {},
                         'Research School of Psychology': {},
                         'Fenner School of Environment and Society': {},
                     }
                 },
                 'Dean ANU College of Physical and Mathematical Sciences': {
                     'ANU College of Physical and Mathematical Sciences': {
                         'Research School of Physics and Engineering': {},
                         'Research School of Earth Sciences': {},
                         'Research School of Chemistry': {},
                         'Research School of Astronomy and Astrophysics': {},
                         'Mathematical Sciences Institute': {},
                         'Australian National Centre for the Public Awareness of Science': {},
                         'Centre for Advanced Microscopy': {},
                     },
                 },


              }
              }
    }

organization_edges = []  # going to build a list of tuples made up of key and value
staff_edges = []  # to be filled with list of tuples made up of staff and their parent
G = nx.Graph() # create networkx graph

def staff_edge_maker(node, parent):
    """

    :param node:
    :param parent:
    :return:
    """
    for uid in node:
        staff_edges.append((parent, uid))


def walker(node, parent=None):
    """
    function walks the input dictionary,
    if the key of the parent dictionary is know it will append both the parent key and each dictionary key
    as a tuple to the organization_edges list e.g. (ParentKey, Localkey0), (ParentKey, Localkey1)

    :param node: dictionary
    :param parent: defaults to None to allow for recursive use of the walker function.
    :return: None
    """

    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, dict):
                if parent:
                    organization_edges.append((parent, k))
                    G.add_edge(parent, k)
                walker(v, k)
            elif isinstance(v, list):
                if parent:  # if parent is known pass it in
                    for staff in v:
                        staff_edge_maker(staff, parent)
                        G.add_edge(staff, parent)

walker(starter2)
print(organization_edges)
print(staff_edges)
x = True

nx.draw(G, with_labels=True, font_size=8)
while x:
    plt.show()

