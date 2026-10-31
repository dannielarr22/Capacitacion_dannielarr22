"""Validador de contraseña"""
def essegura(contra):
    condicion_long=False
    condicion_num=False
    condicion_letraMayus=False
    long=len(contra)
    if(long>=8):
        condicion_long=True
    for i in contra:
        if (i.isdigit()):
            condicion_num=True
            break
    for j in contra:
        if(j.isupper()):
            condicion_letraMayus=True
            break
    if(condicion_long and condicion_num and condicion_letraMayus):
        print("Contraseña Valida")
    if(condicion_long!=1):
        print("Menor a 8 Caracteres")
    if(condicion_num!=1):
        print("Faltó un número")
    if(condicion_letraMayus!=1):
        print("No contiene mayusculas")
contra=str(input("Contraseña: "))
essegura(contra)