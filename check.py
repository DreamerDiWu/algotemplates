import json
import os, sys
import random  

def pretty_print_code(code_str):
    pretty = []
    for i, line in enumerate(code_str.split("\n")):
        pretty.append(f"{i:>2}: {line}")
    print("\n".join(pretty))

with open('./templates.py', 'r') as fr:
    content = fr.readlines()
content_str = "".join(content)
data = eval(content_str)
with open(sys.argv[1], 'r') as fr:
    keys = eval(fr.readline())
    lines = fr.readlines()
key_to_code = {}
while "\n" in lines:
    idx = lines.index("\n")
    text = lines[:idx]
    lines = lines[idx+1:]
    if "".join(text).strip() == "":
        continue 
    key = "".join(text[0]).strip()
    input = "".join(text[1]).strip()
    output = "".join(text[2]).strip()
    code = "".join(text[3:]).strip()
    key_to_code[key] = code 
# print(key_to_code)
# print(data)
for key, code in key_to_code.items():
    
    practice_code = code.strip()
    template_code = data[key]["code"].strip()
    has_diff = False
    for i, (l1, l2) in enumerate(zip(template_code.split('\n'), practice_code.split('\n'))):
        if l1.strip() != l2.strip():
            has_diff = True
            print('+-'*10, f"[{key}] diff at line {i}", '+-'*10)
            print("template:", repr(l1))
            print("practive:", repr(l2))
    if has_diff:
        print('+-' * 10, f"template [{key}]", "+-" * 10)
        pretty_print_code(template_code)
        print('+-' * 10, f"practice [{key}]", "+-" * 10)
        pretty_print_code(practice_code)
    else:
        print(f"Congradulations! [{key}] has no diff!")
