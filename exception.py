## 2. Création de fonction comportant des modules de gestions des exceptions (5 points)

def factorielle():
  """
  cette fonction calcule le factorielle d'un nombre et gère les exceptions
  Entréé: n
  Sortie: calcule du factorielle 
  """
  print("Saisissez un nombre entier et nous allons calculer son factorielle  \n ")
  n=input()
  if(type(n)==str):
    print("Vous avez saisi une chaîne de caractère, mettez un nombre entier \n ")
    while(type(n==str)):
      try:
        n=int(input("Mettez un nombre entier \n"))
      except ValueError:
        print("Mettez un nombre entier \n")
  elif(type(n)==complex):
    print("Vous avez saisi un nombre complexe, mettez un nombre entier \n ")
    while(type(n==complex)):
      try:
        n=int(input("Mettez un nombre entier \n"))
      except ValueError:
        print("Mettez un nombre entier \n")
  elif(n<0):
    print("Vous avez mis un nombre négatif, saisissez un nombre entier positif \n ")
    while(type(n<0)):
      try:
        n=int(input("Mettez un nombre entier positive \n"))
      except ValueError:
        print("Mettez un nombre entier positive \n")
  elif(n>10**5):
    print("Vous avez saisi un grand nombre, mettez un nombre entre 0 et 10^3 au préalable \n ")
    while(type(n>10**5)):
      try:
        n=int(input("Mettez un nombre entier petit \n "))
      except ValueError:
        print("Mettez un nombre entie petit \n ")
  elif(n<10**(-5)):
    print("Vous avez choisi un nombre trop petit, saisissez un nombre entre 10^-2 et 10^3 au préalable \n ")
    while(type(n<10**(-5))):
      try:
        n=int(input("Mettez un nombre entier grand \n"))
      except ValueError:
        print("Mettez un nombre entier grand \n")
  elif(n==1 or n==1):
    return 1
  else:
   return n* factorielle(n-1)
print(factorielle())