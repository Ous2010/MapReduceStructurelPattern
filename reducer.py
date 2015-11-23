#!/usr/bin/python

import sys
import csv

def reducer():
	# Tableau données post
    postValues = [] 
    # Tableau données user
	userValues = [] 
    userOld = None

    for line in sys.stdin:

        data = line.strip().split("\t")      
        if userOld and userOld != data[1]:
            userOld = data[1];
            if len(userValues) != 6 or len(postValues) != 10:
                continue
            fusion(userValues, postValues)

        userOld = data[1]
        if data[0] == "\"user\"":
          userValues = list(data)
        if data[0] == "\"post\"":
          postValues = list(data)
    if userOld != None:
        if len(userValues) == 6 and len(postValues) == 10:
            fusion(userValues, postValues)
			
#fusionner les résultats 
def fusion(userValues, postValues):
    
	# supprimer author_id
    del userValues[1] 
	# supprimer "user"
    del userValues[1] 
    # userValues  --> [reputation, gold, silver, bronze]

    auther_id = postValues[1]
	# supprimer author_id
    del postValues[1] 
	# supprimer "post"
    del postValues[1] 
	# ajouter authord_id au position 5
    postValues.insert(3, auther_id) 
    # post = [id, title, tagNames, author_id, nodeType, parentId, absParentId, addedAt, score]

    # afficher les résultats 
    print ''.join(postValues) + "\t" + "\t" . join(userValues)

reducer()
