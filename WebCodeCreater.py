import json
from bs4 import BeautifulSoup
import re
class CSS:
    @staticmethod
    def list_css_classes(file_path):
        # CSS dosyasını oku
        with open(file_path, 'r') as file:
            css_content = file.read()
        
        # CSS sınıflarını (class) bulmak için regex kullan
        classes = re.findall(r'\.([a-zA-Z0-9_-]+)\s*{', css_content)
        
        # Benzersiz sınıfları listele
        unique_classes = list(set(classes))
        
        # Sınıfları döndür
        return unique_classes

    @staticmethod
    def convert_to_id_css(element_type, element_id, avfp, x, y, width, height, element_class,extra_css):
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

    file_path = 'example.html'
    parsed_data = HTML.convert_to_json(file_path, readinfolder=True)

    # JSON verisini HTML'e dönüştürmek için
    generated_html = HTML.convert_to_html(parsed_data)
    print(generated_html)
