from random import sample
def contar(lista):
  if(len(lista)==0):
    return 0
  else:
      if(lista[0][0]=='A'):
          return 1+contar(lista[1:])
      if (lista[0][0]=='J' or lista[0][0]=='Q' or lista[0][0]=='K'):
          return 10+contar(lista[1:])
      else:
          return lista[0][0]+contar(lista[1:])
        
def contaras(lista):
    if(len(lista)<=0):
        return 0
    if contar(lista)>11:
        return contar(lista)
    else:
        if (lista[0][0] == 'A'):
            return contar(lista)+10
        else:
            return lista[0][0]+contaras(lista[1:])
        
def creadorbaraja():
    return sample([(x,y)for x in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']for y in ['DIAMANTES','TREBOLES','PICAS','CORAZONES']], 52)

    
def juego(listaJ, listaC, lista, JC):
    if(len(listaJ)==0 and len(listaC)==0):
        repartirIni(listaJ, listaC, lista, JC)
        return "      FIN DEL JUEGO"
    else:
        print("jugador: ",contaras(listaJ))
        print(listaJ)
        print("Casa: ")
        print(listaC[0])
        print("")
        print("")
        if(JC==True and contaras(listaJ)<=21):
            if(input("Desea otra carta: ")!='no'):
                print("")
                return repartirIni(listaJ,listaC,lista, JC)
    if(contaras(listaC)<contaras(listaJ) and contaras(listaJ)<=21):
        return repartirIni(listaJ,listaC,lista, False)
    else:
        print("//////// RESULTADOS////////")
        print("")
        print("Mano del Jugador:   ",contaras(listaJ))
        print(listaJ)
        print("Mano de laCasa:      ",contaras(listaC))
        print(listaC)
        print("")
        if(contaras(listaC)>21 and contaras(listaJ)<=21):
            print("     Gana El Jugador :3 ")
        elif((contaras(listaJ)<contaras(listaC) and contaras(listaC)<=21) or (contaras(listaJ)>21 and contaras(listaC)<=21)):
            print("     Gana La Casa :( ")
        elif(contaras(listaJ)==contaras(listaC) and contaras(alistaJ)<=21):
            print("     Es Un Empate :/ ")
        print("/------------------------------/")

def repartirIni(listaJ, listaC, lista, JC):
    if (len(lista)==52):
        return juego(listaJ+[lista[0]]+[lista[1]],listaC+[lista[2]]+[lista[3]],lista[4:],JC)
    elif(len(lista)!=52 and JC==True):
        return juego(listaJ+[lista[0]],listaC,lista[2:],JC)
    elif(len(lista)!=52 and JC==False):
        return juego(listaJ,listaC+[lista[0]],lista[2:],JC)

print("")
print("")
print("")
print("Empezo el juego:")
print("")
print(juego([],[],creadorbaraja(),True))
