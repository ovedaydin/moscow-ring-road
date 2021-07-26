from flask import Flask, render_template
from distance_calculator.geo import geo

app = Flask(__name__)
#This where we get the the geo as a blueprint on /
app.register_blueprint(geo, url_prefix="")

@app.route("/")
def test():
    return "<h1>Test<h1/>"

@app.errorhandler(404)
def error_404(e):
    return '<h1>No source like your request.</h1>', 404

if __name__=="__main__":
    app.run(debug=True)
