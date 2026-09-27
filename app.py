from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "app": "MJ Downloader",
        "status": "online"
    })

@app.route("/download", methods=["POST"])
def download():
    data = request.get_json(silent=True) or {}
    url = (data.get("url") or "").strip()

    if not url:
        return jsonify({"error": "URL is required"}), 400

    return jsonify({
        "status": "received",
        "url": url
    })

if __name__ == "__main__":
    app.run()
