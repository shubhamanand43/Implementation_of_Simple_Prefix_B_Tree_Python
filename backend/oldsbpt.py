class LNode():
  def __init__(self,records=None,next_node=None):
    self.records = records
    self.next_node = next_node

  def get_data(self):
    return self.records

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next



class BNode():
  def __init__(self):
    self.parNode = None
    self.parent = False
    self.sep = []
    self.child = []
    # self.sep_all = "".join(self.sep)
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
    if len(node.child)==4:
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
      return self.newBNodeChild(n_node, level-1)
    else:
      return node

  def newBNodeChild(self, node, level):
    if level >= 1:
      n_node = BNode()
      n_node.level = level
      n_node.parent = True
      n_node.parNode = node
      node.child.append(n_node)
      return self.newBNodeChild(n_node, level-1)
    else:
      return node

  def add(self, node, sep, child):
    a_node = self.availNode(node)
    if len(a_node.child)==4:
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
        return n_node
      else:
        a_node.sep.append(sep)
        m_node = self.newBNodeChild(a_node, cur_level-1)
        m_node.parent = True
        m_node.child.append(child)
        return m_node
    else:
      if a_node.level == 1:
        a_node.sep.append(sep)
        a_node.child.append(child)
        print(a_node.child)
        return a_node
      else:
        n_node = self.newBNodeChild(a_node,a_node.level-1)
        a_node.sep.append(sep)
        n_node.child.append(child)
        return n_node

  def getRootNode(self, node):
    pass

  def searchRecord(self, ssn):
    pass

  def showAllRecords(self, node):
    pass

sbpt = Sbpt()
f_node = sbpt.addFirstElm('apple')

ls = ['ba','bc','ca','cc','da','dc','ea','ec','fa','fc','ga','gc','ha','hc','ia','ic','ja','jc',
      'ka','kc','la','lc','ma','mc','na','nc','oa','oc','pa','pc','qa','qc','ra','rc','sa','sc',
      'ta','tc','ua','uc','va','vc','wa','wc','xa','xc','ya','yc','za','zc']
lc = ['baoy','bcoy','caat','ccat','daog','dcog','eaagle','ecagle','farog','fcrog','gaoat','gcoat','haen','hcen',
      'iank','icnk','jaam','jcam','kaite','kcite','laemon','lcemon','maen','mcen','naest','ncest','oane','ocne','paen','pcen',
      'qauery','qcuery','raed','rced','saheep','scheep','taop','tcop','uapsc','ucpsc','vaava','vcava','wahite','wchite',
      'xain','xcin','yaellow','ycellow','zaen','zcen']

node = f_node
for i in range(len(ls)):
  node = sbpt.add(node,ls[i],lc[i])
