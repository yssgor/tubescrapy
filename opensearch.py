from opensearchpy import OpenSearch
class Opensearch():
    def __init__(self, username, password):
        self.es = OpenSearch(
            hosts = [{'host': 'localhost', 'port': 9200}],
            http_compress = True,
            http_auth=(username, password),
            verify_certs = False,
        )

    def exist_index(self, index):
        index_body= {
        'settings': {
            'index': {
                'number_of_shards': 4
                }
            }
        }
        try:
            response = self.es.indices.create(index, body=index_body)
        except:
            print("index já existente")