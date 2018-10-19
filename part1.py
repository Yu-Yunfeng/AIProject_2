class BasicModelChecking:
    def PL_TRUE(self,sentences=[],model={}):
        if(len(sentences) == 1):
            if(len(sentences[0]) <= 2):
                if(sentences[0] == ''):
                    return True;
                return model[sentences[0]];
        for sentence in sentences:
            '''
            if(len(sentence) <= 2):
                if(not model[sentence]):
                    return False;
                else:
                    continue;
            '''
            if(len(sentence) <= 2):
                if(not model[sentence]):
                    return False;
                else:
                    continue;
            A = '';
            B = '';
            connective = '';
            symbol_not = False;
            if(sentence[0] == '('):
                count = 1;
                pos = 0;
                for index in range(1,len(sentence)):
                    if(sentence[index] == '('):
                        count += 1;
                    if(sentence[index] == ')'):
                        count -= 1;
                    if(count == 0):
                        pos = index;
                        break;
                A = sentence[1:pos];
                if(pos+2<len(sentence)):
                    connective = sentence[pos+1];
                    B = sentence[pos+2:];
            elif(sentence[0] == '~' and sentence[1] == '('):
                count = 1;
                pos = 0;
                for index in range(2,len(sentence)):
                    if(sentence[index] == '('):
                        count += 1;
                    if(sentence[index] == ')'):
                        count -= 1;
                    if(count == 0):
                        pos = index;
                        break;
                A = sentence[2:pos];
                if(pos+2<len(sentence)):
                    connective = sentence[pos+1];
                    B = sentence[pos+2:];
                symbol_not = True;
            elif(sentence[0] == '~' and sentence[1] != '('):
                A = sentence[:2];
                connective = sentence[2];
                B = sentence[3:];
            else:
                A = sentence[0];
                connective = sentence[1];
                B = sentence[2:];

            l1 = [A];
            l2 = [B];
            bool_A = self.PL_TRUE(l1,model);
            bool_B = self.PL_TRUE(l2,model);
#            bool_AB = True;
            if(symbol_not):
                bool_A = not bool_A;
            if(connective == ''):
                return bool_A;
            if(connective == '&'):
                if(not bool_A or not bool_B):
                    return False;
            if(connective == '|'):
                if(not bool_A and not bool_B):
                    return False;
            if(connective == '#'):
                if(bool_A and not bool_B):
                    return False;
            if(connective == '$'):
                if(not bool_A and bool_B):
                    return False;
                if(not bool_B and bool_A):
                    return False;
        return True;

    def TT_Entail(self,knowledge_base=[],beta=[]):
        symbols = [];
        for sentence in knowledge_base:
            for char in sentence:
                if char>='A' and char<='Z':
                    if char not in symbols:
                        symbols.append(char);
        return self.TT_Check_All(knowledge_base,beta,symbols,{});

    def TT_Check_All(self,knowledge_base=[],beta=[],symbols=[],model={}):
        if(len(symbols) == 0):
            if(self.PL_TRUE(knowledge_base,model)):
                return self.PL_TRUE(beta,model);
            else:
                return True;

        P = symbols[0];
        rest = symbols[1:];

        model_1 = model.copy();
        model_2 = model.copy();
        model_1[P] = True;
        model_1["~"+P] = False;
        model_2[P] = False;
        model_2["~"+P] = True;

#        print(model_1," ",self.TT_Check_All(knowledge_base,beta,rest,model_1)," 1");
#        print(model_2," ",self.TT_Check_All(knowledge_base,beta,rest,model_2)," 2");
        return self.TT_Check_All(knowledge_base,beta,rest,model_1) and self.TT_Check_All(knowledge_base,beta,rest,model_2);


beta = [
    '~A',
    '~B',
    'C'
]

alpha = [
    'A&C',
    '~C',
    'B|~A'
]

b = BasicModelChecking();
if(b.TT_Entail(alpha,beta)):
    print("True");
if(not b.TT_Entail(alpha,beta)):
    print("False");