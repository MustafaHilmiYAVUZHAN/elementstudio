import json
from bs4 import BeautifulSoup
import re
class CSS:
    @staticmethod
    def select_sub_class(css,start_selector,readinfile=True):
        soup = BeautifulSoup(css_code, 'html.parser')

        # Extract the desired CSS rules
        start_selector = ".standart-class .button:hover"
        in_block = False
        result = ""

        for line in css_code.split("\n"):
            if line.strip().startswith(start_selector):
                in_block = True
            if in_block:
                result += line + "\n"
                if "}" in line:
                    in_block = False

        # Output the extracted CSS code
        return result.strip()
    @staticmethod
    def css_to_json(css,readinfile=True):
        if readinfile:
            css=CSS.read_css_file(css)
        lines = css.strip().splitlines()
        json_output = {}
        current_selector = None
        current_properties = {}

        for line in lines:
            line = line.strip()
            
            if not line:
                continue
            
            if line.startswith('.') or line.startswith('#')  :
                current_selector = line.split('{')[0].strip()
                current_properties = {}
            elif line.startswith('}'):
                if current_selector:
                    json_output[current_selector] = current_properties
                    current_selector = None
                    current_properties = {}
            else:
                try:
                    prop, value = line.split(':')
                except:
                    print(line.split(':'))
                prop = prop.strip()
                value = value.strip().rstrip(';')
                current_properties[prop] = value
        
        return json_output

    @staticmethod
    def listtodict(lst):
        if len(lst) % 2 != 0:
            print(lst)
            raise ValueError("Liste çift sayıda eleman içermelidir.")

        return {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    @staticmethod
    def stringtodict(class_css=None):
        if class_css:

            print(class_css)
            class_css=class_css.replace(";",":")
            class_css=class_css.replace("\n","")            
            

            print(CSS.listtodict( class_css.split(":")[:-1]))
            
            class_dict= CSS.listtodict( [eleman.strip() for eleman in class_css.split(":")[:-1]])
            print(str(class_dict))
        else:
            class_dict={}
        return class_dict
    @staticmethod
    def extract_all_id_styles(css,readinfile=True):
        if readinfile:
            css=CSS.read_css_file(css)
        id_styles = {}
        pattern = re.compile(r'#([\w-]+)\s*{([^}]*)}', re.MULTILINE)
        matches = pattern.findall(css)
        for match in matches:
            id_name = match[0]
            styles = match[1].strip()
            id_styles[id_name] = styles
        return id_styles
    @staticmethod
    def list_css_classes(css,readinfile=True):
        if readinfile:
            css=CSS.read_css_file(css)
        main_classes = []
        lines = css.splitlines()
        for line in lines:
            if line.strip().endswith('{'):
                class_name = line.split('{')[0].strip()
                main_classes.append(class_name)
        return main_classes
    @staticmethod
    def list_main(item):
        return list(set([item.split()[0] for item in item]))
    @staticmethod
    def group_by_first_word(items):
        # Dictionary to hold groups
        from collections import defaultdict
        groups = defaultdict(list)
        
        # Her bir öğe için
        for item in items:
            # İlk kelimeyi bul
            first_word = item.split()[0]
            # Geri kalan kısmı al (ilk kelimeyi atla)
            rest_of_words = ' '.join(item.split()[1:])
            # Grupları oluştur
            groups[first_word].append(rest_of_words)
        
        return dict(groups)
    @staticmethod
    def get_class(file_path, class_name):
        # CSS dosyasını oku
        with open(file_path, 'r') as file:
            css_content = file.read()
        
        # Verilen class_name'e ait CSS stilini bulmak için regex kullan
        pattern = r'\.' + re.escape(class_name) + r'\s*{(.*?)}'
        match = re.search(pattern, css_content, re.DOTALL)
        
        if match:
            # Eşleşen CSS stilini string olarak döndür
            return match.group(1).strip()
        else:
            # Eğer belirtilen sınıf bulunamazsa None döndür
            return None
    @staticmethod
    def no_pseudo_class(liste):
        return [eleman for eleman in liste if ':' not in eleman]
    @staticmethod
    def find_pseude_class(liste,key):
        return [item.split(key)[1] for item in liste if item.startswith(key)]
    @staticmethod
    def convert_to_id_css(element_type, element_id, avfp, x, y, witableh, height, element_class,extra_css):
        avfp = str(avfp)
        position=avfp
        css_template = f"""#{element_id} {{
        position: {'absolute' if position == '0' else 'fixed' if position == '1' else 'static' if position == '2' else 'relative'};
        left: {x}px;
        top: {y}px;
        width: {width}px;
        height: {height}px;
        {extra_css}
        }}
        """

        return css_template
    @staticmethod
    def read_css_file(filename):
        css_data = ""
        try:
            with open(filename, 'r') as file:
                css_data = file.read()
            return css_data
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            return None
    @staticmethod
    def dict_to_css(style_dict,class_=None):
        if class_:
            pass
        else:
            css = ""
        for key, value in style_dict.items():
            if isinstance(value, dict):
                # Eğer değer bir sözlükse (örneğin 'flex' özelliği gibi)
                css += f"{key}: "
                for sub_key, sub_value in value.items():
                    css += f"{sub_value} "
                css = css.rstrip() + ";\n"
            else:
                css += f"{key}: {value};\n"
        print(css.rstrip())
        return css.rstrip()
    @staticmethod
    def filter_class(liste):
        return [item for item in liste if item.startswith(".") ]
class HTML: 

    @staticmethod
    def convert_to_json(data, readinfolder=False):
        if readinfolder:
            with open(data, 'r', encoding='utf-8') as file:
                html_content = file.read()
        else:
            html_content = data
        
        soup = BeautifulSoup(html_content, 'html.parser')
        result = []

        def create_xpath(element):
            components = []
            while element:
                siblings = element.find_previous_siblings(element.name)
                position = len(siblings) + 1
                components.append(f"{element.name}[{position}]")
                element = element.parent
            components.reverse()
            return '/' + '/'.join(components)

        for element in soup.find_all(True):
            xpath = create_xpath(element)
            element_attrs = element.attrs
            element_text = element.get_text(separator='\n', strip=True)

            if element.find_all(recursive=False):
                element_text = ""
            elif element_text.strip() == "":
                continue

            element_info = {
                "XPath": xpath
            }

            if element_text.strip() != "":
                element_info["Text"] = element_text.strip()

            for attr, value in element_attrs.items():
                if value:
                    element_info[attr.capitalize()] = value if isinstance(value, str) else ' '.join(value)

            result.append(element_info)

        return result
    @staticmethod
    def create_tag(tag_name, attributes=None, text=""):
        if attributes:
            # Attribute'leri uygun formatta stringe dönüştür
            attr_str = ' '.join(f'{key}="{value}"' for key, value in attributes.items())
            return f"<{tag_name} {attr_str}>{text}"
        else:
            return f"<{tag_name}>{text}"
    

    @staticmethod
    def convert_to_html(json_data):
        html = ""
        open_tags = []
        indent = "    "  # Girinti için kullanılacak boşluk sayısı

        for item in json_data:
            tag_name = item["XPath"].split("/")[-1].split("[")[0]
            attributes = dict(list(item.items())[1:])
            if "Text" in attributes.keys():
                attributes = dict(list(attributes.items())[1:])
            # HTML, head veya body etiketleri için girinti seviyesi 0
            if tag_name =="html":
                indent_level = 0
            elif tag_name in ["body","head"]:
                indent_level = 0
            if 1:
                # Diğer etiketler için girinti seviyesi hesaplanıyor
                while len(open_tags) > 0 and not item["XPath"].startswith(open_tags[-1]["XPath"]):
                    html=html[:-1] + HTML.close_tag(open_tags[-1]["tag_name"]) + "\n"
                    open_tags.pop()
                
                if len(open_tags) > 0:
                    indent_level = open_tags[-1]["indent_level"]
                else:
                    indent_level = 0
            
            open_tags.append({"tag_name": tag_name, "XPath": item["XPath"], "indent_level": indent_level-1})
            
            if "Text" in item:
                html += f"{indent * indent_level}{HTML.create_tag(tag_name, attributes, item['Text'])}\n"
            else:
                html += f"{indent * indent_level}{HTML.create_tag(tag_name, attributes)}\n"

        while len(open_tags) > 0:
            html += HTML.close_tag(open_tags[-1]["tag_name"]) + "\n"
            open_tags.pop()
        soup = BeautifulSoup(html, 'html.parser')
        html = soup.prettify()
        return html

    @staticmethod
    def close_tag(tag_name):
        return f"</{tag_name}>"

# Kullanım örneği:
# HTML'i parse etmek için
if __name__ == "__main__":

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

    # CSS'i JSON formatına dönüştür
    json_output = CSS.css_to_json("styles.css")

    # JSON çıktısını yazdır
    import json
    print(json.dumps(json_output, indent=2))
    print(json_output[list(json_output.keys())[0]])
    print(CSS.list_main(CSS.list_css_classes("styles.css")))
    print("mmmmmmmmmmmmmm")
    print(CSS.list_css_classes("styles.css"))

    print(CSS.group_by_first_word(CSS.list_css_classes("styles.css")))
    print(CSS.extract_all_id_styles("styles.css"))
    
"""    print(CSS.find_main_classes(css_code))"""
