class AdvancedPropotionalInference:

    def needCNF(self,sentence=''):
        for word in sentence:
            if(word == '&' or word == '#' or word == '$'):
                return True;
        return False;

    def EliminateDoubleNegation(self,sentence=''):
        newsentence = sentence;
        sentence = '';
        while(newsentence != sentence):
            sentence = newsentence;
            for i in range(sentence.__len__()):
                if(sentence[i] == '~'):
                    pos = 0;
                    for j in range(i,sentence.__len__()):
                        if(sentence[j] != '~'):
                            pos = j;
                            break;
                    if(pos-i == 1):
                        continue;
                    if(pos-i % 2 == 0):
                        newsentence = sentence[:i]+sentence[j:];
                        break;
                    if(pos-i % 2 == 1):
                        newsentence = sentence[:i+1]+sentence[j:];
                        break;
        return newsentence;

    def Conversion_sentence(self,sentence=''):
        res = set();
        if(not self.needCNF(sentence)):
            sentence = self.EliminateDoubleNegation(sentence)
            res.add(sentence);
            return res;
        if(sentence[0] == '('):
            count = 0;
            pos = 0;
            for i in range(sentence):
                if(sentence[i] == '('):
                    count += 1;
                if(sentence[i] == ')'):
                    count -= 1;
                if(count == 0):
                    pos = i;


    def PL_Resolution(self,knowledge_base,alpha):
        pass;

    def isSupplement(self,symbol1='',symbol2=''):
        if(symbol2.__len__() == 2 and symbol1.__len__() == 2):
            return False;
        if(symbol1.__len__() > 2 or symbol2.__len__() > 2):
            return False;
        if(symbol1[symbol1.__len__()-1] == symbol2[symbol2.__len__()-1]):
            if(symbol1[0] == '~' or symbol2[0] == '~'):
                return True;
        return False;


    def PL_Resolve(self,sentence1='',sentence2=''):
        l1 = set();
        l2 = set();
        hasguijie = False;
        sentence1 += '|';
        sentence2 += '|';
        res = [];
        pos = 0;
        for i in range(sentence1.__len__()):
            if(sentence1[i] == '|'):
                l1.add(sentence1[pos:i]);
                pos = i+1;
        pos = 0;
        for i in range(sentence2.__len__()):
            if(sentence2[i] == '|'):
                l2.add(sentence2[pos:i]);
                pos = i+1;
        for symbol1 in l1:
            for symbol2 in l2:
                if(self.isSupplement(symbol1,symbol2)):
                    if(l1.__len__() == 1 and l2.__len__() == 1):
                        return True,'';
                    hasguijie = True;
                    '''
                    tmp = l1 | l2;
                    tmp.discard(symbol1);
                    tmp.discard(symbol2);
                    '''
                    l3 = l1.copy();
                    l4 = l2.copy();
                    l3.discard(symbol1);
                    l4.discard(symbol2);
                    tmp = l3|l4
                    if(tmp.__len__() == 0):
                        return True,'';
                    res.append(tmp);
        if(res.__len__()>1):
            return False,'';
        if(res.__len__()==0):
            return False,''
        else:
            s = ''
            for i in res[0]:
                s += i+'|';
            return False,s[:s.__len__()-1];

#    class Resolution_based:
    def pl_resolution(self, knowledgebase=[], beta=[]):
        clauses = set()
        new = set()
        self.tempt = ''
        # clauses.append(str(knowledgebase))
        # clauses.append('~'+str(beta))
        for i in range(len(knowledgebase)):
            clauses.add(knowledgebase[i])
        # beta.append(beta)
        # for i in range(len(beta)):
        #     clauses.append('~'+beta[i])
        # print(len(beta))
        i = 0
        while i < len(beta):
            if beta[i] == '~':
                self.tempt = self.tempt + beta[i + 1]
                i = i + 2
            elif beta[i] >= 'A' and beta[i] <= 'Z':
                self.tempt = self.tempt + '~' + beta[i]
                i = i + 1
            else:
                self.tempt = self.tempt + beta[i]
                i = i + 1
            # print('tempt='+self.tempt)
        clauses.add(self.tempt)
        print(str(clauses))
        while(1):
            old_clauses = clauses.copy();
            for i in old_clauses:
                if(self.isSupplement(i,i)):
#                    old_clauses.discard(i);
                    continue;
            #for i in range(len(clauses) - 1):
    #            j = i + 1
    #            while j < len(clauses):
                for j in old_clauses:
                    if i == j:
                        continue;
                    if(self.isSupplement(j,j)):
#                        old_clauses.discard(j);
                        continue;
                    resolvents = self.PL_Resolve(i, j)
                    if resolvents[0] == True:
                        return True
                    else:
                        if(resolvents[1] == ''):
                            continue;
                        print(i,' and ',j,' produce resolvents=',resolvents[1])
                        if(self.isSupplement(resolvents[1],resolvents[1])):
                            continue;
                        new.add(resolvents[1])
            count=0
            for i in new:
                if i in old_clauses:
                    count+=1
            if count==new.__len__():
                return False
            else:
                for i in new:
                    old_clauses.add(i)
                clauses=old_clauses;
#                print(clauses)

knowledgebase = [
     '~A',
    '~F|~B|~D',
    '~B|F',
    '~D|F',
    '~G|A|C|E',
    '~A|G',
    '~C|G',
    '~E|G',
    '~F',
    'G'

]
beta = []
print("enter beta:")
b = input()
for i in b:
    beta.append(i)
# print(str(beta))
# print(len(beta))
a = AdvancedPropotionalInference()
if a.pl_resolution(knowledgebase,beta):
    print("True")
else:
    print('False')

# tmp = AdvancedPropotionalInference();
# b,c= tmp.PL_Resolve('P|~Q','~P|Q');
# print(b)
# if(b):
#     print('empty');
# else:
#     print(c);