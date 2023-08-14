from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True)