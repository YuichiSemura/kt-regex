import re

pattern = r's\S*'
string = 'smr tki yki smr ski' # 検索対象文字列

# 全て検索し、文字列リストを返す
result = re.findall(pattern, string)

print(result) # ['smr', 'smr', 'ski']