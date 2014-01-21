#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from config import Config
from process import ProcesBatch


class Color:
    GRIS = "#A4A4A4"
    GRISFORT = "#2E2E2E"
    GREEN = "#CCFF00"
    BLACK = "#000000"


class App:
    def __init__(self, parent):

        self.conf = Config()

        parent.geometry("600x350+350+250")
        parent.title("Foto Process")
        #parent.wm_iconbitmap(ICON)
        f = Frame(parent)
        f.pack(padx=0, pady=10)

        # Label Carpeta
        Label(f, text="Carpeta ",
              font="{Verdana} 15").grid(sticky=E, row=1, column=0)

        # Entry Carpeta
        self.entry_carpeta = Entry(f, bg=Color.GRISFORT,
                                   fg=Color.GREEN, width=47,
                                   font="{Verdana} 15")
        self.entry_carpeta.grid(sticky=NW, row=1, column=1)
        self.entry_carpeta.insert(END, self.conf.c)

        # Separador
        Label(f, text="").grid(sticky=NE, row=2, column=0)

        # Label Tag
        Label(f, text="Tag ",
              font="{Verdana} 15").grid(sticky=E, row=3, column=0)

        # Entry Tag
        self.entry_tag = Entry(f, bg=Color.GRISFORT, fg=Color.GREEN, width=27,
                               font="{Verdana} 15")
        self.entry_tag.grid(sticky=NW, row=3, column=1)
        self.entry_tag.insert(END, self.conf.tag)

        # Separador
        Label(f, text="").grid(sticky=NE, row=4, column=0)

        MODES = [
            (1, "Senderisme", "senderisme"),
            (2, "BTT", "btt"),
            (3, "Muntanya", "muntanya"),
            (4, "Fotos", "fotos")
        ]

        # Valor per defecte
        self.v = StringVar()
        self.v.set(self.conf.tipus)

        # Label Tipus
        Label(f, text="Tipus ",
              font="{Verdana} 15").grid(row=5, column=0, sticky=NE)

        # Radiobutton Tipus
        for num, text, nom in MODES:
            Radiobutton(f, text=text, variable=self.v,
                        value=nom,
                        font="{Verdana} 15").grid(sticky=W,
                                                  row=4+num,
                                                  column=1)

        # Separador
        Label(f, text="").grid(sticky=NE, row=9, column=0)

        # Button
        Button(f, text="Processar Fotos", command=self.processar,
               width=20, bg=Color.BLACK, borderwidth=0, fg=Color.GREEN,
               activebackground=Color.GREEN,
               font="{Verdana} 22").grid(row=10, column=1)

        self.info = StringVar()

        # Label info
        Label(f, textvariable=self.info, text="",
              font="{Verdana} 22").grid(sticky=W, row=11, column=1)

    def processar(self):
        g = ProcessaFotos()
        g.guardar(
            self.entry_carpeta.get(),
            self.entry_tag.get(),
            self.v.get()
        )
        msg = g.processar()
        self.info.set(msg)


class ProcessaFotos:

    def __init__(self):
        pass

    def processar(self):
        pb = ProcesBatch()
        pb.run()
        return "Process OK"

    def guardar(self, entry_carpeta, entry_tag, tipo):
        print "Guardar"
        conf = Config()
        conf.c = entry_carpeta
        conf.tag = entry_tag
        conf.tipus = tipo
        conf.guardar_par()


def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
