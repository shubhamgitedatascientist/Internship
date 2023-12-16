#!/usr/bin/env python
# coding: utf-8

# # Regular Expressions Assignment
Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
Sample Text- 'Python Exercises, PHP exercises.'
Expected Output: Python:Exercises::PHP:exercises:

# In[1]:


import re
Test_string='Python Exercises, PHP exercises.'
pattern = r"\s|[,.]"
result=re.sub(pattern,":",Test_string)
print(result)

Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
Expected output-
0      hello world
1             test
2    four five six
# In[3]:


import pandas as pd
data= {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df = pd.DataFrame(data)
pattern=r"[A-Z0-9,!:;.]"
result=df.replace(to_replace=pattern,value="",regex=True)
print(result)

Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.
# In[22]:


Test_string= "python to find all words that are at least 4 characters"
pattern=r"\w{4,}"
regex_pattern=re.compile(pattern)
result=regex_pattern.findall(Test_string)
print(result)

Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.
# In[23]:


Test_string= "python to find all words that are at least 4 characters"
str_pattern=r"\b\w{3,5}\b"
regex_pattern1=re.compile(str_pattern)
result=regex_pattern1.findall(Test_string)
print(result)

Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
Expected Output:
example.com
hr@fliprobo.com
github.com
Hello Data Science World
Data Scientist
# In[6]:


Test_string= ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
str_pattern=r"[()]"
regex_pattern2=re.compile(str_pattern)
for unwanted in Test_string:
    result=re.sub(regex_pattern2,"",unwanted)
    print(result)

Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
Note- Store given sample text in the text file and then to remove the parenthesis area from the text.

# In[75]:


import re
Text_file = open("myfile.txt", "w")
L = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
 
Text_file.writelines(L)
Text_file.close() 
 
Text_file = open("myfile.txt", "r+")
read_file = Text_file.read()
str_pattern=r" ?\([^)]+\)"
result=re.sub(str_pattern," ",read_file)
print(result.split(" "))

Question 7- Write a regular expression in Python to split a string into uppercase letters.
Sample text: “ImportanceOfRegularExpressionsInPython”
Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]

# In[25]:


import re
Test_string="ImportanceOfRegularExpressionsInPython"
result=re.findall('.[^A-Z]*', Test_string)
print(result)

Question 8- Create a function in python to insert spaces between words starting with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

# In[25]:


import re
Test_string="RegularExpression1IsAn2ImportantTopic3InPython"
result = re.sub(r'(\d+)',r' \1', Test_string)
print(result)

Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython

# In[20]:


import re
Test_string="RegularExpression1IsAn2ImportantTopic3InPython"
result = re.sub('(\d+)', r' \1 ', Test_string)
print(result)

Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv

# In[27]:


import pandas as pd
url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)
df['first_five_letters'] = df['Country'].apply(lambda x: x[:6])
print(df.head())

Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
# In[33]:


import re
def text_match(text):
        patterns = '^[\w]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))

Question 12- Write a Python program where a string will start with a specific number. 
# In[36]:


import re
def match_num(string):
    text = re.compile(r"^523")
    if text.match(string):
        return True
    else:
        return False
print(match_num('52345861'))
print(match_num('62345861'))

Question 13- Write a Python program to remove leading zeros from an IP address
# In[27]:


import re
Test_string = "216.08.094.196"
result = re.sub('\.[0]*', '.', Test_string)
print(result)

Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
Expected Output- August 15th 1947
Note- Store given sample text in the text file and then extract the date string asked format.

# In[141]:


import re

text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."

pattern = r"\b[A-Z][a-z]+ \d{1,2}(?:st|nd|rd|th)? \d{4}\b"

matches = re.findall(pattern, text)
print(matches)

Question 15- Write a Python program to search some literals strings in a string. 
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'
# In[30]:


import re
patterns = [ 'fox', 'dog', 'horse' ]
Test_string = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, Test_string),)
    if re.search(pattern,  Test_string):
        print('Matched!')
    else:
        print('Not Matched!')

Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'

# In[31]:


import re
pattern = 'fox'
Test_string = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, Test_string)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))


# In[ ]:


Question 17- Write a Python program to find the substrings within a string.
Sample text : 'Python exercises, PHP exercises, C# exercises'
Pattern : 'exercises'.


# In[32]:


import re
Test_string = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, Test_string):
    print('Found "%s"' % match)

Question 18- Write a Python program to find the occurrence and position of the substrings within a string.
# In[33]:


import re
Test_string = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, Test_string):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (Test_string[s:e], s, e))

Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
# In[54]:


import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))

Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']

# In[67]:


def find_decimal_numbers(string):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    decimal_numbers = re.findall(pattern, string)
    return decimal_numbers
sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
output = find_decimal_numbers(sample_text)
print(output)

Question 21- Write a Python program to separate and print the numbers and their position of a given string.
# In[34]:


import re
Test_string = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
for m in re.finditer("\d+", Test_string):
    print(m.group(0))
    print("Index position:", m.start())

Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
Expected Output: 950
# In[35]:


import re
Test_string='My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
numbers=re.findall('\d+',Test_string)
print(max(map(int,numbers)))

Question 23- Create a function in python to insert spaces between words starting with capital letters.
Sample Text: “RegularExpressionIsAnImportantTopicInPython"
Expected Output: Regular Expression Is An Important Topic In Python

# In[82]:


import re 
Test_string = "RegularExpressionIsAnImportantTopicInPython"
def addSpace(input):  
    result = re.findall('[A-Z][a-z]*', Test_string) 
    for i in range(0,len(result)):
      result[i]=result[i][0:]
    print(' '.join(result))
addSpace(Test_string)

Question 24- Python regex to find sequences of one upper case letter followed by lower case letters
# In[80]:


import re
def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("AaBbGg"))
print(text_match("python"))

Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
Sample Text: "Hello hello world world"
Expected Output: Hello hello world

# In[79]:


Test_string = 'Hello hello world world'
regex = "\\b(\\w+)(?:\\W+\\1\\b)+"
result = re.sub(regex, r'\1', Test_string)
print(result)

Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.
# In[68]:


import re
Test_string = 'Hello_hello0world7world'
regex = '[a-zA-z0-9]$'
if(re.findall(regex,Test_string)):
    print("Accept")
else:
    print("reject")

Question 27-Write a python program using RegEx to extract the hashtags.
Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']

# In[39]:


import re 
Test_string = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
result = re.findall('#[a-zA-Z]+',Test_string)
print(result)

Question 28- Write a python program using RegEx to remove <U+..> like symbols
Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders

# In[40]:


import re
Test_string = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
result = re.sub(r"<U\+\w{4}>","",Test_string)
print(result)

Question 29- Write a python program to extract dates from the text stored in the text file.
Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
Note- Store this sample text in the file and then extract dates.

# In[61]:


import re
file1 = open("myfile.txt", "w")
L = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."
 
file1.writelines(L)
file1.close() 
 
file1 = open("myfile.txt", "r+")
 
read_file = file1.read()
str_pattern=r'\d+[-]\d+[-]\d+'
result=re.findall(str_pattern,read_file)
print(result)

Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
The use of the re.compile() method is mandatory.
Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.

# In[42]:


import re
Test_string = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
result = re.compile(r'\W*\b\w{2,4}\b')
print(result.sub('', Test_string))

