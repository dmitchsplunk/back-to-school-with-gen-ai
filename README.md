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

Follow the instructions in the [load-textbook example](./load-textbook/README.md) 
to load your text book of choice into the vector database. 

