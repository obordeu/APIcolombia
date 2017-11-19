from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello!! This is our awesome web api for colombia'

if __name__ == '__main__':
  app.run()
