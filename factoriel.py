## implémentation de la fonction factorielle

def factorielle(n):
  """
  cette fonction calcule le factorielle d'un nombre
  Entréé: n
  Sortie: calcule du factorielle 
  """
  if(n==1 or n==1):
    return 1
  else:
   return n* factorielle(n-1)
print(factorielle(5))