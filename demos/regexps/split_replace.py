import re

content = "red|green;blue:yellow"
r = re.compile(r"\||;|:")
print(r.split(content))
print(r.sub(",", content))

content = "red|green;blue:yellow"
r = re.compile(r"[|;:]")
print(r.split(content))
print(r.sub(",", content))
