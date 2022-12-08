import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://MrAbhi2k3:ghp_147bkkabcdefgh@github.com/MrAbhi2k3/MdiskVideoBot
os.system("git clone https://MrAbhi2k3:token@github.com/MrAbhi2k3/MdiskVideoBot ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 main.py &")
