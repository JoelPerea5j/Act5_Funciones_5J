print("Ejemplo de funciones")
#Declarando Funciones
def zy():
 print("Alguien Uso la funcion zy")

def chat(msg):
 print(f"Chat {msg}")

def elcomenta(mgs):
 print(f"Chat el: {mgs}")

def escribenombre(ap,n):
 print(f"Tu nombre completo es:{n} {ap}") 

def suma(a,b):
 s=a+b
 return s

def resta(c,d):
 r=c-d
 return r

def multi(e,f):
 t=e*f
 return t

def divicion(g,h):
 i=g/h
 return i

#Llamadas a funciones
zy()
chat("Que bonito es copiar y pegar")
elcomenta("Pero que mal no seber que hacer")
escribenombre("Perea","Joel Alberto")
print("Operacion suma basicas")
c1=int(input("Ingresa un numero "))
c2=int(input("Ingresa otro numero "))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")

print("Operacion Resta basicas")
c3=int(input("Ingresa un numero "))
c4=int(input("Ingresa otro numero "))
dameresta=resta(c3,c4)
print(f"La resta de {c3} - {c4} = {dameresta}")

print("Operacion Multiplicacion basicas")
c5=int(input("Ingresa un numero "))
c6=int(input("Ingresa otro numero "))
damemulti=multi(c5,c6)
print(f"La multiplicacion de {c5} * {c6} = {damemulti}")

print("Operacion Divicion basicas")
c7=int(input("Ingresa un numero "))
c8=int(input("Ingresa otro numero "))
damedivicion=divicion(c7,c8)
print(f"La divicion de {c7} / {c7} = {damedivicion}")