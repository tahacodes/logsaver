from flask import Flask
import pymongo

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host="localhost", port=27017, serverSelectionTimeoutMS=1000)
    db = mongo.demo
    mongo.server_info()
except:
    print("Couldn't connect to MongoDB")


@app.route('/', methods=['GET'])
def get():
    return


@app.route('/', methods=['POST'])
def post():
    try:
        log = {
            "status": 200,
            "timestamp": 1614033055,
            "output": "CREATED"
        }
        dbResponse = db.logs.insert_one(log)
        for attr in dir(dbResponse):
            print(attr)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    app.run(port=8080, debug=False)
