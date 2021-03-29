import re

pattern = r"(?<=AssemblyFinalVersion=\")\d\.\d\.\d\.\d"
repl = "2.2.2.2"
string = """\
AssemblyVersion="1.0.0.0"
AssemblyFinalVersion="1.0.0.0"
FixVersion="1.0.0.0"\
"""

result = re.sub(pattern, repl, string) # 置換
print(result)