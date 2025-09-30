from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload_room", methods=["POST"])
def upload_room():
    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    furniture = [{"box":[100,200,200,400],"class_id":56},{"box":[300,250,400,450],"class_id":57}]
    return jsonify({"furniture":furniture})

@app.route("/wall_suggestions", methods=["POST"])
def wall_suggestions():
    file = request.files["file"]
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    suggestions = ["/static/design1.jpg","/static/design2.jpg","/static/design3.jpg"]
    return jsonify({"suggestions":suggestions})

@app.route("/generate_wall_designs", methods=["POST"])
def generate_wall_designs():
    file = request.files["file"]
    wall_id = request.form.get("wall_id","wall1")
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    ai_designs = [f"/static/ai_{wall_id}_1.jpg",f"/static/ai_{wall_id}_2.jpg",f"/static/ai_{wall_id}_3.jpg"]
    return jsonify({"ai_designs":ai_designs})

@app.route("/suggest_materials", methods=["POST"])
def suggest_materials():
    materials = [
        {"name":"Oak Wood","type":"wood","color":"brown","cost_per_sqft":15},
        {"name":"Marble","type":"stone","color":"white","cost_per_sqft":50},
        {"name":"Matte Paint","type":"paint","color":"beige","cost_per_sqft":5}
    ]
    return jsonify({"materials":materials})

@app.route("/video_to_3d", methods=["POST"])
def video_to_3d():
    file = request.files["file"]
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    reconstructed_scene = "/static/3d_scene_placeholder.glb"
    suggestions = [{"object":"Sofa","position":[1,0,2]}, {"object":"Coffee Table","position":[1,0,1]}]
    return jsonify({"scene":reconstructed_scene,"suggestions":suggestions})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
