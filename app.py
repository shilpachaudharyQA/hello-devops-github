from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print("Hello DevOps - updated version")
    print("Hello DevOps - Second ve")
    print("Hello DevOps - feature-branch")
    return "Hello DevOps!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)