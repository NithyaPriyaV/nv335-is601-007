#this is a single line comment
"""
this 
is 
a
multi-line
comment
"""
print(type("Hi")) #prints <class 'str'>

x="hi"
x=5
print(x) #prints(5) as first it assignts hi but the latest write counts, hence hi will be printed. 

#casting example below
x= str(5)
print(x) #prints <class 'str'>

#functions example:
def say_it(a):
    a += x
    print(a)
say_it("Hi")
# the variables outside the scope of a function can be read, but not used/printed. 
#hence, solution below: declaring it global.
def say_it0(a):
    global x
    x += a
    print(x)
say_it0("Hi")
"""
What is a complex datatype? = Imaginary Number
"""
a=1
b=0
for i in range(10):
    b += 0.1
    print(b)

print(a == b)
#prints false due to floating point precision - happens due to cpu processings ==> Solution: Use Integer values instead as it wouldn't need rounding
