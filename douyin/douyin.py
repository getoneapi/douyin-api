import datetime
import json
import re

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
did_ck = {}


@app.route('/video', methods=['POST'])
def video_list():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    video_id = data['id']
    except Exception as e:
           return {
                 'code': 0,
                 'data': str(e)
            }


@app.route('/user/profile', methods=['POST'])
def get_user():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    user_id = data['id']
    except Exception as e:
           return {
                 'code': 0,
                 'data': str(e)
            }


@app.route('/feed/profile', methods=['POST'])
def get_feed():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    feed_id = data['id']
    except Exception as e:
           return {
                 'code': 0,
                 'data': str(e)
            }



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6666, debug=True)
