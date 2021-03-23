import re

pattern = r"<a\s+(?:[^>]*?)href=\"([^\"]*)\""
string = """
<a href="4513.html">4513</a>
<a target="_blank" href="myojin.png">koko</a>
<a href="kanejun.tex">erotech</a>
"""

result = re.findall(pattern, string) # 検索
print(result) # ['4513.html', 'myojin.png', 'kanejun.tex']