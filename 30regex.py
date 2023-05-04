import re

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""
# pattern= re.compile(r"abc")
# pattern= re.compile(r"\.")
# pattern= re.compile(r"\d\d\d.\d\d\d.\d\d\d")
# pattern= re.compile(r"\d\d\d[-.]\d\d\d[-.]\d\d\d")
# pattern= re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d")
pattern= re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")
matches= pattern.finditer(text_to_search) #return match object with some extra functionality

for match in matches:
    print(match)

# findall:
# pattern= re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")
pattern= re.compile(r"\d{3}.\d{3}.\d{4}")
matches= pattern.findall(text_to_search) #just return matches as a list of strings
#If matching groups then only return groups

for match in matches:
    print(match)

# match:
sentence= "Start a sentence and tehn bring it to an end"
pattern= re.compile(r"Start")
matches= pattern.match(sentence) #only match at the beginning of the string

print(matches)

# search:
sentence= "Start a sentence and tehn bring it to an end"
pattern= re.compile(r"sentence")
pattern= re.compile(r"start", re.IGNORECASE) #check for pattern ignoring casing
pattern= re.compile(r"start", re.I) #short form
matches= pattern.search(sentence) #search the entire string for the pattern

print(matches)
 
# Pattern matches phone number with . or - in data.txt file
with open("data.txt", "r") as f:
    contents = f.read()
    matches= pattern.finditer(contents)
    for match in matches:
        print(match)