import json

json_data = [
  {
    "XPath": "/html"
  },
  {
    "XPath": "/html[1]/head"
  },
  {
    "XPath": "/html[1]/head[1]/title",
    "Text": "Örnek Karmaşık Web Sitesi"
  },
  {
    "XPath": "/html[1]/head[1]/style",
    "Text": "/* Genel stil ayarları */\n        body {\n            font-family: 'Arial', sans-serif;\n            line-height: 1.6;\n            background-color: #f4f4f4;\n            margin: 0;\n            padding: 0;\n        }\n        header {\n            background-color: #333;\n            color: #fff;\n            padding: 10px 0;\n            text-align: center;\n        }\n        nav {\n            background-color: #444;\n            padding: 10px 0;\n            text-align: center;\n        }\n        nav a {\n            color: #fff;\n            text-decoration: none;\n            padding: 10px 20px;\n        }\n        nav a:hover {\n            background-color: #555;\n        }\n        .container {\n            width: 80%;\n            margin: auto;\n            overflow: hidden;\n            padding: 20px;\n        }\n        .main {\n            float: left;\n            width: 70%;\n        }\n        .sidebar {\n            float: left;\n            width: 30%;\n            background: #f0f0f0;\n            padding: 10px;\n            margin-top: 20px;\n        }\n        .sidebar ul {\n            list-style-type: none;\n            padding: 0;\n        }\n        .sidebar li {\n            margin-bottom: 10px;\n        }\n        footer {\n            text-align: center;\n            padding: 10px 0;\n            background-color: #333;\n            color: #fff;\n            position: absolute;\n            bottom: 0;\n            width: 100%;\n        }"
  },
  {
    "XPath": "/html[1]/body"
  },
  {
    "XPath": "/html[1]/body[1]/header"
  },
  {
    "XPath": "/html[1]/body[1]/header[1]/h1",
    "Text": "Örnek Web Sitesi"
  },
  {
    "XPath": "/html[1]/body[1]/nav"
  },
  {
    "XPath": "/html[1]/body[1]/nav[1]/a",
    "Text": "Anasayfa"
  },
  {
    "XPath": "/html[1]/body[1]/nav[1]/a",
    "Text": "Hakkımızda"
  },
  {
    "XPath": "/html[1]/body[1]/nav[1]/a",
    "Text": "Hizmetler"
  },
  {
    "XPath": "/html[1]/body[1]/nav[1]/a",
    "Text": "İletişim"
  },
  {
    "XPath": "/html[1]/body[1]/div",
    "Class": "container"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/section",
    "Class": "main"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/section[1]/h2",
    "Text": "Hoş Geldiniz!"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/section[1]/p",
    "Text": "Bu örnek web sitesi, HTML ve CSS kullanılarak oluşturulmuş karmaşık bir tasarıma sahiptir."
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/section[1]/p",
    "Text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam gravida ante ut mauris lobortis, a congue nunc finibus."
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/aside",
    "Class": "sidebar"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/aside[1]/h3",
    "Text": "Sidebar Başlığı"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/aside[1]/ul"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/aside[1]/ul[1]/li"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[1]/a",
    "Text": "Örnek Link 1"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/aside[1]/ul[1]/li"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[2]/a",
    "Text": "Örnek Link 2"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/aside[1]/ul[1]/li"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[3]/a",
    "Text": "Örnek Link 3"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/aside[1]/ul[1]/li"
  },
  {
    "XPath": "/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[4]/a",
    "Text": "Örnek Link 4"
  },
  {
    "XPath": "/html[1]/body[1]/footer"
  },
  {
    "XPath": "/html[1]/body[1]/footer[1]/p",
    "Text": "© 2024 Örnek Web Sitesi. Tüm hakları saklıdır."
  }
]
def create_tag(tag_name, attributes="", text=""):
    if attributes:
        return f"<{tag_name} class=\"{attributes}\">{text}"
    else:
        return f"<{tag_name}>{text}"

def close_tag(tag_name):
    return f"</{tag_name}>"

def convert_to_html(json_data):
    html = ""
    open_tags = []

    for item in json_data:
        tag_name = item["XPath"].split("/")[-1].split("[")[0]
        attributes = item.get("Class", "")

        if tag_name == "html" or tag_name == "head" or tag_name == "body":
            indent_level = item["XPath"].count("/") - 2
            indent = "    " * indent_level
        else:
            while len(open_tags) > 0 and not item["XPath"].startswith(open_tags[-1]["XPath"]):
                html += close_tag(open_tags[-1]["tag_name"]) + "\n"
                open_tags.pop()

            if len(open_tags) > 0:
                indent = "    " * (open_tags[-1]["indent_level"] + 1)
            else:
                indent = ""

        open_tags.append({"tag_name": tag_name, "XPath": item["XPath"], "indent_level": indent_level})

        if "Text" in item:
            html += f"{indent}{create_tag(tag_name, attributes, item['Text'])}\n"
        else:
            html += f"{indent}{create_tag(tag_name, attributes)}\n"

    while len(open_tags) > 0:
        html += close_tag(open_tags[-1]["tag_name"]) + "\n"
        open_tags.pop()

    return html

generated_html = convert_to_html(json_data)
print(generated_html)
