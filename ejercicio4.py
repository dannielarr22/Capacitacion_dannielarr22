"""Sucesión de fibonacci"""
n=int(input("Ingresa el total de elementos de la sucesión de fibonacci a mostrar:\n"))
numsucesion=0
ant1=0
ant2=1
res=""
for i in range(0,n):
    if(i>0):
        numsucesion=ant1+ant2
        res+=","
    res+=str(numsucesion)
    ant1,ant2=ant2,numsucesion
print(res)