import yaml
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def index():
    print_yaml()
    return "YAML printed in console"


def print_yaml():
    stream = open("test.yaml", "r")
    dictonary = yaml.safe_load(stream)

    for key, value in dictonary.items():
        print(key + " : " + str(value))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)