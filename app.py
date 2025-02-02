from flask import Flask, request, render_template
from query import query_rag

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    gemma2_response = None
    llama3_response = None
    gemma2_source = None
    llama3_source = None
    if request.method == "POST":
        query_text = request.form["query_text"]
        gemma2_response, gemma2_source = query_rag(query_text,"gemma2")
        llama3_response, llama3_source= query_rag(query_text,"llama3")
    return render_template("index.html", gemma2_response=gemma2_response, llama3_response=llama3_response, gemma2_source=gemma2_source, llama3_source=llama3_source)

if __name__ == "__main__":
    app.run(debug=True, port=5500)