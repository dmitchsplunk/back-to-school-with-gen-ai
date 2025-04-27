# Load Text Book

This sub-component of the application parses a textbook 
in PDF format and loads it into the vector database. 

It reads the text in the document, but does not extract 
text from images.

## Run the Application

Let's start by creating a virtual environment: 

``` bash
cd load-textbook

# create a virtual environment
python -m venv venv

# activate the virtual environment
source venv/bin/activate
```

Then we'll install the [pypdf](https://pypdf.readthedocs.io/en/stable/) Python library, 
which we'll use to load and parse the PDF document: 

``` bash
pip install pypdf==5.4.0
pip install langchain_community==0.3.22
pip install langchain_openai==0.3.14
pip install langchain-chroma==0.2.3
```

Ensure your OPENAI_API_KEY token is set as an environment variable before running
the application.  For example, if the token is not set as part of your profile, 
use the following command to set it: 

``` bash
export OPENAI_API_KEY=<your OpenAI API key value> 
```

To run the application, use the following command:

* Be sure to include the path to a PDF document you'd like to load 

``` bash 
python app.py <path to PDF document> 
```

