from flask import Flask
app = Flask(__name__)

@app.route('/')
def menuMaker():
  return 'Hello!! Prueba'

if __name__ == '__main__':
  app.run()
