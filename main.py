

def printjus(cosa):
  print(str(cosa).rjust(ANCHURA))

def multiplica(factor1,factor2):
 global ANCHURA
 ANCHURA=(len(str(factor1*factor2)))+2
 printjus("")
 printjus((factor1))
 printjus("x"+str(factor2))
 if factor1>factor2:
  nrayas=len(str(factor1))
 else:
  nrayas=len(str(factor2))+1
 printjus("-"*nrayas)
 espacios=0
 for i in str(factor2)[::-1]:
#  printjus(int(i)*factor1)
  printjus(str(int(i)*factor1)+" "*espacios)
  espacios=espacios+1
 printjus("-"*len(str(factor1*factor2))) 
 printjus(factor1*factor2)



def resta(minuendo,sustraendo):
 print("")
 if minuendo>sustraendo:
  anchura=(len(str(minuendo)))+2 
 else:
  anchura=(len(str(sustraendo)))+2 
 print(str(minuendo).rjust(int(anchura)))
 print(" -")
 print(str(sustraendo).rjust(int(anchura)))
 anchu=anchura=anchura-2
 print("  "+"-"*anchu)
 if minuendo>sustraendo:
  anchura=(len(str(minuendo)))+2
 else:
  anchura=(len(str(sustraendo)))+2
 print(str(minuendo-sustraendo).rjust(anchura))



def suma(sumandos):
 print("")
 total=0
 for a in range(len(sumandos)):
  total=total+sumandos[a]
 for i in range(len(sumandos)-1):
  print(str(sumandos[i]).rjust(len(str(total))+2))
 print(" +"+str(sumandos[-1]).rjust(len(str(total))))
 print("  "+"-"*len(str(total)))
 print("  "+str(total).rjust(len(str(total))))

def division(dividendo , divisor ):

    dividendo = str(dividendo)
    divisor=str(divisor)

    





    #print(dividendo+color.UNDERLINE+"|"+divisor+color.END)
    print(dividendo+"|"+divisor)
    print(" ".rjust(len(dividendo))+"-----")

    col=len(divisor)
    resto=dividendo[0:len(divisor)]
    resultado=True

    while True:

        while int(resto)<int(divisor) and col<len(dividendo):
            resto=resto+dividendo[col]
            col+=1
        resto=str(int(resto)%int(divisor))
        while int(resto)<int(divisor) and col<len(dividendo):  #bajo uno
            resto=resto+dividendo[col]
            col+=1
        if resultado:
            cociente=str(int(int(dividendo)/int(divisor)))
            print(resto.rjust(col)+cociente.rjust(len(dividendo)-col+len(cociente)+1))
            resultado=False
        else:
            print(resto.rjust(col))
        if col>=len(dividendo) and int(resto)<int(divisor):
            break








#**************************************
#*              test                  *
#**************************************
def test():
  print("Iván López -->Semana Santa 2019")
  print("")
  print("multiplica(factor1,factor2)")
  print("Escribe las mutiplicaciones como en el cole")
  print("Ej:multiplica(124,35)")
  multiplica(124,35)
  print("")

  print("")
  print("resta(minuendo,sustraendo)")
  print("Escribe las restas como en el cole")
  print("Ej:resta(1587,342)")
  resta(1587,342)
  print("")

  print("")
  print("suma([sumando1,sumando2,...])")
  print("Escribe las sumas como en el cole")
  print("Ej:suma(1587,342,123,9879)")
  suma([1587,342,123,9879])
  print("")

test()
