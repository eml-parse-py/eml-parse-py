from flask import Flask

app = Flask(__name__, static_folder='./app/static/parse_py_ui/build', static_url_path='/')


@app.route("/")
def hello():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(debug=True)
