print("Hello World!")

def func(n):
    print(n)

func(4)

# object types / datatypes
# number : 1234, 3.14, 3+4j, 0b111, decimal(), fraction()
# string : 'spam', "bob's", b'a\x01c', u'sp\xc4m'
# list : [1, [2, 'three'], 4.5], list(Range(10))
# tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
# Dictionary : {'food': 'spam', 'taste': 'yum'}, (hours=10)
# set : set('abc'), {'a', 'b', 'c'}
# File : open('eggs.txt'), open('eggs.txt', 'w')
# Boolean : True, False
# None : None
# Function, modules, classes, instances, exceptions
# advance: Decorators, generators, iterators, metaprogramming

# we dont assign data types to variables, we assign references to objects
# there is data type assigned inside the memory and it only exists in the memory

# eg : l1 - [1, 2, 3] l2 - l1
# l1 - one l2 - [1, 2, 3] ; l1 - [1, 2, 3] 
# l2 and l1 both shows [1, 2, 3] but they are not same object why? because l1 was changed once
# l1[0] = 33 ; l1 - [33, 2, 3] ; l2 - [1, 2, 3]

# eg : l1 - [1, 2, 3] l2 - l1
# l1 - [1, 2, 3] l2 - [1, 2, 3] 
# l1[0] = 44 ; l1 - [44, 2, 3] ; l2 - [44, 2, 3] the same object is referenced by both l1 and l2

# h1 = [1, 2 , 3] h2 = h1[:] ->means we have made a copy, : with no value means take full array, this can be also used in slicing
# h1[0] = 55; h1 - [55, 2, 3] h2 - [1, 2, 3]

# m == n -> checks the value ; m is n -> checks if the object in the memory is also same
#  2 ** 100 - > it calculates 2 power 100
# repr, str , print differences check from google

# math.floor -> (3.5) -> 3
# math.trunc -> (-2, 8) -> -2 value that comes first on no. line
# it also handles imaginary nos -> 2 + 3j
# random.randint(1, 10) -> it gives random no. b/w 1 to 10

# type of empty parenthesis is dictionary
# num = "0123456789" -> num[0 : 7 : 2] -> '0246' -> no sliced from 0 to 6 and hopping of 2
# name = '   thevaishndra   ' -> print(name.strip())
# chai = ['lemon,' 'ginger,' 'masala,' 'mint,']  print(chai.split(",")) -> ['lemon', 'ginger', 'masala', 'mint']
# print("".join(chai_variety)) -> LemonMasalaGinger
# for letter in chai:   print(letter) -> M A S A L A  C H A I

# chai = "He said, \"Masala chai is awesome\" " ->It basically means to ignore double inverted commas from Masala to awesome
# chai = 'He said, "Masala Chai is awesome" '
# chai = r"Masala\nChai" -> Masala\nchai
