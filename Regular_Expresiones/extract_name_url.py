import re  

"""
    TODO re.sub(pattern, repl, string, count=0, flags=0)
"""

url = input("-> URL: ").strip()
username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")