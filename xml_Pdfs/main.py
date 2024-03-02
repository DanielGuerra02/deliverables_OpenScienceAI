from os import listdir
from os.path import isfile, join
from xml.etree import ElementTree
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def extract_abstracts(xml_directory):
    abstracts = []
    xml_files = [f for f in listdir(xml_directory) if isfile(join(xml_directory, f))]

    for xml_file in xml_files:
        try:
            tree = ElementTree.parse(join(xml_directory, xml_file))
            root = tree.getroot()
            for abstract in root.findall(".//abstract"):
                abstract_text = abstract.text.strip() if abstract.text else ""
                abstracts.append(abstract_text)
        except ElementTree.ParseError as e:
            print(f"Error parsing {xml_file}: {e}")
            continue
    
    return abstracts


def generate_wordcloud(abstracts):
    text = " ".join(abstracts)
    
    
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    xml_directory = "/home/daniwar/deliverables_OpenScienceAI/xml_Pdfs"  # Directorio donde se encuentran los archivos XML

    abstracts = extract_abstracts(xml_directory)
    generate_wordcloud(abstracts)
