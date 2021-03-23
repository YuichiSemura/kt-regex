import re
from typing import Pattern

pattern = r"/\*[\s\S]*?\*/|//.*(?=(?:\r|\r?\n))"
string = """
max = 7; //line comment
for(int i=0;i<7;i++) System.out.println("sex"+i);
/*  
 * multiline comment
 */
"""

result = re.findall(pattern, string) # 検索
print(result) # ['//line comment', '/*  \n * multiline comment\n */']