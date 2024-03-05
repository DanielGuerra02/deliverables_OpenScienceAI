from grobid_client.grobid_client import GrobidClient

def procesar_archivos_pdf(input_directory, output_directory, concurrency=10):
    client = GrobidClient(config_path="./deliverables_OpenScienceAI/grobid_client_python/config.json")
    client.process("processFulltextDocument", input_directory, output=output_directory, n=concurrency)

if __name__ == "__main__":
    input_directory = "./deliverables_OpenScienceAI/Pdfs"
    output_directory = "./deliverables_OpenScienceAI/xml_Pdfs"

    concurrency = 10

    procesar_archivos_pdf(input_directory, output_directory, concurrency)
