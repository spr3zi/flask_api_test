import json
import random
from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_quote():
    with open('quotes.json') as f:
        data = json.load(f)
        chosen=random.choice(list(data))
        return(chosen)

app.run(host='0.0.0.0', port=81)
