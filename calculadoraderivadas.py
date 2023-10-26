#------------------------------------------importando las librerias-----------------------------
from tkinter import *
from sympy import diff,symbols,parse_expr
#-------------------------------------------------creando mi raiz--------------------------------
raiz=Tk()
#----------------------------------------configuaracion de mi raiz-------------------------------------
raiz.title("Calculadora de Derivadas")
raiz.geometry("650x350")
raiz.config(bg="yellow")
raiz.config(bd=45)
raiz.config(relief="groove")
#---------------------------------------funcion para derivar------------------------------------
def calcular_derivada():
    try: 
        x = symbols('x')
       
        Funcion_A_derivar = cuadrotextofunc.get()
        f = parse_expr(Funcion_A_derivar)
        derivada = diff(f, x)
        cuadrotextoresultado.delete(0, END)  
        cuadrotextoresultado.insert(0, derivada)
    except:
        cuadrotextoresultado.delete(0, END)  
        cuadrotextoresultado.insert(0, "Ingrese una función válida")
#---------------------------------------configuaracion de mi frame-------------------------------------------------
miframe=Frame(raiz,width=500, height=300)
miframe.config(bg="yellow")
#-----------------------------------mis label---------------------------------------------------------
Label(miframe, text="Calculadora de Derivadas 3k",fg="red" , font=("Comic Sans MS",18),bg="yellow").place(x=100,y=25)
calcular=Label(miframe,text="Ingrese la función: ", fg="black", font=("Comic Sans MS",14),bg="yellow")
calcular.place(x=10,y=75)
resultado=Label(miframe,text="La Derivada de la función es:", fg="black", font=("Comic Sans MS",14),bg="yellow")
resultado.place(x=10,y=110)
creditos=Label(miframe,text="developed by Abel_Bravila \n desing by Dark 🧐​ ", fg= "gray",font=("Comic Sans MS",15),bg="yellow")
creditos.place(x=5,y=200) 

#----------------------------------mis cuadros de texto -----------------------------------------------------------
cuadrotextofunc=Entry(miframe)
cuadrotextofunc.place(x=200,y=80)

cuadrotextoresultado=Entry(miframe)
cuadrotextoresultado.place(x=280,y=115)

#---------------------------------------------------------Mi boton---------------------------------------------------
botoncalcular=Button(miframe,  text="Calcular",command=calcular_derivada)
botoncalcular.place(x=300,y=150)
botoncalcular.config(cursor="pirate")
#-------------------------------------------para empaquetar mi frame con mi raiz:)-------------------------------------
miframe.pack()

#raiz.config(cursor="hand2")
#----------------------------------------mainloop para que este actualizando mi raiz---------------------------------
raiz.mainloop()