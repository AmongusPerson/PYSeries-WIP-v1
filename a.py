from tkinter import *
root = Tk()
root.title("Hola")
root.geometry("500x500")

label_series = Label(root, text="Etiqueta 1")
label_series.place(relx=0.2, rely=0.1 , anchor=CENTER)
label_series2 = Label(root, text="Etiqueta 2")
label_series2.place(relx=0.2, rely=0.2 , anchor=CENTER)
label_series3 = Label(root, text="Etiqueta 3")
label_series3.place(relx=0.2, rely=0.3 , anchor=CENTER)
label_series3 = Button(root, text="Boton 1")
label_series3.place(relx=0.2, rely=0.4 , anchor=CENTER,)
root.mainloop()