"""Buscador del número mayor"""
n=int(input("Tamaño del arreglo\n"))
nvalores=[]
for i in range (0,n):
    res=int(input(""))
    nvalores.append(res)
mayor=0
for i in range(0,n):
    if(nvalores[i]>nvalores[mayor]):
        mayor=i
print("El número mayor es: ",nvalores[mayor])