### This is a COMMENT made by Ana-Doris Moisuc & Andrei-Ovidiu Muntean
# Please remove the comment below. The parsing strategy you've used has nothing to do with
# the Grammar class and it should not be in grammar.py
###
# 1c: LR(0)

class Grammar:
    def __init__(self, filename):
        ### This is a COMMENT made by Ana-Doris Moisuc & Andrei-Ovidiu Muntean
        # By having just the filename in the constructor, you achieve two undesirable things:
        # 1. A Grammar object should always be consistent. Your object is inconsistent when you initialize it
        #    and remains inconsistent until you call the `getGrammarFromFile` method on it. A better approach
        #    would be to have a static method that gets a filename and generates a new grammar, having all the
        #    required fields in the Grammar constructor
        # 1. Your Grammar class contains an irrelevant field. (filename) This is used only for generating the
        #    Grammar and is of no use afterwards.
        ###
        self.nonTerminals = []
        self.terminals = []
        self.starting = ''
        self.productions = {}
        self.filename = filename
        self.getGrammarFromFile()

    def getProductionString(self):
        theStr = ''
        for k in self.productions.keys():
            theStr += k + ' -> '
            for t in self.productions[k]:
                theStr += t[0] + ' | '
            theStr = theStr[:-3] + '\n'
        return theStr

    def getProduction(self, index):
        for k in self.productions.keys():
            for p in self.productions[k]:
                if p[1] == index:
                    return k, p[0].strip()
        return None

    def getGrammarFromFile(self):
        ### This is a COMMENT made by Ana-Doris Moisuc & Andrei-Ovidiu Muntean
        # From the design perspective, I find it more intuitive for this method to return a Grammar
        ###
        with open(self.filename, 'r') as file:
            split_line = file.readline().strip().split('=')[1].split(' ')
            for item in split_line:                 # N
                self.nonTerminals.append(item)
            split_line = file.readline().strip()[2:].split(' ')
            ### This is a COMMENT made by Ana-Doris Moisuc & Andrei-Ovidiu Muntean
            # A more pythonic way of adding all the elements of one list to another would be: self.terminals.extend(split_line)
            ###
            for item in split_line:                 # T
                self.terminals.append(item)
            self.starting = file.readline().strip().split('=')[1]   # S
            file.readline()
            # P
            index = 1
            for line in file:
                lhs, rhs = line.split('->')
                rhs = rhs.strip().split(' | ')
                for value in rhs:
                    if lhs in self.productions.keys():
                        self.productions[lhs].append((value, index))
                    else:
                        self.productions[lhs] = [(value, index)]
                    index += 1

    def CFG_check(self):
        for k in self.productions:
            ks = k.split()
            if len(ks) > 1:
                print("WTF")
                return False
            for elem in self.productions[k]:
                alpha = elem[0].split()
                for a in alpha:
                    if a == 'E' or a in self.terminals or a in self.nonTerminals:
                        continue
                    else:
                        return False
        return True

    def print_productions_for_nonTerminal(self, nonT):
        print('Productions for non-terminal "' + str(nonT) + '": ')
        theStr = ''
        for k in self.productions.keys():
            if k == nonT:
                theStr += nonT + ' -> '
                for t in self.productions[nonT]:
                    theStr += t[0] + ' | '
                theStr = theStr[:-3] + '\n'
        print(theStr)

    def get_productions_for_nonTerminal(self, nonT):
        prods = []
        for k in self.productions.keys():
            if k == nonT:
                for t in self.productions[nonT]:
                    prods.append(t[0])
        return prods

    def __str__(self):
        return '\nGrammar:\nnon terminal = { ' + ', '.join(self.nonTerminals) + ' }\n' \
               + 'terminal = { ' + ', '.join(self.terminals) + ' }\n' \
               + 'starting = ' + str(self.starting) + '\n' \
               + 'productions = { \n' + self.getProductionString() + '}\n'


