import re
from parser0 import parse
from Collection import Collection

def add_coll(name,Colls):
    for el in Colls:
        if el.name == name:
            print("Collection with name = "+name + " already exists!")
            return
    Colls.append(Collection(name))
    print("Collection "+name + " was successfully created!")

def insert(name,value,Colls):
    ind = -1
    for i in range(len(Colls)):
        if Colls[i].name == name:
            ind = i
    if ind == -1:
        print("Collection with name = "+name + " does not exist!")
        return

    if value=="":
        print("Value is empty! Aborted!")
        return
    dname = Colls[ind].insert(value)
    print(value + " was successfully inserted in collection "+name + " with name "+dname)

def printInd(name,Colls):
    ind = -1
    for i in range(len(Colls)):
        if Colls[i].name == name:
            ind = i
    if ind == -1:
        print("Collection with name = " + name + " does not exist!")
        return
    print("Indexes for collection "+name+" :")
    Colls[ind].printInd()

def search(name,w1,w2,arg,Colls):
    ind = -1
    for i in range(len(Colls)):
        if Colls[i].name == name:
            ind = i
    if ind == -1:
        print("Collection with name = " + name + " does not exist!")
        return
    Colls[ind].search(w1,w2,arg)
    print(str(Colls[ind].search(w1,w2,arg)))




def execute(command,arr,Colls):
    print("Result for command "+command+": ")
    if arr[0]==1:
        add_coll(arr[1],Colls)
    elif arr[0]==2:
        insert(arr[1],arr[2],Colls)
    elif arr[0]==3:
        printInd(arr[1],Colls)
    elif arr[0]==4:
        search(arr[1],arr[2],arr[3],arr[4],Colls)
    elif arr[0]==-1:
        print("Error = "+arr[1])
    else:
        print("Unknown error!")




if __name__ == '__main__':


    str0 =""
    save = ""
    Collections = []
    while True:
        str0 = input("Input command: ")
        str0 = save + str0
        if re.search("[.]exit",str0.lower()) is not None:
            print("Finished!")
            break
        commands= str0.split(";")
        for i in range(len(commands)):
            if i == len(commands)-1:
                save = commands[i]
                break
            execute(commands[i],parse(commands[i]),Collections)
