import re

def get_all_class_names(code):
    """Returns a list of all the class names in the given code."""
    class_names = []

    # Use a regular expression to find all the class definitions in the code.
    class_definitions = re.findall(r'def\s+(\w+)', code)

    # Add each class name to the list of class names.
    for class_definition in class_definitions:
        class_names.append(class_definition)

    return class_names

# Example usage:

code = '''
class DesignationMaster:
  pass

class Meta:
  pass

class StateMaster:
  pass

'''

class_names = get_all_class_names(code)

filtered_list = [item for item in class_names if item != 'Meta']
# Convert the list to a string, joining elements with a space
result_string = ', '.join(filtered_list)

print(result_string)

