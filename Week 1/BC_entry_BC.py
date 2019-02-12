# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:39:35 2019

@author: Olivier
"""


input=str('01941e985075825e09de53b08cdd346bb67075ef0ce5c94f98853292d4bf94c10d010000006b483045022100ab44ef425e6d85c03cf301bc16465e3176b55bba9727706819eaf07cf84cf52d02203f7dc7ae9ab36bead14dd3c83c8c030bf8ce596e692021b66441b39b4b35e64e012102f63ae3eba460a8ed1be568b0c9a6c947abe9f079bcf861a7fdb2fd577ed48a81Feffffff')


#on a 4 types d'entrees
#trois ont une longueur definie
#on va les retriever
#Le hash de la transaction passée où sont les bitcoins à dépenser (sur 32 octets*8bites)
sequence_initiale=input[:16-1]
#L’index de la sortie (output) de cette transaction concernée (sur 4 octets *8)
sequence_sortie=input[16:16+2]
#le dernier champ: Séquence (sur 4 octets) 
sequence_final=input[-2:]
#le remaining ScriptSig, essentiellement la signature et les informations qui correspondent aux conditions de dépense inscrites dans la transaction de départ (voir ci-dessous Script). 
#Ce champ commence par un varInt annonçant la longueur du champ, 
#puis le Script
ScriptSig=input[19:-3]
print(ScriptSig)
