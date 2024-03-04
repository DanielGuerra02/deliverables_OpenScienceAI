import os
from xml.etree import ElementTree as ET
from wordcloud import WordCloud
import matplotlib.pyplot as plt


namespace_map = {'': 'http://www.tei-c.org/ns/1.0'}

# Función para obtener el resumen del artículo
def get_abstract(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    abstract_elements = root.findall('.//{http://www.tei-c.org/ns/1.0}abstract/{http://www.tei-c.org/ns/1.0}div/{http://www.tei-c.org/ns/1.0}p', namespaces=namespace_map)
    abstract_text = " ".join([element.text.strip() for element in abstract_elements if element.text])
    return abstract_text

# Función para crear la nube de palabras
def create_wordcloud(directory_path):
    xml_files = [file for file in os.listdir(directory_path) if file.endswith(".xml")]
    abstracts = {}
    
    for xml_file in xml_files:
        xml_path = os.path.join(directory_path, xml_file)
        abstract = get_abstract(xml_path)
        abstracts[xml_file] = abstract
    
    all_text = " ".join(abstracts.values())
    wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate(all_text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('./results/wordcloud.png')
    plt.close()

# Función para contar las figuras en cada artículo
def count_figures(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    figure_elements = root.findall('.//{http://www.tei-c.org/ns/1.0}figure', namespaces=namespace_map)
    return len(figure_elements)

# Función para crear la visualización del número de figuras por artículo
def create_figures_visualization(xml_directory):
    xml_files = [file for file in os.listdir(xml_directory) if file.endswith(".xml")]
    figures_per_article = {file: count_figures(os.path.join(xml_directory, file)) for file in xml_files}
    
    plt.bar(range(len(figures_per_article)), list(figures_per_article.values()), align='center')
    plt.xticks(range(len(figures_per_article)), list(figures_per_article.keys()), rotation=90)
    plt.xlabel('Artículos')
    plt.ylabel('Número de figuras')
    plt.title('Número de figuras por artículo')
    plt.tight_layout()
    plt.savefig('./results/figures_per_article.png')
    plt.close()

# Función para extraer enlaces internos de cada artículo
def extract_links(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    biblStruct_elements = root.findall('.//{http://www.tei-c.org/ns/1.0}biblStruct', namespaces=namespace_map)
    links = []
    for biblStruct in biblStruct_elements:
        ptr = biblStruct.find('.//{http://www.tei-c.org/ns/1.0}ptr', namespaces=namespace_map)
        if ptr is not None:
            links.append(ptr.get('target'))
    return links

# Función principal para ejecutar las funcionalidades
def run_main():
    xml_data_directory = './xml_Pdfs'
    results_directory = './results'
    os.makedirs(results_directory, exist_ok=True)  

    create_wordcloud(xml_data_directory)
    
    create_figures_visualization(xml_data_directory)
    
    links_per_article = {}
    for xml_file in sorted(os.listdir(xml_data_directory)):
        if xml_file.endswith(".xml"):
            file_path = os.path.join(xml_data_directory, xml_file)
            links = extract_links(file_path)
            links_per_article[xml_file] = links
    
    with open(os.path.join(results_directory, 'links_per_article.txt'), 'w') as file:
        for article, links in links_per_article.items():
            file.write(f'{article}: {links}\n')

if __name__ == "__main__":
    run_main()