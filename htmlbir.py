import json

# JSON verisi (örneğin tamamı burada yer alacaktır)
json_data =[
  {
    "XPath": "[document][1]/html",
    "Text": "Örnek Karmaşık Web Sitesi\nÖrnek Web Sitesi\nAnasayfa\nHakkımızda\nHizmetler\nİletişim\nHoş Geldiniz!\nBu örnek web sitesi, HTML ve CSS kullanılarak oluşturulmuş karmaşık bir tasarıma sahiptir.\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam gravida ante ut mauris lobortis, a congue nunc finibus.\nSidebar Başlığı\nÖrnek Link 1\nÖrnek Link 2\nÖrnek Link 3\nÖrnek Link 4\n© 2024 Örnek Web Sitesi. Tüm hakları saklıdır."
  },
  {
    "XPath": "[document][1]/html[1]/head",
    "Text": "Örnek Karmaşık Web Sitesi"
  },
  {
    "XPath": "[document][1]/html[1]/head[1]/meta",
    "Text": ""
  },
  {
    "XPath": "[document][1]/html[1]/head[1]/meta",
    "Text": ""
  },
  {
    "XPath": "[document][1]/html[1]/head[1]/title",
    "Text": "Örnek Karmaşık Web Sitesi"
  },
  {
    "XPath": "[document][1]/html[1]/head[1]/style",
    "Text": "/* Genel stil ayarları */\n        body {\n            font-family: 'Arial', sans-serif;\n            line-height: 1.6;\n            background-color: #f4f4f4;\n            margin: 0;\n            padding: 0;\n        }\n        header {\n            background-color: #333;\n            color: #fff;\n            padding: 10px 0;\n            text-align: center;\n        }\n        nav {\n            background-color: #444;\n            padding: 10px 0;\n            text-align: center;\n        }\n        nav a {\n            color: #fff;\n            text-decoration: none;\n            padding: 10px 20px;\n        }\n        nav a:hover {\n            background-color: #555;\n        }\n        .container {\n            width: 80%;\n            margin: auto;\n            overflow: hidden;\n            padding: 20px;\n        }\n        .main {\n            float: left;\n            width: 70%;\n        }\n        .sidebar {\n            float: left;\n            width: 30%;\n            background: #f0f0f0;\n            padding: 10px;\n            margin-top: 20px;\n        }\n        .sidebar ul {\n            list-style-type: none;\n            padding: 0;\n        }\n        .sidebar li {\n            margin-bottom: 10px;\n        }\n        footer {\n            text-align: center;\n            padding: 10px 0;\n            background-color: #333;\n            color: #fff;\n            position: absolute;\n            bottom: 0;\n            width: 100%;\n        }"
  },
  {
    "XPath": "[document][1]/html[1]/body",
    "Text": "Örnek Web Sitesi\nAnasayfa\nHakkımızda\nHizmetler\nİletişim\nHoş Geldiniz!\nBu örnek web sitesi, HTML ve CSS kullanılarak oluşturulmuş karmaşık bir tasarıma sahiptir.\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam gravida ante ut mauris lobortis, a congue nunc finibus.\nSidebar Başlığı\nÖrnek Link 1\nÖrnek Link 2\nÖrnek Link 3\nÖrnek Link 4\n© 2024 Örnek Web Sitesi. Tüm hakları saklıdır."
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/header",
    "Text": "Örnek Web Sitesi"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/header[1]/h1",
    "Text": "Örnek Web Sitesi"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/nav",
    "Text": "Anasayfa\nHakkımızda\nHizmetler\nİletişim"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/nav[1]/a",
    "Text": "Anasayfa"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/nav[1]/a",
    "Text": "Hakkımızda"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/nav[1]/a",
    "Text": "Hizmetler"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/nav[1]/a",
    "Text": "İletişim"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div",
    "Text": "Hoş Geldiniz!\nBu örnek web sitesi, HTML ve CSS kullanılarak oluşturulmuş karmaşık bir tasarıma sahiptir.\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam gravida ante ut mauris lobortis, a congue nunc finibus.\nSidebar Başlığı\nÖrnek Link 1\nÖrnek Link 2\nÖrnek Link 3\nÖrnek Link 4",
    "Class": "container"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/section",
    "Text": "Hoş Geldiniz!\nBu örnek web sitesi, HTML ve CSS kullanılarak oluşturulmuş karmaşık bir tasarıma sahiptir.\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam gravida ante ut mauris lobortis, a congue nunc finibus.",
    "Class": "main"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/section[1]/h2",
    "Text": "Hoş Geldiniz!"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/section[1]/p",
    "Text": "Bu örnek web sitesi, HTML ve CSS kullanılarak oluşturulmuş karmaşık bir tasarıma sahiptir."
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/section[1]/p",
    "Text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam gravida ante ut mauris lobortis, a congue nunc finibus."
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/aside",
    "Text": "Sidebar Başlığı\nÖrnek Link 1\nÖrnek Link 2\nÖrnek Link 3\nÖrnek Link 4",
    "Class": "sidebar"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/aside[1]/h3",
    "Text": "Sidebar Başlığı"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/aside[1]/ul",
    "Text": "Örnek Link 1\nÖrnek Link 2\nÖrnek Link 3\nÖrnek Link 4"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li",
    "Text": "Örnek Link 1"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[1]/a",
    "Text": "Örnek Link 1"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li",
    "Text": "Örnek Link 2"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[2]/a",
    "Text": "Örnek Link 2"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li",
    "Text": "Örnek Link 3"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[3]/a",
    "Text": "Örnek Link 3"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li",
    "Text": "Örnek Link 4"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/div[1]/aside[1]/ul[1]/li[4]/a",
    "Text": "Örnek Link 4"
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/footer",
    "Text": "© 2024 Örnek Web Sitesi. Tüm hakları saklıdır."
  },
  {
    "XPath": "[document][1]/html[1]/body[1]/footer[1]/p",
    "Text": "© 2024 Örnek Web Sitesi. Tüm hakları saklıdır."
  }
]

def json_to_html(json_data):
    html_content = ""
    for item in json_data:
        if "Text" in item:
            html_content += f"<{item['XPath']}>{item['Text']}</{item['XPath'].split('/')[-1]}>"
        else:
            html_content += f"<{item['XPath']}/>"
        html_content += "\n"
    return html_content

# HTML kodunu oluştur
generated_html = json_to_html(json_data)

# Oluşturulan HTML'yi ekrana yazdır
print(generated_html)
