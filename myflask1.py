from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/hello/<leslie>')
def hello_name(leslie):
        return 'Hello %s!' % leslie

if __name__ == '__main__':
        app.run()