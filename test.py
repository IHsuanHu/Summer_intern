import os
import re
# keep the number and replace with the new format
def replace_type(match):
    type_value = match.group(1)
    if type_value.isdigit():
        return f", {type_value}, \' \'"
    return match.group(0)


def replace(file_path):
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()
    
    modified_lines = []
    for line in lines:
        # if re.search(r"\s+AS\s+NVARCHAR\(\d+\)", line, flags= re.I) and (r"sqlext.BIG5RPAD", line):
        line = re.sub(r"(substr\()cast", r"\1sqlext.BIG5RPAD", line, flags= re.I)
        modified_lines.append(line)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(''.join(modified_lines))
        

path = input("Enter folder path: ")
# origin = input("Enter the orgin string: ")
# new = input("Enter the new string: ")

os.chdir(path)

for file in os.listdir():
    if file.endswith(".sh"):
        file_path = f'{path}\{file}'
        replace(file_path)