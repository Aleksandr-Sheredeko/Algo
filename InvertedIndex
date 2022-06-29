class InvInd:
    def __init__(self):
        self.left = None
        self.right = None
        self.word = ""
        self.values = []
        self.documents = []
    def add(self,w,d,p):
        if self.word == "" or self.word == w:
            self.word = w
            self.documents.append(d)
            self.values.append(p)
            return
        elif self.word < w:
            if self.right is None:
                self.right = InvInd()
            self.right.add(w, d, p)
        else:
            if self.left is None:
                self.left = InvInd()
            self.left.add(w, d, p)
    def searhW(self,w):
        if self.word.lower() == w:
            return self.documents
        elif self.word.lower()<w:
            if self.right is None:
                return []
            else:
                return self.right.searhW(w)
        else:
            if self.left is None:
                return []
            else:
                return self.left.searhW(w)
    def searhWv(self,w):
        resd = []
        resv = []
        if self.word.lower() == w:
            resd.extend(self.documents)
            resv.extend(self.values)
            if self.right is not None:
                temp = self.right.searhWv(w)
                resd.extend(temp[0])
                resv.extend(temp[1])
            if self.left is not None:
                temp = self.left.searhWv(w)
                resd.extend(temp[0])
                resv.extend(temp[1])
        elif self.word.lower()<w:
            if self.right is not None:
                temp = self.right.searhWv(w)
                resd.extend(temp[0])
                resv.extend(temp[1])
        else:
            if self.left is not None:
                temp = self.left.searhWv(w)
                resd.extend(temp[0])
                resv.extend(temp[1])
        return [resd,resv]
    def searchBW(self,w1,w2):
        res = []
        if w1<=self.word.lower()<=w2:
            res.extend(self.documents)
            if self.right is not None:
                res.extend(self.right.searchBW(w1, w2))
            if self.left is not None:
                res.extend(self.left.searchBW(w1,w2))
        elif self.word.lower() < w1:
            if self.right is not None:
                res.extend(self.right.searchBW(w1,w2))
        elif self.word.lower() > w2:
            if self.left is not None:
                res.extend(self.left.searchBW(w1, w2))

        ret = []
        for el in res:
            if el not in ret:
                ret.append(el)
        return ret
    def printInd(self):
        str0 =""
        str0+="\""+self.word+"\":\n"
        for i in range(len(self.documents)):
            str0+= str(self.documents[i]) + " -> "+str(self.values[i])+"\n"
        if self.left is not None:
            str0+= self.left.printInd()
        if self.right is not None:
            str0+=self.right.printInd()
        return str0
    def searchRange(self,r, w1, w2):
        res = []
        w1Res = self.searhWv(w1)
        w2Res = self.searhWv(w2)
        for i in range(len(w1Res[0])):
            for j in range(len(w2Res[0])):
                if w1Res[0][i] == w2Res[0][j]:
                    if w1Res[0][i] in res:
                        continue
                    for i1 in range(len(w1Res[1][i])):
                        if w1Res[0][i] in res:
                            break
                        for j1 in range(len(w2Res[1][j])):
                            if w1Res[0][i] in res:
                                break
                            if abs(w1Res[1][i][i1] - w2Res[1][j][j1]) == r:
                                res.append(w1Res[0][i])
        return res

