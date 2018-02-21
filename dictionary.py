#Dictionary literals

#Perhaps the most commonly used way of constructing a python dictionary is with curly bracket syntax:


d = {"age":25}


#As dictionaries are mutable, you need not know all the entries in advance:
 
# Empty dict
d = {}
# Fill in the entries one by one
d["age"] = 25


#From a list of tuples

#You can also construct a dictionary from a list (or any iterable) of key, value pairs. For instance:
 
d = dict([("age", 25)])
 

#This is perhaps most useful in the context of a list comprehension:

 
class Person(object):
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
 
people = [Person("Nick", "Programmer"), Person("Alice","Engineer")]
professions = dict([ (p.name, p.profession) for p in people ])
>>> print professions
{"Nick": "Programmer", "Alice": "Engineer"}
 

#This is equivalent, though a bit shorter, to the following:
 
people = [Person("Nick", "Programmer"), Person("Alice","Engineer")]
professions = {}
for p in people:
    professions[p.name] = p.profession
 
 
#From two parallel lists
#This method of constructing a dictionary is intimately related to the prior example. Say you have two lists of elements, perhaps pulled from a database table:

# Static lists for purpose of illustration
names = ["Nick", "Alice", "Kitty"]
professions = ["Programmer", "Engineer", "Art Therapist"]
 
#If you wished to create a dictionary from name to profession, you could do the following:
 
professions_dict = {}
for i in range(len(names)):
    professions_dict[names[i]] = professions[i]
 

#This is not ideal, however, as it involves an explicit iterator, and is starting to look like Java. The more Pythonic way to handle this case would be to use the zip method, which combines two iterables:
 
print zip(range(5), ["a","b","c","d","e"])
[(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e")]
 
names_and_professions = zip(names, professions)
print names_and_professions
[("Nick", "Programmer"), ("Alice", "Engineer"), ("Kitty", "Art Therapist")]
 
for name, profession in names_and_professions:
    professions_dict[name] = profession
 
#As you can see, this is extremely similar to the previous section. You can dispense the iteration, and instead use the dict method:
 
professions_dict = dict(names_and_professions)
# You can dispence the extra variable and create an anonymous
# zipped list:
professions_dict = dict(zip(names, professions))
 

