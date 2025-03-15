import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask on Render!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default to 10000 if no PORT is set
    app.run(host='0.0.0.0', port=port)
