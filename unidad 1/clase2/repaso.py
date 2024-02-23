from tkinter import Frame, Tk
from tkinter.messagebox import askyesno

def evento_dar_click(evento):
    frame.focus_set()
    print("Di clik en las coordenadas: ", evento.x, evento.y)

def evento_presionar_tecla(evento):
    print("Presione la tecla: ", repr(evento.char))

def el_usuario_quiere_salir():
    if askyesno('Salir de la aplicación', '¿Seguro que quieres salir de la aplicación?'):
        principal.destroy()

principal = Tk()
principal.title('Prueba eventos')

frame = Frame(principal, width=500, height=500)
frame.bind("<Button-1>", evento_dar_click)
frame.bind("<Key>", evento_presionar_tecla)

frame.pack()

principal.protocol('WM_DELETE_WINDOW', el_usuario_quiere_salir)
principal.mainloop()
