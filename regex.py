import re

pattern = r'tki' # 正規表現を書くときは、raw 文字列を使うと良き。
string = 'smr tki yki smr ski' # 検索対象文字列

# 一つ検索し、マッチオブジェクトを返す。
result = re.search(pattern, string)

if result: # none 以外の場合
    print(result.span())  # output:(4, 7)
    print(result.group()) # output:tki