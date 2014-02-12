import copy
from operator import add

class Group:
    elem = []
    rule = {}
    unit = None
    def __init__(self, unit, elem, rule):
        self.elem = elem
        self.unit = unit
        self.rule = rule
    def calc(self, a, b):
        return self.rule[(a, b)]
    def make_table(self):
        table = [[[] for y in self.elem] for x in self.elem]
        for k1, v1 in enumerate(self.elem):
            for k2, v2 in enumerate(self.elem):
                table[k1][k2] = self.calc(v1, v2)
        return table
    def make_indextable(self):
        table2 = self.make_table()
        table = [[self.elem[i]]+table2[i] for i in range(len(self.elem))]
        table = [["*"]+self.elem] + table
        return table
    def print_table(self):
        table = self.make_indextable()
        flattened = sum(table, [])
        maxlen = max([len(str(x)) for x in flattened])
        rowlen = maxlen*(len(self.elem)+1) + len(self.elem) + 2
        print "-"*rowlen
        showtable = [[[] for y in self.elem] for x in self.elem]
        for y in range(len(self.elem)+1):
            row = "|"
            for x in range(len(self.elem)+1):
                s = str(table[x][y])
                row += " "*(maxlen - len(s)) + s + "|"
            print row
            print "-"*rowlen
        return
    def is_group(self):
        if not self.unit in self.elem:
            #print "No Unit"
            return False

        for x in self.elem:
            prod = [self.calc(x, y) for y in self.elem]
            if not self.unit in prod:
                #print "No inverse to " + str(self.unit) + ", " + str([str(i) for i in prod])
                return False


        for x in self.elem:
            prod = [self.calc(x, y) for y in self.elem]
            if len(set(prod)-set(self.elem)) != 0:
                #print "Not closed " + str(prod)
                return False
        return True
    def generate_subgroups(self):
        subsets = [x for x in gen_subset(self.elem)]
        cand = [Group(self.unit, x, self.rule) for x in subsets]
        return [x for x in cand if x.is_group()]
    def is_normal_to(self, parent):
        for a in parent.elem:
            an = set([parent.calc(a, x) for x in self.elem])
            na = set([parent.calc(x, a) for x in self.elem])
            if an != na:
                return False
        return True


class Permutation:
    permlist = []
    def __init__(self, l):
        self.permlist = l
    def compose(self, p):
        return Permutation([p.permlist[i] for i in self.permlist])
    def __str__(self):
        return "P" + str(self.permlist)
    def __eq__(self, other):
        return self.permlist == other.permlist
    def __hash__(self):
        return hash(str(self.permlist))

def get_permutations(l):
    if len(l) == 1:
        return [l]
    acc = []
    for i in l:
        acc += [[i] + y for y in get_permutations([x for x in l if x != i])]
    return acc



def gen_subset(l):
    acc = [[]]
    for i in l:
        ac1 = acc
        ac2 = [x + [i] for x in acc]
        acc = ac1 + ac2
    return acc

def test_group():
    g = Group(0, [0, 1],
              {(0,0):0,
               (0,1):1,
               (1,0):1,
               (1,1):0})
    g.print_table()
    print g.is_group()
    for i in g.generate_subgroups():
        i.print_table()

        print "*"*80

        g = Group(0, range(12),
                  dict([((i, j), (i + j)%12) for i in range(12) for j in range(12)]))
        g.print_table()
        print g.is_group()
        for i in g.generate_subgroups():
            i.print_table()

            print "*"*80
            g = Group(0, [0, 1],
                      {(0,0):1,
                       (0,1):1,
                       (1,0):1,
                       (1,1):1})
            g.print_table()
            print g.is_group()
            for i in g.generate_subgroups():
                i.print_table()
                print "*"*80

                print gen_subset([0, 1, 2])

def test_perm():
    p = Permutation([2,1,0])
    q = Permutation([1,2,0])
    print p, q, p.compose(q)
    print get_permutations([0, 1, 2])

def test_permgroup():
    elem = [Permutation(x) for x in get_permutations([0, 1, 2])]
    g = Group(Permutation([0, 1, 2]),
              elem,
              dict([((x, y), x.compose(y)) for x in elem for y in elem]))
    g.print_table()
    sg = g.generate_subgroups()
    for i in sg:
        i.print_table()
        print i.is_normal_to(g)

def make_permutation_group(n):
    elem = [Permutation(x) for x in get_permutations(range(n))]
    g = Group(Permutation(range(n)),
              elem,
              dict([((x, y), x.compose(y)) for x in elem for y in elem]))
    return g


