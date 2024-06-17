
from collections import namedtuple,deque,ChainMap,Counter,OrderedDict
courses = namedtuple('courses',['name','tech'])
clist = courses(name='data science',tech='python')
print(clist[0])
print(clist.name)
print(getattr(clist,"tech"))
couselist=['web development','angular']
print(courses._make(couselist))

'Deque - it is an optimised list to perform insertion and deletion easily'
team_list=["rohit","virat","hardik","rahul"]
teqeue = deque(team_list)
print(teqeue)
teqeue.append("risha")
teqeue.appendleft("siraj")

print("After append",teqeue)
teqeue.pop()
teqeue.popleft()
print("After pop",teqeue)
'''chainmap - it is a dictionary like class which is able to make a single view'''
tmodule1 = {1:'angular',2:'python'}
tmodule2 = {3:'react',4:'cloud computing',5:'devops'}
module_list=ChainMap(tmodule1,tmodule2)
print(module_list)
tmodule3={6:"fundamentals",7:"docker"}
module_list=ChainMap(tmodule1,tmodule2,tmodule3)
print(module_list)
"""counter -it is a dictionary sub class which is used to count hash table objects"""
rohit_socores = [70,89,170,270,200,100,100,70,50,89,60,50,200]
scorecount=Counter(rohit_socores)
print(scorecount)
print(scorecount.keys())
print(scorecount.values())
print(scorecount.items())
""""""
tempod= OrderedDict()
tempod[1] = "17.10"
tempod[2] = "19.09"
print(tempod)