class tree(object):
  def __init__(self,l,iz,der):
    self.label=l
    self.left=iz
    self.right=der

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
print ("Interpretaciones:")
for i in interps:
    

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
            if(VI(arb.left,I)==1 and VI(a.right,I)==1):
                return 1
            else:
                return 0
        elif arb.label=='O':
            if(VI(arb.left,I)==0 or VI(arb.right,I)==0):
               return 1
            else:
               return 0
        elif arb.label=='>':
               if(VI(arb.left,I)==0 or VI(arb.right,I)==0):
                   return 1
               else:
                   return 0
        elif arb.label=='<>':
               if(VI(arb.left,I)==VI(arb.right,I)):
                  return 1
               else:
                  return 0


def Equivalencia(arb,arb2,):
    for i in interps:
        j=VI(arb,i)
        k=VI(arb2,i)
        if j!=k:
            return False
    return True
    
    
           
               
