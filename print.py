from arango import ArangoClient

client = ArangoClient(hosts='http://app_arangodb_db_container_1:8529')

### USE OF PLAIN TEXT PASSWORD
### IS FOR DEMONSTRATION PURPOSES ONLY

db = client.db('test', username='root', password='passwd')


# Execute an AQL query and iterate through the result cursor.
cursor_names = db.aql.execute('FOR doc IN famous_directors RETURN doc')

director_names = [document['name'] for document in cursor_names]

cursor_films = db.aql.execute('FOR doc IN famous_directors RETURN doc')

director_films = [document['film'] for document in cursor_films]

for k, v in zip(director_names, director_films):
    print(k,v)

