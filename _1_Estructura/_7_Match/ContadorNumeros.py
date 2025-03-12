from email.quoprimime import header_check
import sys
if __name__ == '__main__':
    lista=[1,2,5,1,5,4,5,9,1,80,10,10,-1,10,4,2,5,30,6,3,7,9,8,6,4,9,10,1,3]
    totales=[0,0,0,0,0,0,0,0,0,0]
    adoptados:int=0
    #se tiene que hacer global la variable para que funcione con los dos for
    for elemento in lista:
        totales[2]+=1
        match elemento:
            case 1: totales[0]+=1
            case 2: totales[1]+=1
            case 3: totales[2]+=1
            case 4: totales[3]+=1
            case 5: totales[4]+=1
            case 6: totales[5]+=1
            case 7: totales[6]+=1
            case 8: totales[7]+=1
            case 9: totales[8]+=1
            case 10:totales[9]+=1
            case _: adoptados+=1

    i:int=1
    for n in totales:

        print(f" La cantidad de numeros {i}, son :{n}")
        i+=1

    """j:int=1
    for j in adoptados:
        print (f"La cantidad de adoptados es: {j}")
        j+=1"""