import json
from bs4 import BeautifulSoup

# HTML dosyasını oku
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# BeautifulSoup ile HTML içeriğini parse et
soup = BeautifulSoup(html_content, 'html.parser')

# Tüm elementleri seçmek için XPath oluştur
def create_xpath(element):
    components = []
    for parent in element.parents:
        if parent.name:
            index = sum(1 for previous_sibling in parent.find_previous_siblings(parent.name)) + 1
            components.append(f"{parent.name}[{index}]")
    components.reverse()
    return '/'.join(components) + '/' + element.name

# Liste için boş bir liste oluştur
result = []

# Tüm elementleri seç ve istenen bilgileri JSON formatında listeye ekle
for element in soup.find_all(True):
    xpath = create_xpath(element)
    element_id = element.get('id', None)
    element_class = ' '.join(element.get('class', []))
    element_text = element.get_text().strip()
    
    # JSON formatında bir dictionary oluştur
    element_info = {
        "XPath": xpath,
        "Text": element_text
    }
    
    # ID ve Class bilgilerini ekleyelim (varsa)
    if element_id:
        element_info["ID"] = element_id
    if element_class:
        element_info["Class"] = element_class
    
    # Liste içine dictionary'yi ekle
    result.append(element_info)

# JSON formatında çıktıyı yazdır
print(json.dumps(result, indent=2, ensure_ascii=False))
