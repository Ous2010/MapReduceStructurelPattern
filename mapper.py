#!/usr/bin/python
import sys
import csv

def mapper():
    fileReader = csv.reader(sys.stdin, delimiter='\t')
    fileWriter = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

	#Début lecture du fichier forum_nodes et forum_users
    for line in fileReader:
		#Tableau vide pour stocker les données : author_id, id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score  
        values = []
		#Test 
        if len(line) == 5: 
          # user_ptr_id, reputation, gold, silver, bronze 
          values = ["user", line[0], line[1], line[2], line[3], line[4]]
		#Début lecture du fichier forum_nodes	
        if len(line) == 19: # line comes from forum_node, just pick the ones needed
          
		  # author_id, id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score  
          values = ["post", line[3], line[0], line[1], line[2], line[5], line[6], line[7], line[8], line[9]]

        fileWriter.writerow(values)
mapper()
