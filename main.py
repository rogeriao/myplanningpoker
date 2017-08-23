import os
from flask import Flask, jsonify, request
from config import DevConfig
from cloudant.client import Cloudant
from dotenv import load_dotenv

app = Flask(__name__)

app.config.from_object(DevConfig)

@app.route('/')
def home():
    return ""

if __name__ == "__main__":
	app.run()
