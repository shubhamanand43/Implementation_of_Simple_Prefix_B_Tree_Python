import os
import pandas as pd
from sbpt import LNode,BNode,Sbpt
# from folder.file import Klasa

class Alter(object):

    def __init__(self):
        pass

    # Comma to pipe and csv to txt ...
    def csvToTxt(self, file):
        fr = open(file)
        st = fr.read()
        sn = st.replace(",", "|")
        fr.close()
        fw = open("temp.csv", "w")
        fw.write(sn)
        fw.close()
        os.remove(file)
        os.rename("temp.csv", file)
        n_file = file.split(".")[0] + ".txt"
        os.rename(file, n_file)
        return n_file

    # Pipe to Comma and txt to csv ...
    def txtToCsv(self, file):
        fr = open(file)
        st = fr.read()
        sn = st.replace("|", ",")
        fr.close()
        fw = open("temp.txt", "w")
        fw.write(sn)
        fw.close()
        os.remove(file)
        os.rename("temp.txt", file)
        n_file = file.split(".")[0] + ".csv"
        os.rename(file, n_file)
        return n_file

    def add(self, tup, file):
        fd = open(file,"a")
        st_add = tup[0] +"|"+ tup[1] +"|"+ tup[2] + "|" + tup[3] + "|" + tup[4] + "|" + tup[5] + "\n"
        fd.write(st_add)
        fd.close()
        file = self.txtToCsv(file)
        df = pd.read_csv(file)
        df = df.sort_values(by=['User_ID'])
        df.to_csv(file, index = False)
        file = self.csvToTxt(file)

    def delete(self, id, file):
        at_sbpt = Sbpt()
        t = at_sbpt.loadTree(file)
        st = at_sbpt.search(t[0],id)
        if st[:2] == "NO":
            return st
        else:
            file = self.txtToCsv(file)
            df = pd.read_csv(file)
            df = df[df.User_ID != id]
            df.to_csv(file, index = False)
            file = self.csvToTxt(file)
            return id + " User DELETED from RECORD"

    # def modify(self, id, tup, file):
    #     at_sbpt = Sbpt()
    #     t = at_sbpt.loadTree(file)
    #     st = at_sbpt.search(t[0],id)
    #     if st[:2] == "NO":
    #         return st
    #     else:
    #         st = self.delete(id, file)
    #         self.add(tup, file)
    #         return id + " Been Modified"


# sbpt = Sbpt()
# t = sbpt.loadTree("text.txt")
# l_node = LNode(t[0])
# f_node = sbpt.addFirstElm(l_node)
# node = f_node
# fl_node = l_node
#
# for i in range(len(t[1])):
#   child = LNode(records=t[2][i])
#   node = sbpt.add(node, t[1][i], child)
#   l_node.next_node = child
#   l_node = child
# print(sbpt.search(t[0],"aachapman"))

# change = Alter()
# st = input("--> ")
# st0 = input("User_ID --> ")
# st1 = input("Emp ID --> ")
# st2 = input("First Name --> ")
# st3 = input("Middle Initial --> ")
# st4 = input("Last Name --> ")
# st5 = input("Gender --> ")
# tup = (st0, st1, st2, st3, st4, st5)

# print(change.delete(st,"text.txt"))
# change.add(tup, "text.txt")
