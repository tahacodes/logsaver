from flask import Flask, Response, request
import pymongo
import json

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host="localhost", port=27017, serverSelectionTimeoutMS=1000)
    db = mongo.logs_database
    mongo.server_info()
except:
    print("Couldn't connect to MongoDB")


@app.route('/', methods=['GET'])
def get():
    total = db.logs.count_documents({})
    successful = db.logs.count_documents({"status": "200"})
    return "tatal requests: {}\nfailed requests: {}\n".format(total, total - successful)

@app.route('/', methods=['POST'])
def post():
    data = request.files['file'].read().decode('ascii')
    final = []
    for line in data.splitlines():
        data = line.split(",")
        jsondata = {
            "status": data[0],
            "timestamp": data[1],
            "response": data[2],
        }
        final.append(jsondata)

    dbResponse = db.logs.insert_many(final)
    print(dbResponse.inserted_ids)

    return Response(
        response=json.dumps({"message": "saved"}),
        status=200,
        mimetype="application/json")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
