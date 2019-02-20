# -*- coding: utf-8 -*-

"""
	Initialement, un fichier "correction_drive" comportait des bouts de codes à executer 
	un après l'autre dans un terminal.
"""
import pdb
import csv
#------------------------ mettre entre "" --------------------------------
with open('start.csv', 'r') as infile, open('quoted.csv', 'w') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter=';', quoting=csv.QUOTE_ALL)
    for line in reader:
        writer.writerow(line)
#-------------------------------------------------------------------------

#------------------------ ordonner les colonnes et ajouter les valeurs par défaut ------------
d = {'ID_CLIENT':'', 'MARQUE':'', 'MODELE':'', 'NOM':'', 'ANNEE':0, 'KM':0, 'VILLE':'', 'CP':'', 'PRIX':0, 'CARBURANT':'', 'COULEUR':'', 'TYPE':'', 'SITE':'', 'DEPARTEMENT':'', 'ANNONCE_LINK':'', 'ANNONCE_DATE':'0000-00-00 00:00:00', 'MOIS':0, 'EMAIL':'', 'CONTACT':'', 'TELEPHONE':'', 'TELEFAX':'', 'GARAGE_ID':'', 'TELEPHONE_2':'', 'GARAGE_NAME':'', 'CYLINDRE':'', 'COUNTRY':0, 'ADRESSE':'', 'CONTACT_PRENOM':'', 'CONTACT_NOM':'', 'OPTIONS':'', 'BOITE':'', 'PORTE':'', 'PLACE':'', 'CARROSSERIE':'', 'PHOTO':0, 'TELEPHONE_3':'', 'TELEPHONE_4':'', 'PUISSANCE':'', 'PROVINCE':'', 'LITRE':0.0, 'IMMAT':'', 'NB_VITESSE':0, 'WEBSITE':'', 'VN_IND':0, 'SIRET':'', 'VIN':''}
res=[]
with open('quoted.csv','r') as f:
    reader=csv.reader(f,delimiter=';')
    row0 = next(reader)
    for key in d.keys():
        if key not in row0:
            row0.append(key)
    res.append(row0)
    for row in reader:
            if row is not row0:
                item=[]
                for element in row:
                    item.append(element)
                for i in range(len(row0)-len(row)):
                    item.append('')
                res.append(item)
    for key in d.keys():
        index=row0.index(key)
        for rows in res:
            if len(str(rows[index]))==0 or rows[index]=='None':
                rows[index]=d[key]
with open('begin.csv','w') as ff:
    writer=csv.writer(ff,delimiter=';', quoting=csv.QUOTE_ALL)
    for rows in res:
        writer.writerow(rows)
    ff.close()
#-----------------------------------------------------------------------------------------------

#--------------------------- correctifs des valeurs crawlés (règles et mise en forme) ----------
import re
res=[]
with open('begin.csv','r') as f:
    reader=csv.reader(f,delimiter=';')
    row0 = next(reader)
    res.append(row0)
    for row in reader:
        if row is not row0:
            item=[]
            for element in row:
                item.append(element)
            res.append(item)
            #pdb.set_trace()
    for rows in res:
        if rows is not row0:
            rows[27]=0
            rows[20]=re.findall(r'[0-9\.]+', str(rows[20])) # trouver les chiffres dans une chaine "bonnjour404bon--->404"  il peut etre vide 
            if rows[20]!=[]: # iil peut etre vide donc il ajouter cette instruction
                rows[20]=rows[20][0]
                rows[20]=int(rows[20].replace('.', ''))
            l=re.findall(r'[0-9]+\.?[0-9]*', str(rows[24]))
            if len(l)==2:
                rows[24]=float(l[1])
            elif len(l)==1:
                rows[24]=float(l[0])
            else:
                rows[24] = 0.0
            if rows[24] > 9.9:
                rows[24] = 0.0
            #rows[34]=rows[36]
            rows[36]=''
            rows[38]='0'
            l=re.findall(r'[0-9]+[\.0-9]*', str(rows[19]))
            if len(l)==1:
                rows[19]=l[0]
            else:
                rows[19] = 0
            rows[19]=int(str(rows[19]).replace('.', ''))
            #pdb.set_trace()

with open('end.csv','w') as ff:
    writer=csv.writer(ff,delimiter=';', quoting=csv.QUOTE_ALL)
    for rows in res:
        writer.writerow(rows)
    ff.close()
#----------------------------------------------------------------------------------------------
