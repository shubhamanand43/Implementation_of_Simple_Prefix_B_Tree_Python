#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    May 20, 2019 06:54:15 PM IST  platform: Windows NT

import sys
import os
# import numpy as np
# import pandas as pd
from backend.sbpt import Sbpt
from backend.alter import Alter

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

import addrecord_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    addrecord_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    addrecord_support.init(w, top, *args, **kwargs)
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
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("900x500+200+100")
        top.title("Add New Record")
        top.configure(background="#ffaa00")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.033, rely=0.06,
                          relheight=0.89, relwidth=0.939)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(width=845)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.024, rely=0.135, height=21, width=184)
        self.Label1.configure(anchor='e')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Consolas} -size 11 -slant italic")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(justify='left')
        self.Label1.configure(text='''User ID''')
        self.Label1.configure(width=184)

        self.Entry11 = tk.Entry(self.Frame1)
        self.Entry11.place(relx=0.272, rely=0.809, height=30, relwidth=0.17)
        self.Entry11.configure(background="#ebfffd")
        self.Entry11.configure(disabledforeground="#a3a3a3")
        self.Entry11.configure(font="-family {Consolas} -size 11")
        self.Entry11.configure(foreground="#000000")
        self.Entry11.configure(insertbackground="black")
        self.Entry11.configure(readonlybackground="#f0f0f0")
        self.Entry11.configure(relief="groove")
        self.Entry11.configure(selectbackground="#0078d7")
        self.Entry11.configure(width=144)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.024, rely=0.202, height=21, width=184)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='e')
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Consolas} -size 11 -slant italic")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(justify='left')
        self.Label2.configure(text='''Emp ID''')

        self.Entry01 = tk.Entry(self.Frame1)
        self.Entry01.place(relx=0.272, rely=0.135, height=30, relwidth=0.17)
        self.Entry01.configure(background="#ebfffd")
        self.Entry01.configure(disabledforeground="#a3a3a3")
        self.Entry01.configure(font="-family {Consolas} -size 11")
        self.Entry01.configure(foreground="#000000")
        self.Entry01.configure(highlightbackground="#d9d9d9")
        self.Entry01.configure(highlightcolor="black")
        self.Entry01.configure(insertbackground="black")
        self.Entry01.configure(readonlybackground="#f0f0f0")
        self.Entry01.configure(relief="groove")
        self.Entry01.configure(selectbackground="#c4c4c4")
        self.Entry01.configure(selectforeground="black")
        self.Entry01.configure(width=144)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.024, rely=0.27, height=21, width=184)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='e')
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Consolas} -size 11 -slant italic")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(justify='left')
        self.Label3.configure(text='''Name Prefix''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.024, rely=0.337, height=21, width=184)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='e')
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Consolas} -size 11 -slant italic")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(justify='left')
        self.Label4.configure(text='''First Name''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.024, rely=0.404, height=21, width=184)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='e')
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Consolas} -size 11 -slant italic")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(justify='left')
        self.Label5.configure(text='''Middle Initial''')

        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.024, rely=0.539, height=21, width=184)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor='e')
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Consolas} -size 11 -slant italic")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(justify='left')
        self.Label7.configure(text='''Gender''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.024, rely=0.472, height=21, width=184)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(anchor='e')
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Consolas} -size 11 -slant italic")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(justify='left')
        self.Label6.configure(text='''Last Name''')

        self.Label8 = tk.Label(self.Frame1)
        self.Label8.place(relx=0.024, rely=0.607, height=21, width=184)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor='e')
        self.Label8.configure(background="#ffffff")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Consolas} -size 11 -slant italic")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(justify='left')
        self.Label8.configure(text='''E Mail''')

        self.Label10 = tk.Label(self.Frame1)
        self.Label10.place(relx=0.024, rely=0.742, height=21, width=184)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(anchor='e')
        self.Label10.configure(background="#ffffff")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(
            font="-family {Consolas} -size 11 -slant italic")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(justify='left')
        self.Label10.configure(text='''Mother's Name''')

        self.Label9 = tk.Label(self.Frame1)
        self.Label9.place(relx=0.024, rely=0.674, height=21, width=184)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(anchor='e')
        self.Label9.configure(background="#ffffff")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Consolas} -size 11 -slant italic")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(justify='left')
        self.Label9.configure(text='''Father's Name''')

        self.Label11 = tk.Label(self.Frame1)
        self.Label11.place(relx=0.024, rely=0.809, height=21, width=184)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(anchor='e')
        self.Label11.configure(background="#ffffff")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(
            font="-family {Consolas} -size 11 -slant italic")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(justify='left')
        self.Label11.configure(text='''Age in Yrs''')

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.272, rely=0.202, height=30, relwidth=0.17)
        self.Entry2.configure(background="#ebfffd")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Consolas} -size 11")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(readonlybackground="#f0f0f0")
        self.Entry2.configure(relief="groove")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(width=144)

        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry3.place(relx=0.272, rely=0.27, height=30, relwidth=0.17)
        self.Entry3.configure(background="#ebfffd")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="-family {Consolas} -size 11")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(readonlybackground="#f0f0f0")
        self.Entry3.configure(relief="groove")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(width=144)

        self.Entry6 = tk.Entry(self.Frame1)
        self.Entry6.place(relx=0.272, rely=0.472, height=30, relwidth=0.17)
        self.Entry6.configure(background="#ebfffd")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="-family {Consolas} -size 11")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(readonlybackground="#f0f0f0")
        self.Entry6.configure(relief="groove")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")
        self.Entry6.configure(width=144)

        self.Entry8 = tk.Entry(self.Frame1)
        self.Entry8.place(relx=0.272, rely=0.607, height=30, relwidth=0.17)
        self.Entry8.configure(background="#ebfffd")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="-family {Consolas} -size 11")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(highlightbackground="#d9d9d9")
        self.Entry8.configure(highlightcolor="black")
        self.Entry8.configure(insertbackground="black")
        self.Entry8.configure(readonlybackground="#f0f0f0")
        self.Entry8.configure(relief="groove")
        self.Entry8.configure(selectbackground="#c4c4c4")
        self.Entry8.configure(selectforeground="black")
        self.Entry8.configure(width=144)

        self.Entry7 = tk.Entry(self.Frame1)
        self.Entry7.place(relx=0.272, rely=0.539, height=30, relwidth=0.17)
        self.Entry7.configure(background="#ebfffd")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="-family {Consolas} -size 11")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(highlightbackground="#d9d9d9")
        self.Entry7.configure(highlightcolor="black")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(readonlybackground="#f0f0f0")
        self.Entry7.configure(relief="groove")
        self.Entry7.configure(selectbackground="#c4c4c4")
        self.Entry7.configure(selectforeground="black")
        self.Entry7.configure(width=144)

        self.Entry10 = tk.Entry(self.Frame1)
        self.Entry10.place(relx=0.272, rely=0.742, height=30, relwidth=0.17)
        self.Entry10.configure(background="#ebfffd")
        self.Entry10.configure(disabledforeground="#a3a3a3")
        self.Entry10.configure(font="-family {Consolas} -size 11")
        self.Entry10.configure(foreground="#000000")
        self.Entry10.configure(highlightbackground="#d9d9d9")
        self.Entry10.configure(highlightcolor="black")
        self.Entry10.configure(insertbackground="black")
        self.Entry10.configure(readonlybackground="#f0f0f0")
        self.Entry10.configure(relief="groove")
        self.Entry10.configure(selectbackground="#c4c4c4")
        self.Entry10.configure(selectforeground="black")
        self.Entry10.configure(width=144)

        self.Entry4 = tk.Entry(self.Frame1)
        self.Entry4.place(relx=0.272, rely=0.337, height=30, relwidth=0.17)
        self.Entry4.configure(background="#ebfffd")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="-family {Consolas} -size 11")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(readonlybackground="#f0f0f0")
        self.Entry4.configure(relief="groove")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")
        self.Entry4.configure(width=144)

        self.Entry9 = tk.Entry(self.Frame1)
        self.Entry9.place(relx=0.272, rely=0.674, height=30, relwidth=0.17)
        self.Entry9.configure(background="#ebfffd")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="-family {Consolas} -size 11")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(highlightbackground="#d9d9d9")
        self.Entry9.configure(highlightcolor="black")
        self.Entry9.configure(insertbackground="black")
        self.Entry9.configure(readonlybackground="#f0f0f0")
        self.Entry9.configure(relief="groove")
        self.Entry9.configure(selectbackground="#c4c4c4")
        self.Entry9.configure(selectforeground="black")
        self.Entry9.configure(width=144)

        self.Entry5 = tk.Entry(self.Frame1)
        self.Entry5.place(relx=0.272, rely=0.404, height=30, relwidth=0.17)
        self.Entry5.configure(background="#ebfffd")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="-family {Consolas} -size 11")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(readonlybackground="#f0f0f0")
        self.Entry5.configure(relief="groove")
        self.Entry5.configure(selectbackground="#c4c4c4")
        self.Entry5.configure(selectforeground="black")
        self.Entry5.configure(width=144)

        self.Label13 = tk.Label(self.Frame1)
        self.Label13.place(relx=0.521, rely=0.202, height=21, width=184)
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(anchor='e')
        self.Label13.configure(background="#ffffff")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(
            font="-family {Consolas} -size 11 -slant italic")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="black")
        self.Label13.configure(justify='left')
        self.Label13.configure(text='''Age in Company (Years)''')

        self.Label14 = tk.Label(self.Frame1)
        self.Label14.place(relx=0.521, rely=0.27, height=21, width=184)
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(anchor='e')
        self.Label14.configure(background="#ffffff")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(
            font="-family {Consolas} -size 11 -slant italic")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(justify='left')
        self.Label14.configure(text='''Salary''')

        self.Label15 = tk.Label(self.Frame1)
        self.Label15.place(relx=0.521, rely=0.337, height=21, width=184)
        self.Label15.configure(activebackground="#f9f9f9")
        self.Label15.configure(activeforeground="black")
        self.Label15.configure(anchor='e')
        self.Label15.configure(background="#ffffff")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(
            font="-family {Consolas} -size 11 -slant italic")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(highlightbackground="#d9d9d9")
        self.Label15.configure(highlightcolor="black")
        self.Label15.configure(justify='left')
        self.Label15.configure(text='''SSN''')

        self.Label16 = tk.Label(self.Frame1)
        self.Label16.place(relx=0.521, rely=0.404, height=21, width=184)
        self.Label16.configure(activebackground="#f9f9f9")
        self.Label16.configure(activeforeground="black")
        self.Label16.configure(anchor='e')
        self.Label16.configure(background="#ffffff")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(
            font="-family {Consolas} -size 11 -slant italic")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(highlightbackground="#d9d9d9")
        self.Label16.configure(highlightcolor="black")
        self.Label16.configure(justify='left')
        self.Label16.configure(text='''Phone No''')

        self.Label17 = tk.Label(self.Frame1)
        self.Label17.place(relx=0.521, rely=0.472, height=21, width=184)
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(activeforeground="black")
        self.Label17.configure(anchor='e')
        self.Label17.configure(background="#ffffff")
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(
            font="-family {Consolas} -size 11 -slant italic")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(highlightbackground="#d9d9d9")
        self.Label17.configure(highlightcolor="black")
        self.Label17.configure(justify='left')
        self.Label17.configure(text='''City''')

        self.Label18 = tk.Label(self.Frame1)
        self.Label18.place(relx=0.521, rely=0.539, height=21, width=184)
        self.Label18.configure(activebackground="#f9f9f9")
        self.Label18.configure(activeforeground="black")
        self.Label18.configure(anchor='e')
        self.Label18.configure(background="#ffffff")
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(
            font="-family {Consolas} -size 11 -slant italic")
        self.Label18.configure(foreground="#000000")
        self.Label18.configure(highlightbackground="#d9d9d9")
        self.Label18.configure(highlightcolor="black")
        self.Label18.configure(justify='left')
        self.Label18.configure(text='''State''')

        self.Label19 = tk.Label(self.Frame1)
        self.Label19.place(relx=0.521, rely=0.607, height=21, width=184)
        self.Label19.configure(activebackground="#f9f9f9")
        self.Label19.configure(activeforeground="black")
        self.Label19.configure(anchor='e')
        self.Label19.configure(background="#ffffff")
        self.Label19.configure(disabledforeground="#a3a3a3")
        self.Label19.configure(
            font="-family {Consolas} -size 11 -slant italic")
        self.Label19.configure(foreground="#000000")
        self.Label19.configure(highlightbackground="#d9d9d9")
        self.Label19.configure(highlightcolor="black")
        self.Label19.configure(justify='left')
        self.Label19.configure(text='''ZIP''')

        self.Label12 = tk.Label(self.Frame1)
        self.Label12.place(relx=0.521, rely=0.135, height=21, width=184)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(anchor='e')
        self.Label12.configure(background="#ffffff")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(
            font="-family {Consolas} -size 11 -slant italic")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(justify='left')
        self.Label12.configure(text='''Date of Joining''')

        self.Entry12 = tk.Entry(self.Frame1)
        self.Entry12.place(relx=0.769, rely=0.135, height=30, relwidth=0.17)
        self.Entry12.configure(background="#ebfffd")
        self.Entry12.configure(disabledforeground="#a3a3a3")
        self.Entry12.configure(font="-family {Consolas} -size 11")
        self.Entry12.configure(foreground="#000000")
        self.Entry12.configure(highlightbackground="#d9d9d9")
        self.Entry12.configure(highlightcolor="black")
        self.Entry12.configure(insertbackground="black")
        self.Entry12.configure(readonlybackground="#f0f0f0")
        self.Entry12.configure(relief="groove")
        self.Entry12.configure(selectbackground="#c4c4c4")
        self.Entry12.configure(selectforeground="black")
        self.Entry12.configure(width=144)

        self.Entry13 = tk.Entry(self.Frame1)
        self.Entry13.place(relx=0.769, rely=0.202, height=30, relwidth=0.17)
        self.Entry13.configure(background="#ebfffd")
        self.Entry13.configure(disabledforeground="#a3a3a3")
        self.Entry13.configure(font="-family {Consolas} -size 11")
        self.Entry13.configure(foreground="#000000")
        self.Entry13.configure(highlightbackground="#d9d9d9")
        self.Entry13.configure(highlightcolor="black")
        self.Entry13.configure(insertbackground="black")
        self.Entry13.configure(readonlybackground="#f0f0f0")
        self.Entry13.configure(relief="groove")
        self.Entry13.configure(selectbackground="#c4c4c4")
        self.Entry13.configure(selectforeground="black")
        self.Entry13.configure(width=144)

        self.Entry14 = tk.Entry(self.Frame1)
        self.Entry14.place(relx=0.769, rely=0.27, height=30, relwidth=0.17)
        self.Entry14.configure(background="#ebfffd")
        self.Entry14.configure(disabledforeground="#a3a3a3")
        self.Entry14.configure(font="-family {Consolas} -size 11")
        self.Entry14.configure(foreground="#000000")
        self.Entry14.configure(highlightbackground="#d9d9d9")
        self.Entry14.configure(highlightcolor="black")
        self.Entry14.configure(insertbackground="black")
        self.Entry14.configure(readonlybackground="#f0f0f0")
        self.Entry14.configure(relief="groove")
        self.Entry14.configure(selectbackground="#c4c4c4")
        self.Entry14.configure(selectforeground="black")
        self.Entry14.configure(width=144)

        self.Entry15 = tk.Entry(self.Frame1)
        self.Entry15.place(relx=0.769, rely=0.337, height=30, relwidth=0.17)
        self.Entry15.configure(background="#ebfffd")
        self.Entry15.configure(disabledforeground="#a3a3a3")
        self.Entry15.configure(font="-family {Consolas} -size 11")
        self.Entry15.configure(foreground="#000000")
        self.Entry15.configure(highlightbackground="#d9d9d9")
        self.Entry15.configure(highlightcolor="black")
        self.Entry15.configure(insertbackground="black")
        self.Entry15.configure(readonlybackground="#f0f0f0")
        self.Entry15.configure(relief="groove")
        self.Entry15.configure(selectbackground="#c4c4c4")
        self.Entry15.configure(selectforeground="black")
        self.Entry15.configure(width=144)

        self.Entry16 = tk.Entry(self.Frame1)
        self.Entry16.place(relx=0.769, rely=0.404, height=30, relwidth=0.17)
        self.Entry16.configure(background="#ebfffd")
        self.Entry16.configure(disabledforeground="#a3a3a3")
        self.Entry16.configure(font="-family {Consolas} -size 11")
        self.Entry16.configure(foreground="#000000")
        self.Entry16.configure(highlightbackground="#d9d9d9")
        self.Entry16.configure(highlightcolor="black")
        self.Entry16.configure(insertbackground="black")
        self.Entry16.configure(readonlybackground="#f0f0f0")
        self.Entry16.configure(relief="groove")
        self.Entry16.configure(selectbackground="#c4c4c4")
        self.Entry16.configure(selectforeground="black")
        self.Entry16.configure(width=144)

        self.Entry17 = tk.Entry(self.Frame1)
        self.Entry17.place(relx=0.769, rely=0.472, height=30, relwidth=0.17)
        self.Entry17.configure(background="#ebfffd")
        self.Entry17.configure(disabledforeground="#a3a3a3")
        self.Entry17.configure(font="-family {Consolas} -size 11")
        self.Entry17.configure(foreground="#000000")
        self.Entry17.configure(highlightbackground="#d9d9d9")
        self.Entry17.configure(highlightcolor="black")
        self.Entry17.configure(insertbackground="black")
        self.Entry17.configure(readonlybackground="#f0f0f0")
        self.Entry17.configure(relief="groove")
        self.Entry17.configure(selectbackground="#c4c4c4")
        self.Entry17.configure(selectforeground="black")
        self.Entry17.configure(width=144)

        self.Entry18 = tk.Entry(self.Frame1)
        self.Entry18.place(relx=0.769, rely=0.539, height=30, relwidth=0.17)
        self.Entry18.configure(background="#ebfffd")
        self.Entry18.configure(disabledforeground="#a3a3a3")
        self.Entry18.configure(font="-family {Consolas} -size 11")
        self.Entry18.configure(foreground="#000000")
        self.Entry18.configure(highlightbackground="#d9d9d9")
        self.Entry18.configure(highlightcolor="black")
        self.Entry18.configure(insertbackground="black")
        self.Entry18.configure(readonlybackground="#f0f0f0")
        self.Entry18.configure(relief="groove")
        self.Entry18.configure(selectbackground="#c4c4c4")
        self.Entry18.configure(selectforeground="black")
        self.Entry18.configure(width=144)

        self.Entry19 = tk.Entry(self.Frame1)
        self.Entry19.place(relx=0.769, rely=0.607, height=30, relwidth=0.17)
        self.Entry19.configure(background="#ebfffd")
        self.Entry19.configure(disabledforeground="#a3a3a3")
        self.Entry19.configure(font="-family {Consolas} -size 11")
        self.Entry19.configure(foreground="#000000")
        self.Entry19.configure(highlightbackground="#d9d9d9")
        self.Entry19.configure(highlightcolor="black")
        self.Entry19.configure(insertbackground="black")
        self.Entry19.configure(readonlybackground="#f0f0f0")
        self.Entry19.configure(relief="groove")
        self.Entry19.configure(selectbackground="#c4c4c4")
        self.Entry19.configure(selectforeground="black")
        self.Entry19.configure(width=144)

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.75, rely=0.764, height=44, width=160)
        self.Button1.configure(activebackground="#d8d8d8")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#88ff00")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(
            font="-family {Consolas} -size 12 -slant italic")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="flat")
        self.Button1.configure(text='''Add Record''')
        self.Button1.configure(width=197)

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.60, rely=0.764, height=44, width=100)
        self.Button2.configure(activebackground="#d8d8d8")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#F0DF87")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(
            font="-family {Consolas} -size 12 -slant italic")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="flat")
        self.Button2.configure(text='''Go Back''')
        self.Button2.configure(width=197)

        self.Message1 = tk.Message(self.Frame1)
        self.Message1.place(relx=0.367, rely=0.045,
                              relheight=0.052, relwidth=0.225)
        self.Message1.configure(background="#ffffff")
        self.Message1.configure(
            font="-family {Consolas} -size 13 -weight bold -slant italic -underline 1")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Add New Record''')
        self.Message1.configure(width=190)


        self.Message2 = tk.Message(self.Frame1)
        self.Message2.place(relx=0.75, rely=0.045, relheight=0.052
                , relwidth=0.189)
        self.Message2.configure(background="#ffffff")
        self.Message2.configure(font="-family {Consolas} -size 12 -weight bold")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(width=160)

        self.Button1.configure(command=self.addRecord)
        self.Button2.configure(command=self.goBack)
        # self.Entry01.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")
        # self.Entry1.insert(0, "a default value")

    def goBack(self):
        root.destroy()
        os.system('python operations.py')

    def addRecord(self):

        import random
        r1 = lambda: random.randint(7,15)
        r2 = lambda: random.randint(0,15)
        color = "#"+ str(hex(r1())[2:]) + str(hex(r2())[2:]) + str(hex(r1())[2:]) + str(hex(r2())[2:]) + str(hex(r1())[2:]) + str(hex(r2())[2:])

        var1 = str(self.Entry01.get())
        var2 = str(self.Entry2.get())
        var3 = str(self.Entry3.get())
        var4 = str(self.Entry4.get())
        var5 = str(self.Entry5.get())
        var6 = str(self.Entry6.get())
        var7 = str(self.Entry7.get())
        var8 = str(self.Entry8.get())
        var9 = str(self.Entry9.get())
        var10 = str(self.Entry10.get())
        var11 = str(self.Entry11.get())
        var12 = str(self.Entry12.get())
        var13 = str(self.Entry13.get())
        var14 = str(self.Entry14.get())
        var15 = str(self.Entry15.get())
        var16 = str(self.Entry16.get())
        var17 = str(self.Entry17.get())
        var18 = str(self.Entry18.get())
        var19 = str(self.Entry19.get())

        file = "data.txt"
        st = var1 +"|"+ var2 +"|"+ var3 +"|"+ var4 +"|"+ var5 +"|"+ var6 +"|"+ var7 +"|"+ var8 +"|"+ var9 +"|"+ var10 +"|"+ var11 +"|"+ var12 +"|"+ var13 +"|"+ var14 +"|"+ var15 +"|"+ var16 +"|"+ var17 +"|"+ var18 +"|"+ var19 + "\n"
        sp = Sbpt()
        t = sp.loadTree(file)
        ser = sp.search(t[0], var1)
        if var1 == '' or var2 == '' or var3 == '' or var4 == '' or var5 == '' or var6 == '' or var7 == '' or var8 == '' or var9 == '' or var10 == '' or var11 == '' or var12 == '' or var13 == '' or var14 == '' or var15 == '' or var16 == '' or var17 == '' or var18 == '' or var19 == '':
            self.Message2.configure(background=color)
            self.Message2.configure(text='''Fill all Boxes''')
        else:
            if ser[:2] == "NO":
                self.Entry01.delete(0, tk.END)
                self.Entry2.delete(0, tk.END)
                self.Entry3.delete(0, tk.END)
                self.Entry4.delete(0, tk.END)
                self.Entry5.delete(0, tk.END)
                self.Entry6.delete(0, tk.END)
                self.Entry7.delete(0, tk.END)
                self.Entry8.delete(0, tk.END)
                self.Entry9.delete(0, tk.END)
                self.Entry10.delete(0, tk.END)
                self.Entry11.delete(0, tk.END)
                self.Entry12.delete(0, tk.END)
                self.Entry13.delete(0, tk.END)
                self.Entry14.delete(0, tk.END)
                self.Entry15.delete(0, tk.END)
                self.Entry16.delete(0, tk.END)
                self.Entry17.delete(0, tk.END)
                self.Entry18.delete(0, tk.END)
                self.Entry19.delete(0, tk.END)
                at = Alter()
                at.add(st, file)
                self.Message2.configure(background=color)
                self.Message2.configure(text='''Added''')
                # print(st)
            else:
                self.Entry01.delete(0, tk.END)
                self.Message2.configure(background=color)
                self.Message2.configure(text='''Already Exist''')

if __name__ == '__main__':
    vp_start_gui()
