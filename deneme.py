def divide_css_classes(css_input):
    lines = css_input.strip().split('\n')
    output = []

    current_class = None
    current_properties = []

    for line in lines:
        line = line.strip()
        if line.startswith('.'):
            if current_class:
                output.append(f".{current_class} {{")
                output.extend(current_properties)
                output.append("  }\n")
            current_class = line.split()[0][1:]
            current_properties = []
        elif line.startswith('  '):
            current_properties.append(line)
        else:
            output.append(line + '\n')

    if current_class:
        output.append(f".{current_class} {{")
        output.extend(current_properties)
        output.append("  }}\n")

    return ''.join(output)

# Test with the provided input
input_css = """.custom-style {
    background-color: lightblue;
    padding: 10px;
    border: 1px solid black;
  }

  button.custom-style {
    background-color: green;
    color: white;
  }

  div.custom-style {
    background-color: yellow;
    font-size: 20px;
  }"""

output_css = divide_css_classes(input_css)
print(output_css)
