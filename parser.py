from fuzzywuzzy import fuzz
from fuzzywuzzy import process
valid_roles = ['Australian National University', 'Vice Chancellor', 'Office of the Vice Chancellor',
			   'Alumni Relations and Philanthropy', 'Deputy Vice Chancellor Research',
			   'Pro Vice Chancellor Research and Research Training', 'Statistical Consulting Unit',
			   'Research Training', 'Pro Vice Chancellor Innovation', 'Technology Transfer Office',
			   'Business Development Research and Education','Research Services', 'Strategy and Policy',
			   'Research Infrastructure', 'Deputy Vice Chancellor Academic',
			   'Pro Vice Chancellor University Experience', 'Indigenous', 'Equity',
			   'Dean of Students', 'Pro Vice Chancellor Education and Global Engagement Standing Deputy',
			   'International Research and Education', 'ANU Online',
			   'Centre for Higher Education Learning and Teaching', 'Strategic Communications and Public Affairs',
			   'Curriculum Enrichment', 'Marketing', 'Student Recruitment and Admissions',
			   'Registrar Student Administration', 'Registrar Student Life', 'Academic Performance',
			   'Executive Directory Administration and Planning', 'Finance and Business Services',
			   'Human Resources', 'Facilities and Services', 'Information Technology Services',
			   'Planning and Performance Measurement', 'Service Improvement Group',
			   'Corporate Governance and Risk Office', 'Legal Office', 'University Librarian',
			   'Drill Hall Gallery', 'Dean ANU College of Arts and Social Science',
			   'ANU College of Arts and Social Sciences', 'Research School of Social Sciences',
			   'Research School of Humanities and the Arts', 'Dean ANU College of Asia and the Pacific',
			   'ANU College of Asia and the Pacific', 'Crawford School of Public Policy',
			   'Coral Bell School of Asia Pacific Affairs', 'School of Culture History and Language',
			   'Regulatory Institutions Network', 'The Australian Centre on China in the World',
			   'Research School of Asia and the Pacific', 'Dean ANU College of Business and Economics',
			   'ANU College of Business and Economics', 'Research School of Management',
			   'Research School of Finance Actuarial Studies and Applied Science',
			   'Research School of Accounting and Business Information Systems', 'Research School of Economics',
			   'Dean ANU College of Engineering and Computer Science',
			   'ANU College of Engineering and Computer Science', 'Research School of Engineering',
			   'Research School of Computer Science', 'Dean ANU College of Law', 'ANU College of Law',
			   'Faculty of Law', 'Dean ANU College of Medicine Biology and the Environment',
			   'ANU College of Medicine Biology and Environment', 'John Curtin School of Medical Research',
			   'ANU Medical School', 'Research School of Population Health', 'Research School of Biology',
			   'Research School of Psychology', 'Fenner School of Environment and Society',
			   'Dean ANU College of Physical and Mathematical Sciences',
			   'ANU College of Physical and Mathematical Sciences', 'Research School of Physics and Engineering',
			   'Research School of Earth Sciences', 'Research School of Chemistry',
			   'Research School of Astronomy and Astrophysics', 'Mathematical Sciences Institute',
			   'Australian National Centre for the Public Awareness of Science', 'Centre for Advanced Microscopy', ]

#check if role is a valid role by comparing with list of valid roles using fuzzy string matching.
def check_roles(roles):
	r=[]
	for role in roles:
		if len(role.replace(",","").replace(" ",""))>0: # clean up commas and spaces
			matched_role, score = process.extractOne(role, valid_roles)
			# print(matched_role)
			if score > 90: # if matched role has a score greater then 90, add the person to the list of people in role
				r.append(matched_role)
	return r







# read data pulled down and check if it is a valid role if it is add to dictionary where key is role and values are list of UID.
def parse_data(filename):
	role_members = {}
	file = open(filename,"r")
	content = file.read()
	for line in content.split("\n"):
		#check for empty list in data
		if len(line.split(",",1))>1:
			#get UID and remove any spaces and commas
			uid=line.split(",",1)[0].replace(" ","").replace("\n","")
			#get list of roles and remove backets, commads and string quotation marks
			roles=check_roles(line.split(",",1)[1].replace("[","").replace("]","").split("\'"))
			#append to dictionary if key already exists else create new entry in dictionary
			for role in roles:
				if role in role_members.keys():
					role_members[role].append(uid)
				else:
					role_members[role]=[uid]
	return role_members
