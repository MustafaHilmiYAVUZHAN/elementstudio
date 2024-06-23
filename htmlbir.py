import json

json_data = [
  {
    "XPath": "/[document][1]/html[1]",
    "Lang": "tr"
  },
  {
    "XPath": "/[document][1]/html[1]/head[1]"
  },
  {
    "XPath": "/[document][1]/html[1]/head[1]/title[1]",
    "Text": "Örnek Karmaşık Web Sitesi"
  },
  {
    "XPath": "/[document][1]/html[1]/head[1]/style[1]",
    "Text": "/* Genel stil ayarları */\n        body {\n            font-family: 'Arial', sans-serif;\n            line-height: 1.6;\n            background-color: #f4f4f4;\n            margin: 0;\n            padding: 0;\n        }\n        header {\n            background-color: #333;\n            color: #fff;\n            padding: 10px 0;\n            text-align: center;\n        }\n        nav {\n            background-color: #444;\n            padding: 10px 0;\n            text-align: center;\n        }\n        nav a {\n            color: #fff;\n            text-decoration: none;\n            padding: 10px 20px;\n        }\n        nav a:hover {\n            background-color: #555;\n        }\n        .container {\n            width: 80%;\n            margin: auto;\n            overflow: hidden;\n            padding: 20px;\n        }\n        .main {\n            float: left;\n            width: 70%;\n        }\n        .sidebar {\n            float: left;\n            width: 30%;\n            background: #f0f0f0;\n            padding: 10px;\n            margin-top: 20px;\n        }\n        .sidebar ul {\n            list-style-type: none;\n            padding: 0;\n        }\n        .sidebar li {\n            margin-bottom: 10px;\n        }\n        footer {\n            text-align: center;\n            padding: 10px 0;\n            background-color: #333;\n            color: #fff;\n            position: absolute;\n            bottom: 0;\n            width: 100%;\n        }"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/header[1]"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/header[1]/h1[1]",
    "Text": "Örnek Web Sitesi"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/nav[1]"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/nav[1]/a[1]",
    "Text": "Anasayfa",
    "Href": "#"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/nav[1]/a[2]",
    "Text": "Hakkımızda",
    "Href": "#"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/nav[1]/a[3]",
    "Text": "Hizmetler",
    "Href": "#"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/nav[1]/a[4]",
    "Text": "İletişim",
    "Href": "#"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]",
    "Class": "container"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/section[1]",
    "Class": "main"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/section[1]/h2[1]",
    "Text": "Hoş Geldiniz!"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/section[1]/p[1]",
    "Text": "Bu örnek web sitesi, HTML ve CSS kullanılarak oluşturulmuş karmaşık bir tasarıma sahiptir."
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/section[1]/p[2]",
    "Text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam gravida ante ut mauris lobortis, a congue nunc finibus."
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/aside[1]",
    "Class": "sidebar"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/aside[1]/h3[1]",
    "Text": "Sidebar Başlığı"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[1]"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[1]/a[1]",
    "Text": "Örnek Link 1",
    "Href": "#"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[2]"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[2]/a[1]",
    "Text": "Örnek Link 2",
    "Href": "#"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[3]"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[3]/a[1]",
    "Text": "Örnek Link 3",
    "Href": "#"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[4]"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[4]/a[1]",
    "Text": "Örnek Link 4",
    "Href": "#"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/footer[1]"
  },
  {
    "XPath": "/[document][1]/html[1]/body[1]/footer[1]/p[1]",
    "Text": "© 2024 Örnek Web Sitesi. Tüm hakları saklıdır."
  }
]
def create_tag(tag_name, attributes=None, text=""):
    if attributes:
        # Attribute'leri uygun formatta stringe dönüştür
        attr_str = ' '.join(f'{key}="{value}"' for key, value in attributes.items())
        return f"<{tag_name} {attr_str}>{text}"
    else:
        return f"<{tag_name}>{text}"

def close_tag(tag_name):
    return f"</{tag_name}>"

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
                html=html[:-1] + close_tag(open_tags[-1]["tag_name"]) + "\n"
                open_tags.pop()
            
            if len(open_tags) > 0:
                indent_level = open_tags[-1]["indent_level"]
            else:
                indent_level = 0
        
        open_tags.append({"tag_name": tag_name, "XPath": item["XPath"], "indent_level": indent_level-1})
        
        if "Text" in item:
            html += f"{indent * indent_level}{create_tag(tag_name, attributes, item['Text'])}\n"
        else:
            html += f"{indent * indent_level}{create_tag(tag_name, attributes)}\n"

    while len(open_tags) > 0:
        html += close_tag(open_tags[-1]["tag_name"]) + "\n"
        open_tags.pop()
    
    return html
generated_html = convert_to_html(json_data)
print(generated_html)
