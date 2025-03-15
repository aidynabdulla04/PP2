import re
#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
txt = "the ii in accb abb a_a_a AdhAa Aabsdsd"
x = re.search(r"ab*", txt)
print(x)
#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
x = re.search(r"ab{2,3}", txt)
print(x)
#Write a Python program to find sequences of lowercase letters joined with a underscore.
x = re.findall(r"[a-z](?:[_][a-z])+", txt)
print(x)
#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
x = re.findall(r"[A-Z]{1}[a-z]+", txt)
print(x)
#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
x = re.search(r"\ba[a-z]+b\b", txt)
print(x)
#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
txt = "The, rain.in Spain"
x = re.sub("\s", ":", txt)
x = re.sub(",", ":", x)
x = re.sub("\.", ":", x)
print(x)
#Write a python program to convert snake case string to camel case string.
def repl(m): 
    return m[0][1].upper()
txt = "The_rain_in_Spain"
txt=txt.casefold()
txt=txt.capitalize()
x = re.sub(r"_[a-z]", repl, txt)
print(x)
#Write a Python program to split a string at uppercase letters.
txt = "the ii in accb abb a_a_a AdhAa Aabsdsd"
x = re.split("[A-Z]", txt)
print(x)
#Write a Python program to insert spaces between words starting with capital letters.
def rep(m): 
    return m[0][0]+" "+m[0][1]
txt = "TheRainInSpain"
x = re.sub(r"[a-z][A-Z]",rep, txt)
print(x)
#Write a Python program to convert a given camel case string to snake case.
def snake(m): 
    return "_"+m[0][0].lower()
txt = "theRainInSpain"
x=re.sub(r"[A-Z]",snake,txt)
print(x)











