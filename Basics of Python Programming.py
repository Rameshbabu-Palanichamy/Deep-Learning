#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lower case
message = "Hello World Welcome to Learn Python"
print(message.lower())


# In[2]:


print(message.upper())
print(message.count('Welcome'))
print(message.find('Welcome'))
new_message=message.replace("World","Universe")
print(new_message)


# In[3]:


Greetings = "Hello"
name = 'Rameshbabu'
message=Greetings+" "+name+"."
print(message)
format_message='{} {}.'.format(Greetings,name)
print(format_message)


# In[13]:


greetings=str(input('Enter Your Greetings:'))
name=str(input('Enter Your name:'))
format_string=f'{greetings},{name}.'
format_string_Caps=f'{greetings},{name.upper()}.'
print(format_string)
print(format_string_Caps)
print(dir(name))#methods available


# # LISTS, TUPLES, SETS, DICT

# In[20]:


courses = ['Artificial Intelligence','Machine Learning','Computer Vision','Natural Language Processing']
print(courses)
print(len(courses))
print(courses[3])
print(courses[-1])
print(courses[0:3])
print(courses[:3])
print(courses[3:])


# In[22]:


courses.append('Chatbot')
print(courses)
courses.insert(3,'Analytics')
print(courses)


# In[30]:


courses_1=['Pattern Matching','Recommendations']
courses.extend(courses_1)
print(courses)


# In[31]:


courses.remove('Chatbot')
print(courses)


# # Sort, Reverse

# In[49]:


courses.sort()
print(courses)
courses.reverse()
print(courses)
courses.append('Chatbot')
print(courses)
#popped=courses.pop()
#print("Value eliminated using pop: ", popped)


# In[43]:


#ascending order
numbers = [1,4,2,6,5,0,8]
numbers.sort()
print("Ascending : ",numbers)
#Descending order
numbers.sort(reverse=True)
print("Desc :",numbers)


# In[44]:


#sorted method will not disturb parent records.
sorted_num = sorted(numbers)
print(sorted_num)


# In[47]:


#min,max,sum
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(numbers.index(4))
print(23 in numbers)
print(8 in numbers)


# In[50]:


# to get index and values using enumarate fn
for index,course in enumerate(courses):
    print(index,course)


# In[53]:


for index,course in enumerate(courses, start=1):
    print(index,course)
course_concat = "-".join(courses)
print(course_concat)
split_course= course_concat.split("-")
print(split_course)


# # Lists[] are mutable, Tuples() are immutable, SETS{} not allow duplicates

# In[54]:


set_courses= {'Recommendations', 'Recommendations', 'Pattern Matching', 'Pattern Matching', 'Natural Language Processing', 'Machine Learning', 'Computer Vision', 'Artificial Intelligence', 'Analytics', 'Chatbot'}
print(set_courses)


# In[57]:


art_courses={'Natural Language Processing', 'Artificial Intelligence', 'Computer Vision', 'Analytics','Systemm Design','Algorithms'}
print("Courses common in both set_courses & art_course :",set_courses.intersection(art_courses))
print("Courses not common in both set_courses & art_course :",set_courses.difference(art_courses))
print("Courses provided by both set_courses & art_course :",set_courses.union(art_courses))


# In[80]:


student = {'name':'Rameshbabu', 'Age':38,'Profession':'Data Scientist','courses':['AI','ML']}
student.update({'name':'Rameshbabu', 'Age':37,'phone':9191919191,'courses':['AI','ML','CV']})
del student['phone']
print(student['name'])
print(student['courses'])
print(student.get('Age'))
print(student.get('phone', 'Not Found'))
print(student.keys())
print(student.values())
print(student.items())
for key in student:
    print(key)
for key,value in student.items():
    print(key,value)


# In[83]:


# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


#and,or,not


Language = str(input('Enter the Programming Language :'))
if Language == 'Python':
    print ('Language known is Python')
elif Language == 'JavaScript':
    print ('Language known is JavaScript')
elif Language == 'Java':
    print ('Language known is Java')
else:
    print('Language known differs from Python/Java/Java Script')


# In[84]:


user=str(input('Enter username : '))
logged_in=True

if user=='Admin' and logged_in:
    print('Welcome to Admin Page')
else:
    print("Bad Credentials")


# In[85]:


user=str(input('Enter username : '))
logged_in=False

if user=='Admin' and logged_in:
    print('Welcome to Admin Page')
else:
    print("Bad Credentials")


# In[86]:


user=str(input('Enter username : '))
logged_in=True

if user=='Admin' or logged_in:
    print('Welcome to Admin Page')
else:
    print("Bad Credentials")


# In[88]:


user=str(input('Enter username : '))
logged_in=True

if  not logged_in:
    print('Please Login')
else:
    print("Welcome")


# In[90]:


a=[1,2,3]
b=[1,2,3]
print(a is b)
print(id(a))
print(id(b))
b=a
print(id(a)==id(b))


# In[93]:


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.
condition = " "
if condition:
    print("Elevated to True")
else:
    print("Elevated to False") 
    
condition_1 = ""
if condition_1:
    print("Elevated to True")
else:
    print("Elevated to False") 


# In[96]:


num = [1,2,3,4,5,6]
for numb in num:
    if numb==5:
        print("Found !")
        break
    print(numb)


# In[97]:


num = [1,2,3,4,5,6]
for numb in num:
    if numb==3:
        print("Found !")
        continue
    print(numb)


# In[98]:


for numb in num:
    for letters in "abc":
        print(numb,letters)


# In[100]:


x=10

while x<60:
    if x==55:
        break
    print(x)
    x+=5


# In[101]:


x=10

while True:
    if x==55:
        break
    print(x)
    x+=5


# In[102]:


def hello_function(greeting):
    return '{} Function.'.format(greeting)
print(hello_function("Hi"))


# In[103]:


def hello_function(greeting,name='You'):
    return '{}, {}'.format(greeting,name)
print(hello_function("Hey"))
print(hello_function("Hey", "Ramesh"))


# In[104]:


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
student_info('Maths','Science',name='Ramesh',age=37)


# In[105]:


courses=['Maths', 'Science']
info={'name': 'Ramesh', 'age': 37}
student_info(*courses,**info)


# In[106]:


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


# In[108]:


print(is_leap(2021))
print(days_in_month(2017,2))
print(days_in_month(2016,2))


# #Given two numbers, write a Python code to find the Maximum of these two numbers.

# In[5]:




a= 4
b= 6
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
print(maximum(a,b))


# In[6]:


#Using max() function
maxi=max(a,b)
print(maxi)


# In[7]:


#Using Ternary Operator
print(a if a>b else b)


# # Python program to find the largest
# # number among the three numbers

# In[8]:


c=32
def maxim(a,b,c):
    if (a>b) and (a>c):
        return a
    elif (b>a) and (b>c):
        return b
    else:
        return c
print(maxim(a,b,c))


# In[9]:


#Using List
def maxim(a,b,c):
    list=[a,b,c]
    return max(list)
print(maxim(a,b,c))


# In[10]:


print(max(a,b,c))


# Python Program for factorial of a number 
# 
# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.

# In[11]:


#Recursive
num =5
def factorial(n):
    return 1 if(n==1 or n==0) else n * factorial(n-1);
print("Factorial of",num,"is:")
factorial(num)


# In[ ]:




