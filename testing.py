import re
# email= "pawan.negi2022@vit.com"
email= "pawan.negi2022@infosys.com"

# match = re.search(r"[\w._]+@vit\.com", email)
# match = re.search(r"[\w._]+@vitstudent\.ac\.in", email)
match = re.search(r"[a-zA-Z0-9.-_]+@[a-zA-Z-]+\.(com|edu|net)$",email)

if match:
    print("Valid email")
else:
    print("not valid email")
