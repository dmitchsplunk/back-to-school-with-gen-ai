# Back to School (with Gen AI)

This application shows how Generative AI can be used to convert a 
textbook in PDF format into embeddings, store them in a vector database, 
and then use them along with OpenAI to generate study questions and
answer questions about a particular topic within the textbook. 

## Prerequisites

* Python 3.9+
* [Splunk Distribution of the OpenTelemetry Collector](https://docs.splunk.com/observability/en/gdi/opentelemetry/opentelemetry.html#otel-intro-install)
* An OpenAI account (set via the `OPENAI_API_KEY` environment variable) that has access to utilize the API

## Prepare the Environment

Execute the following commands to prepare the environment: 

``` bash
# clone the repo 
git clone https://github.com/dmitchsplunk/back-to-school-with-gen-ai.git

# navigate to the directory repo
cd back-to-school-with-gen-ai
```

## Load the Text Book into the Vector Database

Before running the main application, follow the instructions in 
the [load-textbook example](./load-textbook/README.md) 
to load your text book of choice into the vector database. 

## Run the Main Application 

Let's start by creating a virtual environment:

``` bash
# create a virtual environment
python -m venv venv

# activate the virtual environment
source venv/bin/activate
```

Then we'll install the [pypdf](https://pypdf.readthedocs.io/en/stable/) Python library,
which we'll use to load and parse the PDF document:

``` bash
pip install langchain==0.3.24
pip install langchain_openai==0.3.14
pip install langchain-chroma==0.2.3
pip install langgraph==0.3.34
```

Ensure your OPENAI_API_KEY token is set as an environment variable before running
the application.  For example, if the token is not set as part of your profile,
use the following command to set it:

``` bash
export OPENAI_API_KEY=<your OpenAI API key value> 
```

To run the application, use the following command:

``` bash 
python app.py 
```

## Add OpenTelemetry Instrumentation

To capture traces from our application, let's add OpenTelemetry instrumentation. 
We'll start by installing the following packages: 

``` bash
pip install opentelemetry-distro==0.53b1
pip install openlit==1.33.20
```

Then run the following command to load additional instrumentation packags: 

``` bash
opentelemetry-bootstrap -a install
pip uninstall opentelemetry-instrumentation-openai-v2
```

Define the service name and environment: 

``` bash
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
export OTEL_SERVICE_NAME=back-to-school-with-gen-ai
export OTEL_RESOURCE_ATTRIBUTES='deployment.environment=back-to-school-with-gen-ai'
```

Now we can run the app with OpenTelemetry instrumentation: 

``` bash
opentelemetry-instrument python app.py
```
