from flask import Flask, render_template
import random

app = Flask(__name__, static_url_path='')

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

@app.route('/')
def root():
    scramble = ["R ","R' ","L ","L' ","U ","U' ","B ","B' ","D ","D' ","F ","F' "]
    scramble = random_string_generator(20, scramble)

    return render_template("index.html", scramble=scramble)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5505)
