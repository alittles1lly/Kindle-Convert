import os

filename = input("Enter File Location ")
def query():
    global dropVar

    dropVar = input("Enter wanted file type, or type -h options ")
query()


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

if dropVar == "-h":
      print(option)
      query()


def convertTuple(tup):
        st = ''.join(map(str, tup))
        return st

def convert(f,l): # f = output format, l = input file
    global basename
    global filename
    l = str(l)
    basename = os.path.splitext(l)
    basename = basename[0]
    basename = basename + "." + f

    print("ebook-convert " + f'"{l}"' + " " + f'"{basename}"')
    cmd = ("ebook-convert " + f'"{l}"' + " " + f'"{basename}"')
    os.system(cmd)



convert(f = dropVar.lower(),l = filename)

if filename != ".":
    print("File saved to" + f'"{basename}"')