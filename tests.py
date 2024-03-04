import unittest
import os
from main import *

class TestXMLProcessing(unittest.TestCase):
    def setUp(self):
        self.test_data_directory = './xml_Pdfs'
        self.test_results_directory = './results'
        os.makedirs(self.test_results_directory, exist_ok=True)

    def test_create_wordcloud(self):
        create_wordcloud(self.test_data_directory)
        self.assertTrue(os.path.isfile(os.path.join(self.test_results_directory, 'wordcloud.png')))

    def test_create_figures_visualization(self):
        create_figures_visualization(self.test_data_directory)
        self.assertTrue(os.path.isfile(os.path.join(self.test_results_directory, 'figures_per_article.png')))

    def test_extract_links(self):
        xml_file = 'Articulo1.grobid.tei.xml'  
        links = extract_links(os.path.join(self.test_data_directory, xml_file))
        with open(os.path.join(self.test_results_directory, 'links_per_article.txt'), 'w') as file:
            file.write(f'{xml_file}: {links}\n')
        self.assertTrue(os.path.isfile(os.path.join(self.test_results_directory, 'links_per_article.txt')))
        
    def test_files_in_results_directory(self):
        files_in_results = os.listdir(self.test_results_directory)

        figure_files = [file for file in files_in_results if file.endswith('.png')]
        text_files = [file for file in files_in_results if file.endswith('.txt')]
        self.assertEqual(len(figure_files), 2)
        self.assertEqual(len(text_files), 1)



if __name__ == '__main__':
    unittest.main()
