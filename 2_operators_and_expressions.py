#operators

#types
#arithemetic operators
'''
+ (addition)
- (subtraction)
* (multiplication)
/ (division)
% (modulo)
** (exponentiation)
// (floor division)
'''

#logical operators
'''
and
or
not
'''

#comparison operators
'''
== (equal to)
!= (not equal to)
> (greater than)
< (less than)
>= (greater than or equal to)
<= (less than or equal to)
'''

#eg.

print(10 + 5) #addition
print(10 - 5) #subtraction
print(10 * 5) #multiplication
print(10 / 5) #division
print(10 % 3) #modulo
print(2 ** 3) #exponentiation
print(10 // 3) #floor division

#difference between == and is
# == checks wheather two objects have the same value
# is checks whether two objects are the same object in memory.
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y) # True, because the values are the same
print(x is y) # False, because they are different objects in memory
print(x is z) # True, because z refers to the same object as x