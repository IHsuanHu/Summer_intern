# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 16:08:42 2023

@author: Michael Hu
"""
import os
import re
# keep the number and replace with the new format
# def replace_type(match):
#     type_value = match.group(1)
#     if type_value.isdigit():
#         return f", {type_value}, \' \'"
#     return match.group(0)

def replace(file_path):
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()
    
    modified_lines = []
    for line in lines:
        # find all (',', '|', x'\d+', as NCHAR) add -- at front
        if re.match(r".*(\(\'(,|\|)\')|(\(x\'\d+\')\s+AS\s+NCHAR\((\d+)\)*$", line, flags= re.I):
            line = "--" + line
        
        #find first CAST and replace it with sqlext.BIG5RPAD
        # find AS NCHAR(\d) and replace it with , \d, ' '
        else:
            line = re.sub(r"CAST", "sqlext.BIG5RPAD", line, count= 1, flags= re.I)
            line = re.sub(r" AS\s+NCHAR\((\d+)\)", r", \1, ' '", line, flags= re.I)
        modified_lines.append(line)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(''.join(modified_lines))
        

path = input("Enter folder path: ")
path = path.replace('"', '')
# origin = input("Enter the orgin string: ")
# new = input("Enter the new string: ")

os.chdir(path)

for file in os.listdir():
    if file.endswith(".sh"):
        file_path = f'{path}\{file}'
        replace(file_path)
        
        
