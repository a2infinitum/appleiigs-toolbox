import json
from collections import defaultdict

# Load the JSON data from a file
with open('toolcalls.json', 'r') as file:
    data = json.load(file)

# Dictionary to store toolname and associated toolcall-description pairs
tool_dict = defaultdict(list)

# Populate the dictionary
for entry in data:
    d= dict()
    
    d['toolname'] = entry['toolname']
    d['toolcall'] = entry['toolcall']
    d['toolnum'] = entry['toolnum']
    d['callname'] = entry['callname']
    d['description'] = entry['description']
    tool_dict[d['toolname']].append(d)


max_toolset_w = max(len(d['toolname']) for d in data)
max_callname_w = max(len(d['callname']) for d in data)
# Print the toolname and associated toolcalls with descriptions
for toolname, toolcalls in tool_dict.items():
    print(f"\n{toolname} ({toolcalls[0]['toolnum']})\n")
    
    for t in toolcalls:
        print(f"{t["toolnum"]} {t["toolcall"]}  {t["toolname"].ljust(max_toolset_w)} {t["callname"].ljust(max_callname_w)}   {t["description"]}")
    print()  # Add a blank line after each toolname section
