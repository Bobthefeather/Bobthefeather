from flask import Flask
app = Flask(__name__)

print('test')

@app.route('/')
def home():
    return 'Hello, your name goes here!'

@app.route('/shop')
def home():
    return 'this is not your home page!'

if __name__=='__main__':
    app.run()