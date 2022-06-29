import re

CREATE_TEMPLATE = r"[cC][rR][eE][aA][tT][eE]\s+(?P<name>[0-9a-zA-Z_]+)\s*"
PRINT_TEMPLATE = r"[pP][rR][iI][nN][tT][_][iI][nN][dD][eE][xX]\s+(?P<name>[0-9a-zA-Z_]+)\s*"
INSERT_TEMPLATE = r"[iI][nN][sS][eE][rR][tT]\s+(?P<name>[0-9a-zA-Z_]+)\s+\"(?P<value>[^\"]*)\"\s*"
SEARCH_TEMPLATE1 = r"[sS][eE][aA][rR][cC][hH]\s+(?P<name>[0-9a-zA-Z_]+)\s*$"
SEARCH_TEMPLATE2 = r"[sS][eE][aA][rR][cC][hH]\s+(?P<name>[0-9a-zA-Z_]+)\s+[wW][hH][eE][rR][eE]\s+\"(?P<value>[0-9a-zA-Z_]*)\"\s*$"

SEARCH_TEMPLATE3 = r"[sS][eE][aA][rR][cC][hH]\s+(?P<name>[0-9a-zA-Z_]+)\s+[wW][hH][eE][rR][eE]\s+" \
                   r"\"(?P<value1>[0-9a-zA-Z_]*)\"\s*(?P<arg>[\-]{1})\s*\"(?P<value2>[0-9a-zA-Z_]*)\"\s*$"
SEARCH_TEMPLATE4 = r"[sS][eE][aA][rR][cC][hH]\s+(?P<name>[0-9a-zA-Z_]+)\s+[wW][hH][eE][rR][eE]\s+"\
                    r"\"(?P<value1>[0-9a-zA-Z_]*)\"\s*<(?P<arg>[1-9][0-9]*)>\s*\"(?P<value2>[0-9a-zA-Z_]*)\"\s*$"


def parse(str0):
    res = [-1,"Null input"]
    temp = re.search(CREATE_TEMPLATE, str0)
    if temp is not None:
        res[0]=1
        res[1]=temp.group("name")
        return res
    temp = re.search(INSERT_TEMPLATE,str0)
    if temp is not None:
        res[0]=2
        res[1]=temp.group("name")
        val = temp.group("value")
        val = re.sub("[^0-9a-zA-Z_\s]"," ",val)
        val = re.sub("\s+"," ",val)
        val = val.strip()
        res.append(val)
        return res
    temp = re.search(PRINT_TEMPLATE, str0)
    if temp is not None:
        res[0] = 3
        res[1] = temp.group("name")
        return res
    temp = re.search(SEARCH_TEMPLATE3, str0)
    if temp is not None:
        res[0] = 4
        res[1] = temp.group("name")
        res.append(temp.group("value1").lower())
        res.append(temp.group("value2").lower())
        res.append(temp.group("arg"))
        return res
    temp = re.search(SEARCH_TEMPLATE4, str0)
    if temp is not None:
        res[0] = 4
        res[1] = temp.group("name")
        res.append(temp.group("value1").lower())
        res.append(temp.group("value2").lower())
        res.append(temp.group("arg"))
        return res
    temp = re.search(SEARCH_TEMPLATE2, str0)
    if temp is not None:
        res[0] = 4
        res[1] = temp.group("name")
        res.append(temp.group("value").lower())
        res.append("&")
        res.append("&")
        return res
    temp = re.search(SEARCH_TEMPLATE1, str0)
    if temp is not None:
        res[0] = 4
        res[1] = temp.group("name")
        res.append("&")
        res.append("&")
        res.append("&")
        return res
    res[1] = "unknown command!"
    return res

    return
