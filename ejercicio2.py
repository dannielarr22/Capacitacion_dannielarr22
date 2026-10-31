"""Detector de palíndromo"""
def espalindromo(frase):
    res=True
    lim=frase.lower().replace(" ","")
    for i in range(0,len(lim)):
         if(lim[i]!=lim[-1-i]):
             res=False
             break
    print("Es Palindromo: ", res)
fraseusuario=input("Ingresa la frase\n")
espalindromo(fraseusuario)