import json
import yaml
# Load the JSON data from a file
with open('toolcalls.json', 'r') as file:
    data = json.load(file)

# Convert Python object to YAML string
yaml_string = yaml.dump(data, default_flow_style=False)
print(yaml_string)

print()  # Add a blank line after each toolname section
