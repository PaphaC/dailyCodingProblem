# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

liste=[10, 15, 3, 7]
k=17
j=21
isKIn=False
isJIn=False

for i in range(0,len(liste)):
    if k-liste[i] in liste:
      isKIn=True
    if j-liste[i] in liste:
      isJIn=True

print( "Can 17 be made with the list : " + str(isKIn) )
print( "Can 21 be made with the list : " + str(isJIn) )