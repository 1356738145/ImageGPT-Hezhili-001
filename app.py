from flask import Flask,render_template,request
import os
import replicate
import json
import time
import requests
#
os.environ["REPLICATE_API_TOKEN"] = "r8_WM1KFdiQb73xEdAv0wot7oWAuuDUo3K328v3J"
m = replicate.models.get("tstramer/midjourney-diffusion")
version = m.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")
app=Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():
    
    if request.method == "POST":
        q = request.form.get("q")
        body = json.dumps({"version": "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf", "input": { "prompt": q } })
        headers = {'Authorization': 'Token 787f515cb0624813736c11e7fefec66473394f02','Content-Type': 'application/json'}
        output = requests.post('https://api.replicate.com/v1/predictions',data=body,headers=headers)
        time.sleep(10)
        get_url = output.json()['urls']['get']
        get_result = requests.post(get_url,headers=headers).json()['output']
        return(render_template("index.html", result=get_result[0]))
    else:
        return(render_template("index.html", result="waiting..."))

if __name__ == "__main__" :
    app.run()
