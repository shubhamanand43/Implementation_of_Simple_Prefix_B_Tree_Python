#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    May 19, 2019 05:01:24 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import datashow_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    datashow_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    datashow_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("900x500+200+100")
        top.title("data.txt")
        top.configure(background="#EAF0F1")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.852, rely=0.02, height=24, width=100)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffaa00")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Consolas} -size 11")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="flat")
        self.Button1.configure(text='''Back''')
        self.Button1.configure(width=137)

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.389, rely=0.02, relheight=0.026
                , relwidth=0.233)
        self.Message1.configure(background="#ffaa00")
        self.Message1.configure(font="-family {Consolas} -size 12 -slant italic")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Current TEXT data''')
        self.Message1.configure(width=210)

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.033, rely=0.08, relheight=0.864
                , relwidth=0.938)
        self.Listbox1.configure(background="#ffffff")
        # self.Listbox1.configure(background="#EAF0F1")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="-family {Consolas} -size 11")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(relief="flat")
        self.Listbox1.configure(width=844)

        self.scrollbar_y = tk.Scrollbar(self.Listbox1, orient="vertical")
        self.scrollbar_y.config(command=self.Listbox1.yview)
        self.scrollbar_y.pack(side="right", fill="y")
        self.Listbox1.config(yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x = tk.Scrollbar(self.Listbox1, orient="horizontal")
        self.scrollbar_x.config(command=self.Listbox1.xview)
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.Listbox1.config(xscrollcommand=self.scrollbar_x.set)

        for x in range(100):
            b = "djfhffuifififuiduiff hfgius gjisdufgiuf gvifsjgiurd iufdgujfidusguiosdr uijhguisfjgifejd ifgjuidsfguif fdsgjfsdgjfiuud fjifdsgidjgui ufgjisdfgisfjdsi fgigjsidji fdgisfdjgfiod fgjidsfgiodsf ifddgisfdgio fdgjiosfdjfgifdsgfidi vidsjgifjdui fdsg ifdui fuijgfuidsguifd"
            self.Listbox1.insert(tk.END, b)

if __name__ == '__main__':
    vp_start_gui()
