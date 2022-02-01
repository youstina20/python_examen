## implémentation de la fonction de Fibonnaci

def fibonnaci():
  """
 Cette fonction calcule la suite de Fibonnaci de n
 Entrée: n de type int 
 Sortie: la suite de fibonnaci
  """

  U0= 0
  U1= 1
  n=int(input("Entrez un nombre \n"))
  print("La suite de Fibonnachi est : \n")
  print(U0,",", U1, end=", ") 
  for i in range(2,n):
    Un =U0+U1
    print(Un," ", end=", ")
    U0=U1
    U1=Un
  return ""
print(fibonnaci())