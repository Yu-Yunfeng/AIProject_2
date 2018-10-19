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
                    hasguijie = True;
                    tmp = l1 | l2;
                    tmp.discard(symbol1);
                    tmp.discard(symbol2);
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

tmp = AdvancedPropotionalInference();
b,c= tmp.PL_Resolve('P|~Q','~P|Q');
print(b)
if(b):
    print('empty');
else:
    print(c);