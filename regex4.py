import re

pattern = r'tk'
repl = 'Teku'
string = 'tktktktk' # 検索対象文字列

# 検索し、置換する。
result = re.sub(pattern, repl, string)

print(result) # TekuTekuTekuTeku
print(string.replace(pattern, repl))