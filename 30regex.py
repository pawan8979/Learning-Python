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
matches= pattern.finditer(text_to_search)

for match in matches:
    print(match)
 
# Pattern matches phone number with . or - in data.txt file
with open("data.txt", "r") as f:
    contents = f.read()
    matches= pattern.finditer(contents)
    for match in matches:
        print(match)