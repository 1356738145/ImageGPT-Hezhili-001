from flask import Flask,render_template,request
import os
import replicate
import json
import time
import requests

os.environ["REPLICATE_API_TOKEN"] = "r8_WM1KFdiQb73xEdAv0wot7oWAuuDUo3K328v3J"
app=Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():
    if request.method =="POST":
        q = request.form.get("question")
        body = json.dumps({"version": "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf", "input": { "prompt": q } })
        headers = {'Authorization': 'Token r8_Ck2kkbp4xm8WENxpzlUkWQpabICdQL01iDLjW','Content-Type': 'application/json'}
        output = requests.post('https://api.replicate.com/v1/predictions',data=body,headers=headers)
        time.sleep(10)
        get_url = output.json()['urls']['get']
        r = requests.post(get_url,headers=headers).json()['output']
        return(render_template("index.html", result=r[0]))
    else:
        return(render_template("index.html", result="waiting"))

if __name__=="__main__":
    app.run()
