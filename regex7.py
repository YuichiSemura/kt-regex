import re

pattern = r"<(.*?)\s.*?>*?</\1>"
string = """
<div class="token"><p>4513</p></div>
"""

result = re.search(pattern, string) # 検索
if result:
    print(result.group()) # <div class="token"><p>4513</p></div>