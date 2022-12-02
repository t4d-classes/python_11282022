import re

content = """<b>content 1</b><b></b>
<span>haptic is cool</span><b>content 2</b><div>fun</div>
<span>audio precision analyzer</span>
<span>(audio precision analyzer)</span>
"""

r = re.compile(r"<span>(?P<content>.*)</span>")

# r = re.compile(r"<b>(.+)</b>")

content = "Austin, TX 78701"

r = re.compile(r"^(?P<city>.*), (?P<state>.*) (?P<zip>.*)")

for match in r.finditer(content):
    print(match.groupdict())
