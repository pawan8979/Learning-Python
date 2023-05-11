import re

email= "pawan.negi2022@infosys.com"

match = re.search(r"[a-zA-Z0-9.-_]+@([a-zA-Z-]+\.(com|edu|net))$", email)
if match:
    domain = match.group(1).split('.')
    # domain = match.group(1).split('@')
    print(domain[0])
