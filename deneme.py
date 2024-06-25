css_code = """
.special-class {
  margin: 0.5cm;
  padding: 0.5;
  box-sizing: border-box;
  font-family: 'Arial', sans-serif;
}
.standart-class {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Arial', sans-serif;
}

.standart-class .body {
  background-color: #f5f5f5;
  color: #333;
  font-size: 16px;
  line-height: 1.6;
}

.standart-class .h1 {
  margin: 20px 0;
  color: #222;
  line-height: 1.2;
  font-size: 2.5em;
}

.standart-class .h2 {
  margin: 20px 0;
  color: #222;
  line-height: 1.2;
  font-size: 2em;
}

.standart-class .h3 {
  margin: 20px 0;
  color: #222;
  line-height: 1.2;
  font-size: 1.75em;
}

.standart-class .h4 {
  margin: 20px 0;
  color: #222;
  line-height: 1.2;
  font-size: 1.5em;
}

.standart-class .h5 {
  margin: 20px 0;
  color: #222;
  line-height: 1.2;
  font-size: 1.25em;
}

.standart-class .h6 {
  margin: 20px 0;
  color: #222;
  font-size: 1em;
  line-height: 1.2;
}

.standart-class .p {
  margin-bottom: 15px;
}

.standart-class .a {
  color: #0066cc;
  text-decoration: none;
}

.standart-class .a:hover {
  text-decoration: underline;
}

.standart-class .ul{
  margin: 20px 0;
  padding-left: 20px;
}

.standart-class .ol {
  margin: 20px 0;
  padding-left: 20px;
}

.standart-class .li {
  margin-bottom: 10px;
}

.standart-class .button {
  background-color: #0066cc;
  color: #fff;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 1em;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.standart-class .button:hover {
  background-color: #004999;
}
"""

# Extract the desired CSS rules

# Output the extracted CSS code
print(result.split("{")[1].split("}")[0])
