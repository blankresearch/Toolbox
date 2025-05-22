from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200", verify_certs=False)

try:
    # Check connection
    if es.ping():
        print("Connected to Elasticsearch")
    else:
        print("Failed to connect")

    # Get index mapping (description) for 'books_data_bis'
    mapping = es.indices.get_mapping(index="books_data_bis")
    print("Index mapping for 'books_data_bis':")
    print(mapping)
except Exception as e:
    print(f"Error: {e}")
