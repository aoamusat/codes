import tkinter as tk
from tkinter import ttk
#from tkinter.messagebox import showinfo

from setuptools import Command

def close(): 
        root.destroy() 


def atribuir():
    return selected_size.get()

#def show_selected_size():
  #      filename = selected_size.get()
        #print(filename)


root = tk.Tk()
root.geometry('300x220')
root.resizable(False, False)
root.title('F-02')

selected_size = tk.StringVar()
sizes = (('Essencia', '4000'),('Caule', '5000'),('Sage', '6000'),('Outra aí', 'XL'),('Mais uma', 'XXL'))

# label
label = ttk.Label(text="Selecione a empresa:")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(root, text=size[0], value=size[0], variable=selected_size, command=atribuir)
    r.pack(fill='x', padx=5, pady=5)


# button
button = ttk.Button(root, text="Selecionar", command=close)
button.pack(fill='x', padx=5, pady=5)
        
root.mainloop()


        #return filename
        #self.root.destroy()
        
                    




    
