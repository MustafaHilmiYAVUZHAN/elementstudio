from bs4 import BeautifulSoup
import json
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
    element_id = element.get('id')
    element_class = ' '.join(element.get('class', []))
    
    # Elementin içeriğini almak için sadece direkt altındaki metni alıyoruz
    element_text = element.get_text(separator='\n', strip=True)
    
    # Eğer elementin altında başka elementler varsa, içindeki metin yerine boş bırakalım
    if element.find_all(recursive=False):
        element_text = ""
    elif element_text.strip() == "":
        continue
    
    # JSON formatında bir dictionary oluştur
    element_info = {
        "XPath": xpath.split("[document][1]")[1]
    }
    
    # Metin içeriği boş değilse ekleyelim
    if element_text.strip() != "":
        element_info["Text"] = element_text.strip()
    
    # ID ve Class bilgilerini ekleyelim (varsa ve boş değilse)
    if element_id:
        element_info["ID"] = element_id
    if element_class:
        element_info["Class"] = element_class
    
    # Liste içine dictionary'yi ekle
    result.append(element_info)
print(json.dumps(result, indent=2, ensure_ascii=False))
