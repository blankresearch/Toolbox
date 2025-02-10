from elasticsearch import Elasticsearch
from database_connector import DatabaseConnector
from tqdm import tqdm

# Establish Elasticsearch connection
es_connector = DatabaseConnector(db_type="elasticsearch", environment="prod")
es_connector.connect()
es = es_connector.connection

# Define the Elasticsearch index name
es_index = "index_name"

# Define the batch size and scroll timeout
batch_size = 3000
scroll_timeout = "10m"

es_query = {
    "query": {
        "match_all": {}
    },
    "size": batch_size,
}


es_result = es.search(index=es_index, body=es_query, scroll=scroll_timeout)

scroll_id = es_result["_scroll_id"]
total_documents = es_result["hits"]["total"]["value"]

# Iterate through the scroll
documents = []
progress_bar = tqdm(total=total_documents, desc="Retrieving documents")

while len(es_result["hits"]["hits"]) > 0:
    # Extract the documents from the search result
    documents.extend([hit["_source"] for hit in es_result["hits"]["hits"]])
    progress_bar.update(len(es_result["hits"]["hits"]))

    # Perform the scroll
    es_result = es.scroll(scroll_id=scroll_id, scroll=scroll_timeout)
    scroll_id = es_result["_scroll_id"]

progress_bar.close()

# Print the retrieved documents
for doc in documents:
    print(doc)
