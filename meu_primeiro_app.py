import time 

def space ():
    print(" ================ ")
    print(" ")
    time.sleep(2)


def space2 ():
    print("")
    print(" ================ ")

def bar():
    print("")

space()
print(" Colégio Paula Feres ")
space2()

bar()
print(" Olá aluno, tudo certo com você? ")
space2()

bar()
condiction=str(input("Deseja saber se foi aprovado? [s/n]: ")).upper()
space2()

if condiction == "S":
    faltas=int(input("Digite a quantidade de faltas: "))
    bar()
    media=float(input("Digite sua média: "))

    if faltas <= 5 and media >= 7:
         space()
         print(" Parabéns aluno! Você foi Aprovado. ")
         space2()

    elif faltas > 5 and media <= 10:
         space()
         print("Como suas faltas", faltas, "faltas", "você foi Reprovado. ")

    else:
         space()
         print("Como sua média foi", media, "você foi Reprovado. ")

else:
    space()
    print("Ok então, tenha um bom dia. ")