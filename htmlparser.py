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
    while element:
        siblings = element.find_previous_siblings(element.name)
        position = len(siblings) + 1
        components.append(f"{element.name}[{position}]")
        element = element.parent
    components.reverse()
    return '/' + '/'.join(components)

# Liste için boş bir liste oluştur
result = []

# Tüm elementleri seç ve istenen bilgileri JSON formatında listeye ekle
for element in soup.find_all(True):
    xpath = create_xpath(element)
    
    # Elementin tüm argümanlarını al
    element_attrs = element.attrs
    
    # Elementin içeriğini almak için sadece direkt altındaki metni alıyoruz
    element_text = element.get_text(separator='\n', strip=True)
    
    # Eğer elementin altında başka elementler varsa, içindeki metin yerine boş bırakalım
    if element.find_all(recursive=False):
        element_text = ""
    elif element_text.strip() == "":
        continue
    
    # JSON formatında bir dictionary oluştur
    element_info = {
        "XPath": xpath
    }
    
    # Metin içeriği boş değilse ekleyelim
    if element_text.strip() != "":
        element_info["Text"] = element_text.strip()
    
    # Tüm mevcut argümanları ekleyelim (varsa ve boş değilse)
    for attr, value in element_attrs.items():
        if value:
            element_info[attr.capitalize()] = value if isinstance(value, str) else ' '.join(value)
    
    # Liste içine dictionary'yi ekle
    result.append(element_info)

# Sonuç listesini döndür
print(json.dumps(result, indent=2, ensure_ascii=False))
