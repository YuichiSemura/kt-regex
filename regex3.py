import re

pattern = r'<p>.*?\(.*?\)</p>'
string = '<p>Yuichi Semura(full-stack engineer)</p>' # 検索対象文字列

# 全て検索し、文字列リストを返す
result = re.fullmatch(pattern, string)

if result:
    print(result.group()) # <p>Yuichi Semura(full-stack engineer)</p>