# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 16:08:42 2023

@author: Michael Hu
"""
import os
import re

def replace_type(match):
    type_value = match.group(1)
    if type_value.isdigit():
        return f", {type_value}, \" \""
    return match.group(0)

def replace(file_path):
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()
    
    modified_lines = []
    for line in lines:
        if re.match(r".*\(\'(,|\|)\'\s+AS\s+NCHAR\((\d+)\)*$", line, flags= re.I):
            line = "--" + line
        else:
            line = re.sub(r"CAST", "sqlext.BIG5RPAD", line, count= 1, flags= re.I)
            line = re.sub(r" AS\s+NCHAR\((\d+)\)", replace_type, line, count = 1, flags= re.I)
        modified_lines.append(line)
        
    # s = s.replace(origin, new)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(''.join(modified_lines))
        

path = input("Enter folder path: ")
# origin = input("Enter the orgin string: ")
# new = input("Enter the new string: ")
# path = "C:\\Users\\user\\Desktop\\test" 
os.chdir(path)

for file in os.listdir():
    if file.endswith(".sh"):
        file_path = f'{path}\{file}'
        replace(file_path)
        
        
