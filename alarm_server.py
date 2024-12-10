from flask import Flask, request, jsonify
import pandas as pd
import json
import requests
from requests.auth import HTTPDigestAuth
url  = 'http://192.168.1.8/LAPI/V1.0/Channels/1/Smart/CrossLineDetection/Areas'
 

app = Flask(__name__)

@app.before_request
def log_request_info():
    print(f"Headers: {request.headers}")
    #print(f"Body: {request.get_data()}")
     
@app.route('/LAPI/V1.0/System/Event/Notification/Alarm', methods=['POST'])
def alarm_notification():
    if request.is_json:
        data = request.get_json()
        print(f"Received data: {data}")
        return jsonify({"status": "success"}), 200
    else :

        request_str = request.get_data().decode('utf-8').strip()
        request_lines = request_str.splitlines(True)

        # Parse JSON data
        data = json.loads(request_str)

        # Accessing elements
        reference = data["Reference"]
        alarm_info = data["AlarmInfo"]
        related_objects = data["RelatedObjects"]

        # Print parsed data
        print(f"Reference: {reference}")
        print(f"Alarm Type: {alarm_info['AlarmType']}")
        print(f"Alarm Level: {alarm_info['AlarmLevel']}")
        print(f"Time Stamp: {alarm_info['TimeStamp']}")
        print(f"Alarm Sequence: {alarm_info['AlarmSeq']}")
        print(f"Alarm Source ID: {alarm_info['AlarmSrcID']}")
        print(f"Alarm Source Name: {alarm_info['AlarmSrcName']}")
        print(f"Device ID: {alarm_info['DeviceID']}")
        print(f"Related ID: {alarm_info['RelatedID']}")

        print(f"Object Number: {related_objects['ObjectNum']}")
        for obj in related_objects["ObjectList"]:
            print(f"Object Type: {obj['ObjectType']}")
            print(f"Object ID: {obj['ObjectID']}")
        #print(json_string)
        return jsonify({"status": "success"}), 200


    #print(f"Received data: {data}")
    return {"status": "success"}, 200

 
def getArea():
    response = requests.get(url,auth=HTTPDigestAuth('admin','password123456!'), verify=False,  stream=True)   
    print("Response code:" + str(response.status_code))
    print("Response code:" + str(response.json()))
    data = response.json()
    #print(data['Enabled'])

if __name__ == '__main__':
    #getArea()
    app.run(host='0.0.0.0', port=5000)
