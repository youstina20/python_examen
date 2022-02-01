## Création de fonctions mathématiques sur python

## Implémentation de la fonction polynomiale 

def polynomiale(x):
  """
  Cette fonction calcule le polynome x^3-1,5x^2-6x+5
  Entrée: x de type int
  Sortie: calcule du polynome type double 
  """
  return(x**(3)-1.5*x**(2)-(6*x)+5)
print(polynomiale(5))