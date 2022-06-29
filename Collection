from InvertedIndex import InvInd

class Collection:
    def __init__(self, name):
        self.indexes = InvInd()
        self.name = name
        self.documents = []
    def insert(self,val):
        dname = ""
        if len(self.documents)==0:
            self.documents.append(1)
            dname = "d1"
        else:
            dname = "d"+str(self.documents[len(self.documents)-1]+1)
            self.documents.append(self.documents[len(self.documents)-1]+1)
        words = val.split(" ")
        visited = []
        res = []
        for i in range(len(words)):
            if words[i] not in visited and words[i] != "":
                visited.append(words[i])
                res.append([i])
            elif words[i] in visited:
                ind = visited.index(words[i])
                res[ind].append(i)
        for i in range(len(res)):
            self.indexes.add(visited[i],dname,res[i])
        return dname
    def printInd(self):
        print(self.indexes.printInd())
    def search(self,w1,w2,arg):
        if w1 == "&":
            res = []
            for el in self.documents:
                res.append("d"+str(el))
            return res

        if w2 == "&":
            res = self.indexes.searhW(w1)
            return res
        elif arg == "-":
            res = self.indexes.searchBW(w1,w2)
            return res
        elif arg != "&":
            res = self.indexes.searchRange(int(arg),w1,w2)
            return res

