class Tree(object):
  def __init__(self,l,iz,der):
    self.label=l
    self.left=iz
    self.right=der


#formulas
A=Tree("p",None,None)#p
A1=Tree("-",None,A)#-p
B=Tree("q",None,None)#q
B1=Tree("-",None,B)#-q
C=Tree("r",None,None)#r
C1=Tree("-",None,None)#-r
D=Tree("O",B,C)#qor
D1=Tree("Y",A,D)#(pY(qor))a
D2=Tree("Y",A,B)#(pyq)
D3=Tree("Y",A,C)#(pyr)
D4=Tree("O",D2,D3)#((pyq)o(pyr))a
D5=Tree("O",A,B)#(poq)b
D6=Tree("Y",A1,B1)#(-py-q)
D7=Tree("-",None,D6)#-((-py-q))b
D8=Tree("O",A1,B1)#(-po-q)
D9=Tree("-",None,D8)#(-(-po-q))
D10=Tree(">",A,B)#p->q
D11=Tree("O",A1,B)#-poq








I={'p':0,'q':1,'r':1,'s':0}
#luego I['P']=0

letrasProposicionales=['p','q','r']
interps=[]#lista de todas las posibles interpretaciones
aux={}#primer interpretacion

for i in letrasProposicionales:
    aux[i]=1 #todas las interpretaciones comienzan en verdadero

interps.append(aux)#la incluimos en interps


for i in letrasProposicionales:
    interps_aux=[a for a in interps]

    for j in interps_aux:
        aux1={}
        for b in letrasProposicionales:
            if i==b:
                aux1[b]=1-j[b]
            else:
                aux1[b]=j[b]
        interps.append(aux1)



#implementar la funcion vi
    
def VI(arb,I):
	if arb.right==None:
    		return I[arb.label]
	elif arb.label=='-':
    		if VI(arb.right,I)==1:
        		return 0
    		else:
        		return 1
	elif arb.label=='Y':
    		if(VI(arb.left,I)==1 and VI(arb.right,I)==1):
        		return 1
    		else:
        		return 0
	elif arb.label=='O':
    		if(VI(arb.left,I)==1 or VI(arb.right,I)==1):
       			return 1
    		else:
       			return 0
	elif arb.label=='>':
       		if(VI(arb.left,I)==0):
           		return 1
       		else:
           		return VI(arb.right,I)
	elif arb.label=='<>':
       		if(VI(arb.left,I)==VI(arb.right,I)):
          		return 1
       		else:
          		return 0


def Equivalencia(arb,arb2):
    for i in interps:
        j=VI(arb,i)
        k=VI(arb2,i)
        if j!=k:
            return False
    return True		


#probamos la primera formula 

#a
print(Equivalencia(D1,D4),"este es el 5a")

#b

print(Equivalencia(D5,D7),"este es el 5b")

#c

print(Equivalencia(D2,D9),"este es el 5c")


#d
print(Equivalencia(D10,D11),"este es el 5d")


  
    

               
