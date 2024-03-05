[![DOI](https://zenodo.org/badge/759483919.svg)](https://zenodo.org/doi/10.5281/zenodo.10779299)

# Scientific Article Analysis with Grobid and Data Visualization

This project utilizes text analysis tools to process open-access scientific articles and generate useful visualizations from the extracted data. The main program, main.py, is responsible for drawing a keyword cloud based on abstract information and creating visualizations showing the number of figures per article. Additionally, a list of links found in each article is generated.

## Project Structure

-`main.py`: Main script responsible for executing the analysis and visualization generation.
-`extract.py`: Script that utilizes the Grobid client to convert PDF documents to XML.
-`test.py`: Contains tests to ensure that the code functions as expected.
-`Dockerfile`: Contains all instructions to build the Docker image of the project.

## Getting Started

Before running the project, it's necessary to install Grobid client, which is used to convert PDF documents to XML. Execute the following commands to clone the Grobid client repository and perform the installation: 

git clone https://github.com/kermitt2/grobid_client_python
cd grobid_client_python
python3 setup.py install

## Project Execution

### In Your Local Environment

To execute `main.py` in your local environment, ensure you have all necessary dependencies installed, as described in `requirements.txt`.

### Using Docker

For those who prefer to use Docker, detailed instructions are provided for building and running the container.

#### Build Docker Image

Run the following command to build the Docker image:

docker build -t your_image_name .

#### Run Docker Containerr

To start the container and execute the project:

docker run -it --name your_container_name your_image_name

If you wish to view the results directly within the container, open a new terminal and execute:

docker exec -it your_container_name /bin/bash

Navigate to the results folder to view the generated files.

#### Copy Results to Local Environment

If you prefer to copy the results to the local environment, use:

docker cp your_container_name:/app/results ./results






