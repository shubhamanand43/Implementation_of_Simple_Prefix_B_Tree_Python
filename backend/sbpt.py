class LNode():
    def __init__(self, records=None, next_node=None):
        self.records = records
        self.next_node = next_node


class BNode():
    def __init__(self):
        self.parNode = None
        self.parent = False
        self.sep = []
        self.child = []
        self.sep_all = "".join(self.sep)
        self.level = None


class Sbpt(object):

    def __init__(self):
        pass

    def addFirstElm(self, child):
        f_node = BNode()
        f_node.child.append(child)
        f_node.level = 1
        return f_node

    def availNode(self, node):
        if len(node.child) == 4:
            if node.parent == False:
                return node
            else:
                return self.availNode(node.parNode)
        else:
            return node

    def newBNodeParent(self, node, level):
        if level >= 1:
            n_node = BNode()
            n_node.level = level
            n_node.parent = True
            n_node.parNode = node.parNode
            node.parNode.child.append(n_node)
            return self.newBNodeChild(n_node, level - 1)
        else:
            return node

    def newBNodeChild(self, node, level):
        if level >= 1:
            n_node = BNode()
            n_node.level = level
            n_node.parent = True
            n_node.parNode = node
            node.child.append(n_node)
            return self.newBNodeChild(n_node, level - 1)
        else:
            return node

    def add(self, node, sep, child):
        a_node = self.availNode(node)
        if len(a_node.child) == 4:
            cur_level = a_node.level
            if a_node.parent == False:
                p_node = BNode()
                p_node.level = a_node.level + 1
                p_node.child.append(a_node)
                p_node.sep.append(sep)
                a_node.parent = True
                a_node.parNode = p_node
                cur_level = a_node.level
                n_node = self.newBNodeParent(a_node, cur_level)
                n_node.child.append(child)
                # print(n_node.child[-1].records)
                return n_node
            else:
                a_node.sep.append(sep)
                n_node = self.newBNodeChild(a_node, cur_level - 1)
                n_node.parent = True
                n_node.child.append(child)
                # print(n_node.child[-1].records)
                return n_node
        else:
            if a_node.level == 1:
                a_node.sep.append(sep)
                a_node.child.append(child)
                # print(a_node.child[-1].records)
                return a_node
            else:
                n_node = self.newBNodeChild(a_node, a_node.level - 1)
                a_node.sep.append(sep)
                n_node.child.append(child)
                # print(n_node.child[-1].records)
                return n_node

    # Take Node as first BNode...
    def getRootNode(self, node):
        if node.parent == True:
            node = node.parNode
            return self.getRootNode(node)
        else:
            return node

    def getNodeSep(self, node, id):
        li = node.sep
        li.append(id)
        li.sort()
        p = li.index(id)
        return p

    # Nothing.....
    def searchRecord(self, node, id):
        if node.level > 1:
            pos = self.getNodeSep(node, id)
            c_node = node.child[pos]
            return self.searchRecord(c_node, id)
        else:
            s_node = node
            for x in node.child:
                if id in x.records:
                    tup = (x, s_node)
                    return tup
            else:
                tup = ("NOT FOUND search record wala", s_node)
                return tup

    # get Node as first BNode and id as ID
    def searchOp(self, node, id):
        r_node = self.getRootNode(node)
        s_node = self.searchRecord(r_node, id)
        # if type(s_node[0])==str:
        #   print(s_node[0])
        # else:
        #   print(s_node[0].records)
        return s_node[1]

    # Take NODE as return from searchOp()
    def getSearchBlock(self, node, id):
        l_index = self.getNodeSep(node, id)
        l_node = node.child[l_index]
        return l_node.records

    # Take block as return of getSearchBlock()
    def findInBlock(self, block, id):
        lb = block
        flag = 0
        for i in lb:
            if i.split("|")[0] == id:
                # print(i)
                return i
                flag = 1
        if flag == 0:
            # print("NOT FOUND FIND WALA")
            return "NOT FOUND"

    # Take Node as a first BNode and id as ID
    def search(self, node, id):
        so = self.searchOp(node, id)
        sb = self.getSearchBlock(so, id)
        # print(sb)
        return self.findInBlock(sb, id)

    def getSepBlocks(self, file, b_size=10, s_size=4):
        fdata = open(file, "r")
        fblocks = []
        li_record = fdata.read().split("\n")
        li_record.pop()
        head = li_record[0]
        li_record.pop(0)
        m = 0
        for x in range(0, int(len(li_record) / b_size)):
            ad = li_record[x * b_size:x * b_size + b_size]
            m = x
            fblocks.append(ad)
        if len(li_record) % b_size > 0:
            ad = li_record[m * b_size + b_size:]
            fblocks.append(ad)
        sep = []
        c = 0
        for i in fblocks:
            sep.append(fblocks[c][0].split("|")[0])
            c += 1
        f_blk = fblocks[0]
        sepr = [x[:s_size] for x in sep]
        tup = (f_blk, sepr[1:], fblocks[1:], head)
        return tup

    def showAllLnode(self, lnode):
        print(lnode.records)
        if lnode.next_node == None:
            pass
        else:
            return self.showAllLnode(lnode.next_node)

    def loadTree(self, file):
        t = self.getSepBlocks(file, 10, 4)
        l_node = LNode(t[0])
        f_node = self.addFirstElm(l_node)
        node = f_node
        fl_node = l_node
        for i in range(len(t[1])):
            child = LNode(records=t[2][i])
            node = self.add(node, t[1][i], child)
            l_node.next_node = child
            l_node = child
        tup = (f_node,l_node)
        return tup
        # print(sbpt.search(f_node, "aachapman"))


# sbpt = Sbpt()
# t = sbpt.getSepBlocks("1000records.txt", 10, 4)
# # print(t[0])
# # print(t[3])
# # print(t[1])
# # print(t[2][0])
# # l_node = LNode("apple")
# l_node = LNode(t[0])
#
# f_node = sbpt.addFirstElm(l_node)
#
# # ls = ['ba','bc','ca','cc','da','dc','ea','ec','fa','fc','ga','gc','ha','hc','ia','ic','ja','jc',
# #       'ka','kc','la','lc','ma','mc','na','nc','oa','oc','pa','pc','qa','qc','ra','rc','sa','sc',
# #       'ta','tc','ua','uc','va','vc','wa','wc','xa','xc','ya','yc','za','zc']
# # lc = ['baoy','bcoy','caat','ccat','daog','dcog','eaagle','ecagle','farog','fcrog','gaoat','gcoat','haen','hcen',
# #       'iank','icnk','jaam','jcam','kaite','kcite','laemon','lcemon','maen','mcen','naest','ncest','oane','ocne','paen','pcen',
# #       'qauery','qcuery','raed','rced','saheep','scheep','taop','tcop','uapsc','ucpsc','vaava','vcava','wahite','wchite',
# #       'xain','xcin','yaellow','ycellow','zaen','zcen']
#
# node = f_node
# fl_node = l_node
#
# # for i in range(len(ls)):
# #   child = LNode(records=lc[i])
# #   node = sbpt.add(node, ls[i], child)
# #   l_node.next_node = child
# #   l_node = child
#
# for i in range(len(t[1])):
#   child = LNode(records=t[2][i])
#   node = sbpt.add(node, t[1][i], child)
#   l_node.next_node = child
#   l_node = child
#
# # sbpt.showAllLnode(fl_node)
# print(sbpt.search(f_node,"aachapman"))
#
# # so = sbpt.searchOp(f_node, "cop")
# # sb = sbpt.getSearchBlock(so, "cop")
# # print(sb)
# # sbpt.findInBlock(sb,"cop")
#
# # SEARCH Operations......
# # r_node = sbpt.getRootNode(node)
# # s_node = sbpt.searchRecord(r_node,"aam")
# # if type(s_node)==str:
# #   print(s_node)
# # else:
# #   print(s_node.child)
#
# # GET Root Node....
# # r_node = sbpt.getRootNode(f_node)
# # print(r_node.child)
# # print(r_node.level)
#
# # for i in range(len(t[1])):
#   # node = sbpt.add(node, t[1][i], t[2][i])
