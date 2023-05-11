import re
phn= "625-244-8788"

match= re.search(r"[9876]{3}-\d{3}-\d{4}",phn)
# match2= re.search(r"[9876]\d{2}-\d{3}-\d{4}",phn)
match2= re.search(r"\d{3}-\d{3}-\d{3}[9876]",phn)

if match:
    print("Valid phone 1")
else:
    print("not valid phone 1")
if match2:
    print("Valid phone 2")
else:
    print("not valid phone 2")
