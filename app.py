from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    resp = VoiceResponse()
    resp.say("Hello! This is your voice agent. Please leave a message after the beep.")
    resp.record()
    return Response(str(resp), mimetype="text/xml")

@app.route("/")
def index():
    return "Voice Agent is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
