from arango import ArangoClient

# Initialize the client for ArangoDB.
#client = ArangoClient(hosts='http://localhost:8529')
client = ArangoClient(hosts='http://app_arangodb_db_container_1:8529')

# Connect to "_system" database as root user.
sys_db = client.db('_system', username='root', password='passwd')

# Create a new database named "test".
sys_db.create_database('test')

# Connect to "test" database as root user.
db = client.db('test', username='root', password='passwd')

# Create a new collection named "famous directors"

famous_directors = db.create_collection('famous_directors')

# Add a hash index to the collection.

famous_directors.add_hash_index(fields=['name'], unique=True)

# Insert new documents into the collection.

famous_directors.insert({'name': 'David Lynch', 'film': 'Lost Highway'})
famous_directors.insert({'name': 'Martin Scorsese', 'film': 'Taxi Driver'})
famous_directors.insert({'name': 'Joel and Ethan Coen', 'film': 'Fargo'})
famous_directors.insert({'name': 'David Cronenberg', 'film': 'Crash'})
famous_directors.insert({'name': 'Quentin Tarantino', 'film': 'Kill Bill'})


# Execute an AQL query and iterate through the result cursor.
cursor = db.aql.execute('FOR doc IN famous_directors RETURN doc')
director_names = [document['name'] for document in cursor]
director_films = [document['film'] for document in cursor]

