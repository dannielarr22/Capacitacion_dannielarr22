"""Calculadora de propinas"""
cuenta=float(input("Total de la cuenta: "))
porc_propina=int(input("% propina: "))
totalpropina=cuenta*(porc_propina/100)
totalapagar=cuenta+totalpropina
print("Propina: ",totalpropina)
print("Total a pagar: ",totalapagar)