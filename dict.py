empty={}
type(empty)
empty==dict()
a=dict(one=1,two=2,three=3)
b={"one": 1, "two": 2, "three": 3}
print(a==b)

##name=dict(Firstname=Hina, Lastname=Chowrasia, achievement=prize)
about_me={"Firstname":'Hina', "Lastname":'Chowraisa', "achievement": 'prize'}
about_me['Firstname']='Riya'
about_me['Skill']='html'
print(about_me)
##print(about_me['one'])
print(about_me['Firstname'])

#...creating dictionaries using list...##
d={"CS":[106, 107, 110], "MATH":[51,110]}
print(d.get("CS"))
print(d.get("MATH"))

english_classes=d.get("ENGLISH", [])
num_english=len(english_classes)
print(num_english)

##.....DELETE in Dict....###

d={"one": 1, "two": 2, "three": 3}
del d["one"]
print(d)

##....POP in dict...####
d={"one": 1, "two": 2, "three": 3}
d.pop("one")
d.popitem()
print(d)

##....show the dict value..##
d={"one": 1, "two": 2, "three": 3}
print(d.keys())
print(d.values())
print(d.items())
##print(len(d.keys())
      ##('one',1) in d.items()
for value in d.items():
      print(value)




