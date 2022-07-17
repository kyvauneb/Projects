# Hashing allows us to map data of any size to a fixed length
## That fixed length integer is called a hash value

# The <object>.__hash__() method returns the hash value of the object if it has one
# An object is hashable if it has a hash value (memory address) that doesn't change during it's lifetime
## Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally
## Immutable built-in objects are hashable, mutable containers (dictionaries, lists, sets) are not
## Objects that are instances of user-defined classes are hashable by default
## They will all compare unequal, unless compared against themself; hash value is derived from their id (object’s address as present in the memory)

# If a class does not define an __eq__ method it should not define a __hash__ operation either; if it defines __eq__ but not __hash__, its instances will not be usable as items in hashable collections.
# Immutability: 
## Changes made to MUTABLE referenced objects (ex. values2 = values when both are lists) are made to the same address location in memory
## For IMMUTABLE objects, after copying by reference, the memory address of both variables will be the same; but after changing ones value, they'll be different
## "is" comparison is used to check if objects have the same memory address/identity/id, "==" is used to check if they have the same values
## Exception: Though tuples are immutable, we can change the value of a list (or other mutable container) in the tuple
### When we talk about the mutability of a container only the **identities** of the contained objects are implied


class User1: # note, we don't need to explicitly define __hash__ here because objects that are instances of user-defined classes are hashable by default

    def __init__(self, name, occupation):

        self.name = name
        self.occupation = occupation


u1 = User1('John Doe', 'gardener')
u2 = User1('John Doe', 'gardener')

print('hash of user 1')
print(hash(u1))

print('hash of user 2')
print(hash(u2))

if (u1 == u2):
    print('same user')
else:
    print('different users') # this will print; though the user details are the same, comparison yields different objects


class User2:

    def __init__(self, name, occupation):

        self.name = name
        self.occupation = occupation

    def __eq__(self, other): # since I define this, I won't be able to insert User2 objects into a set until I explicitly define a __hash__ method as well

        return self.name == other.name \
            and self.occupation == other.occupation # other is another instance of the User2 class

    def __str__(self):
        return f'{self.name} {self.occupation}'


u1 = User2('John Doe', 'gardener')
u2 = User2('John Doe', 'gardener')

if (u1 == u2):
    print('same user')
    print(f'{u1} == {u2}') # this will print
else:
    print('different users')

hashset = set()
# hashset.add(u1)  // TypeError: unhashable type: 'User2'

# users = {u1, u2}
# print(len(users))


class User3:

    def __init__(self, name, occupation):

        self.name = name
        self.occupation = occupation

    def __eq__(self, other):

        return self.name == other.name \
            and self.occupation == other.occupation

    def __hash__(self):
        return hash((self.name, self.occupation)) # now, the hash function is calculated from a tuple of attributes "name and occupation" as opposed to it's memory address/id

    def __str__(self):
        return f'{self.name} {self.occupation}'


u1 = User3('John Doe', 'gardener') #
u2 = User3('John Doe', 'gardener') # these will point to the same memory address, as we've defined the hash function to hash based off of the objects attributes

users = {u1, u2} # this will return a length of 1, as the users have the same attributes and therefore the same hash value

print(len(users))

if (u1 == u2):
    print('same user')
    print(f'{u1} == {u2}')
else:
    print('different users')

print('------------------------------------')

u1.occupation = 'programmer'

users = {u1, u2} # this will return a length of 2, as the users now have different attributes determining the hash value

print(len(users))

if (u1 == u2):
    print('same user')
    print(f'{u1} == {u2}')
else:
    print('different users')

skills = ["Programming", "Machine Learning", "Statistics"]
person = (129392130, skills)
print(type(person))
print(person)

print("Memory address of skills before edit: " + str(id(skills))) # shouldn't change - mutable
print("Memory address of person before 'skills' edit: " + str(id(person))) # shouldn't change, as we technically haven't changed the tuple, just a reference within


skills[2] = "Maths"
print(person)

print("Memory address of skills after edit: " + str(id(skills))) # shouldn't change - mutable
print("Memory address of person after 'skills' edit: " + str(id(person))) # shouldn't change, as we technically haven't changed the tuple, just a reference within

