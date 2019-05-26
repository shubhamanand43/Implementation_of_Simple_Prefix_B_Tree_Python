from backend.sbpt import LNode,BNode,Sbpt
# from alter import Alter
# from backend.sbpt import

# at = Alter()
# print(at.delete("aebanks","text.txt"))
sp = Sbpt()
t = sp.loadTree("test.txt")
print(sp.search(t[0],"acfrye"))
