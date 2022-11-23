from tkinter import *

from tkinter import ttk

''' Cores '''

cor1 = "#444466" # preto 

cor2 = "#feffff" # branco 

cor3 = "6f9fbd" # azul 

cor4 = "#38576b" # valor 

cor5 = "#403d3d" # letra 

cor5 = "#ef5350" # vermelho 


''' Criando janela '''

janela = Tk()

janela.title('')

janela.geometry('550x510')

janela.configure(bg=cor2)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)

style.theme_use("clam")

''' Criando frame '''

frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)


''' Nome do pokemon '''

poke_name = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER, font=('fixedsys 20'), bg=cor2, fg=cor1)
poke_name.place(x=12, y=15)



''' Tipo do pokemon '''

poke_tipo = Label(frame_pokemon, text='Elétrico', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=cor2, fg=cor1)
poke_tipo.place(x=12, y=50)






janela.mainloop()
