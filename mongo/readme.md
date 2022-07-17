# Mongo Course Notes

Document - a way to organize and store data as a set of field-value pairs.

Field - a unique identifier for a datapoint.

Value - data related to a given identifier.

Collection - an organized store of documents in MongoDB, usually with common fields between documents. There can be many collections per database and many documents per collection.

Replica Set - a few connected machines that store the same data to ensure that if something happens to one of the machines the data will remain intact. Comes from the word replicate - to copy something.

Instance - a single machine locally or in the cloud, running a certain software, in our case it is the MongoDB database.

Cluster - group of servers that store your data.

DB Username/Pass:
username: m001-student
password: m001-mongodb-basics

Standard JSON format includes quotes around both keys and values

JSON Cons:
- Text-based: text parsing is very slow
- Space-consuming: JSON's readable format is not space efficient
- Limited: Only a limited number of datatypes supported (string, boolean, numbers, arrays)

MongoDB addresses this with BSON:
- BSON is a binary representation for storing data in JSON format; it is better performing than JSON
- Other BSON benefits:
    - As opposed to being encoded in UTF-8 strings like JSON, BSON is binary encoded
    - Supports Strings, Booleans, Numbers (Integer, Long, Float, ...), Array, Date, Raw Binary
    - Con:
        Readable by Machine only

MongoDB stores data in BSON internally and over the network
- MongoDB also supports JSON, and BSON is viewable in JSON format

Generally speaking, data is stored in BSON but readable in JSON

mongodump --uri "mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/<database>" # Exports in BSON format

mongoexport --uri="mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/<database>" --collection=sales --out=sales. json # Exports in JSON format

mongorestore --uri "mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/<database>"  --drop dump # Imports data in BSON dump

mongoimport --uri="mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/<database>" --drop sales.json # Imports data in JSON (or other supported formats, like csv)
- we can also specify the name of the collection that will contain the data; if not, the collection will take on the name of the file you're importing from

URI - Uniform Resource Identifier
- In MongoDB, we use a srv string to connect to our Atlas cluster

show dbs - to list all dbs in cluster
use <database_name> - to connect to a specific db
show collections - once connected to a specific db, show all collections in that db

Querying a collection for a specific document: db.zips.find({"state": "NY"} # note: the results are not ordered in the order in which they're entered
- After running the above command, we are prompted to use "it" to view more results
-- "it" short of "iterate" allows us to iterate through the cursor object that is return by the find command
--- a cursor is a pointer to the result set of a query
---- a pointer is a direct address to the memory location
- using .count() on the cursor object returned would return the number of documents matching that specific query
- using .pretty() formats results into JSON structure
