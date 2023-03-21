import os
import tkinter as tk
from tkinter import filedialog

option = [
    "EPUB",
    "AZW3",
    "MOBI",
    "DOCX",
    "FB2",
    "HTMLZ",
    "KFX",
    "LIT",
    "LRF",
    "PDB",
    "PDF",
    "PMLZ",
    "RB",
    "RTF",
    "SNB",
    "TCR",
    "TXT",
    "TXTZ",
    "ZIP"
]
filename = ()
def browsefiles():
    global filename
    filename = tk.filedialog.askopenfilename(initialdir = "/home/noah/Downloads",
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("PDF files",
                                                        "*.pdf*")))
    label_file_explorer.configure(text="File Opened: "+filename)
def convertTuple(tup):
        st = ''.join(map(str, tup))
        return st

def convert(f,l): # f = output format, l = input file
    l = str(l)
    basename = os.path.splitext(l)
    basename = basename[0]
    basename = basename + "." + f

    print("ebook-convert " + f'"{l}"' + " " + f'"{basename}"')
    cmd = ("ebook-convert " + f'"{l}"' + " " + f'"{basename}"')
    os.system(cmd)
    print(l)



window = tk.Tk()

window.title('Kindle Converter')

window.geometry("500x500")


dropVar = tk.StringVar(window)
dropVar.set(option[0])

outPutMenu = tk.OptionMenu(window, dropVar, *option)

 
label_file_explorer = tk.Label(window,text= "Select File", width=100,height=4)
button_explore = tk.Button(window,text="Browse Files", command=browsefiles)
commandtd = print("test")
conv = tk.Button(window,text="Convert",command=lambda : (convert(f = dropVar.get().lower(),l = filename)))
convLabel = tk.Label(window,text="Convert")

label_file_explorer.pack()
button_explore.pack()
outPutMenu.pack()
convLabel.pack()
conv.pack()
window.mainloop()

print(filename)

# (convert(f = dropVar.get().lower(),l = filename))