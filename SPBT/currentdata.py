#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    May 21, 2019 04:10:27 AM IST  platform: Windows NT

from backend.sbpt import LNode,BNode,Sbpt
import sys
import os

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

import currentdata_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    currentdata_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    currentdata_support.init(w, top, *args, **kwargs)
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

        top.geometry("1200x650+60+25")
        top.title("Current TEXT Data")
        top.configure(background="#BB2CD9")

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.017, rely=0.031, relheight=0.942
                , relwidth=0.97)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="-family {Consolas} -size 11")
        self.Listbox1.configure(foreground="#535C68")
        self.Listbox1.configure(relief="flat")
        self.Listbox1.configure(width=1164)

        self.scrollbar_y = tk.Scrollbar(self.Listbox1, orient="vertical")
        self.scrollbar_y.config(command=self.Listbox1.yview)
        self.scrollbar_y.pack(side="right", fill="y")
        self.Listbox1.config(yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x = tk.Scrollbar(self.Listbox1, orient="horizontal")
        self.scrollbar_x.config(command=self.Listbox1.xview)
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.Listbox1.config(xscrollcommand=self.scrollbar_x.set)

        file = "data.txt"
        fd = open(file)
        ld = fd.read().split("\n")
        fd.close()

        for line in ld:
            self.Listbox1.insert(tk.END, line)

if __name__ == '__main__':
    vp_start_gui()
