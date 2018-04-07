class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        import collections
        assert isinstance(e, collections.Hashable), 'input is not hashable'

        if e in self.vals.keys():
            self.vals[e] = self.vals[e]-1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        import collections
        assert isinstance(e, collections.Hashable), 'input is not hashable'

        return self.vals.get(e, 0)

    def __add__(self, value):
        assert isinstance(value, type(self))
        ans = Bag()
        for key in set(list(self.vals.keys()) + list(value.vals.keys())):
            r = self.vals.get(key, 0) + value.vals.get(key, 0)
            ans.vals[key] = r
            
        return ans

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        import collections
        assert isinstance(e, collections.Hashable), 'input is not hashable'
        
        self.vals.pop(e, 0)

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        import collections
        assert isinstance(e, collections.Hashable), 'input is not hashable'

        return e in self.vals.keys()

# Example 1
d1 = Bag()
d1.insert(4)
d1.insert(4)
assert d1.__str__() == "4:2\n"
print(d1)
d1.remove(2)
assert d1.__str__() == "4:2\n"
print(d1)

# Example 2
d1 = Bag()
d1.insert(4)
d1.insert(4)
d1.insert(4)
assert d1.count(2) == 0
print(d1.count(2))
assert d1.count(4) == 3
print(d1.count(4))

# Test 1
d1 = Bag()
d1.insert(4)
d1.remove(4)
d1.remove(4)
d1.remove(4)
print(">>:", d1)

# Problem 6-2
# Example 1
a = Bag()
a.insert(4)
a.insert(3)
b = Bag()
b.insert(4)
assert (a+b).__str__() == '3:1\n4:2\n'
print(a+b)


# Problem 6-3
# Example 1
d1 = ASet()
d1.insert(4)
d1.insert(4)

d1.remove(2)
assert d1.__str__() == "4:2\n"
print(d1)

d1.remove(4)
assert d1.__str__() == ""
print(d1)

# Example 2
d1 = ASet()
d1.insert(4)
assert d1.is_in(4) == True
print(d1.is_in(4))
d1.insert(5)
assert d1.is_in(5) == True
print(d1.is_in(5))
d1.remove(5)
assert d1.is_in(5) == False
print(d1.is_in(5))
