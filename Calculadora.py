from tkinter import *
ventana =Tk()
ventana.title("Calculadora")

#Entrada
e_texto= Entry(ventana, font=("Calibri "))
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#Botones 
boton1=Button(ventana, text="1", width=5, height=2)
boton2=Button(ventana, text="2", width=5, height=2)
boton3=Button(ventana, text="3", width=5, height=2)
boton4=Button(ventana, text="4", width=5, height=2)
boton5=Button(ventana, text="5", width=5, height=2)
boton6=Button(ventana, text="6", width=5, height=2)
boton7=Button(ventana, text="7", width=5, height=2)
boton8=Button(ventana, text="8", width=5, height=2)
boton9=Button(ventana, text="9", width=5, height=2)
boton0=Button(ventana, text="0", width=13, height=2)

boton_Borrar=Button(ventana, text="AC", width=5, height=2)
boton_Parentesis1=Button(ventana, text="(", width=5, height=2)
boton_Parentesis2=Button(ventana, text=")", width=5, height=2)
boton_Punto=Button(ventana, text=".", width=5, height=2)

boton_Div=Button(ventana, text="/", width=5, height=2)
boton_Mult=Button(ventana, text="*", width=5, height=2)
boton_Suma=Button(ventana, text="+", width=5, height=2)
boton_Resta=Button(ventana, text="-", width=5, height=2)
boton_Igual=Button(ventana, text="=", width=5, height=2)

#Agregar botones en pantalla 
boton_Borrar.grid(row= 1, column=0, padx=5, pady=5)
boton_Parentesis1.grid(row= 1, column=1, padx=5, pady=5)
boton_Parentesis2.grid(row= 1, column=2, padx=5, pady=5)
boton_Div.grid(row= 1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_Mult.grid(row=2, column=3, padx=5, pady=5)


boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_Suma.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_Resta.grid(row=4, column=3, padx=5, pady=5)


#boton.grid(row=, column=, padx=, pady=)
#boton.grid(row=, column=, padx=, pady=)
#boton.grid(row=, column=, padx=, pady=)
#boton.grid(row=, column=, padx=, pady=)


ventana.mainloop()