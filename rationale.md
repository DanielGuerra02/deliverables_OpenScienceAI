# Rationale

This document provides a detailed explanation of how the requirements for analyzing 10 open-access articles using Grobid and other text analysis tools have been validated.

## Requirements Validation

### Keyword Cloud

**Requirement:** Draw a keyword cloud based on the words found in the abstracts of the articles
**Validation:**
To validate the keyword cloud, the following steps were taken:

Abstracts of the articles were extracted using Grobid, which converts PDF documents to XML, facilitating text extraction.
A Python library called wordcloud was used to generate the keyword cloud.
Manual verification was performed to ensure that the most frequent words in the abstracts were prominently represented in the keyword cloud.
The keyword cloud was compared with the keywords provided by the authors of the articles to ensure accuracy.

### Visualization of Number of Figures per Article


**Requirement:** Create a visualization showing the number of figures per article.

**Validation:**
To validate the visualization of the number of figures, the following steps were taken:

The extracted XML was used to count the <figure> tags present in each article.
A bar chart was created using matplotlib to visualize the number of figures.
The original articles were reviewed to confirm that the figure count matched the figures present in the documents.

### List of Links per Article

**Requirement:** Create a list of links found in each article.

**Validation:**
The list of links was validated by:

Extracting all links using XPath during XML processing.
Creating a list associating each link with its corresponding article.
Manually verifying a sample of links to confirm that they point to resources cited in the articles.