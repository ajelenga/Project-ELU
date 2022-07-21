from flask import Flask, render_template, request, make_response

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/")
def home():
    with open("./data_csv/territories.csv") as file:
        return render_template("show_csv_data.html", csv=file)


if __name__ == "__main__":
    app.run(debug=True)
