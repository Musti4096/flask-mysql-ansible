from flask import Flask, render_template,

app = Flask(__name__)
developer_name = "Mustafa"


@app.route("/", methods=["GET"])
def main_get():
    return render_template("index.html", developer_name= developer_name, not_valid= False)
   
    

#    app.run(host='0.0.0.0', port=80)
if __name__ == "__main__":
    #app.run(debug = True)
    app.run(host="0.0.0.0", port=80)