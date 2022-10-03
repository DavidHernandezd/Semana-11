from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
from tkinter import Button, Place, Radiobutton, Tk, Label, filedialog, IntVar


def cargar():
    archivo = filedialog.askopenfilename()
    foto2 = Image.open(archivo)
    reducida2 = foto2.resize((250,200), Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(reducida2)
    if x.get() == 1:
        bn = foto2.convert("L")
        bn.show()
        bn.save("Resultado.jpg")
        lb2.configure(image=render2)
        lb2.image=render2
    elif x.get() == 2:
        desenfocar = foto2.filter(ImageFilter.BLUR)
        desenfocar.show()
        desenfocar.save("Resultado.jpg")
        lb2.configure(image=render2)
        lb2.image=render2
    elif x.get() == 3:
        contorno = foto2.convert("L")
        contorno = contorno.filter(ImageFilter.FIND_EDGES)
        contorno.show()
        contorno.save("Resultado.jpg")
        lb2.configure(image=render2)
        lb2.image=render2
    elif x.get() == 4:
        resaltar = ImageEnhance.Contrast(foto2).enhance(4)
        resaltar.show()
        resaltar.save("Resultado.jpg")
        lb2.configure(image=render2)
        lb2.image=render2
    else:
        lb2.configure(image=render2)
        lb2.image=render2

ventana = Tk()
ventana.geometry("500x400")
x = IntVar()
titulo = Label(ventana, text="Semana 11 2.10.22")
lb2 = Label(ventana, image="")
btn2= Button(ventana, text="Cargar foto", command=cargar)
btn = Radiobutton(ventana, text="Blanco y negro", value=1, variable=x)
btn3 = Radiobutton(ventana, text="Desenfocar", value=2, variable=x)
btn4 = Radiobutton(ventana, text="Contorno", value=3, variable=x)
btn5 = Radiobutton(ventana, text="Resaltar", value=4, variable=x)
titulo.place(relx=0.05, rely=0.05)
lb2.place(relx=0.05, rely=0.2)
btn2.place(relx=0.7, rely=0.4)
btn.place(relx=0.05, rely=0.75)
btn3.place(relx=0.26, rely=0.75)
btn4.place(relx=0.43, rely=0.75)
btn5.place(relx=0.59, rely=0.75)
ventana.mainloop()