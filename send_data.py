import requests
import pprint
import json
import subprocess
import time

endpoint = 'http://33e2-112-134-227-222.ngrok.io/predict'
filename = 'sample4.wav'
device_id = 'homenet_iot_9'
count = 1


def send_raw(wav):
    files = {'file': open(wav, 'rb')}
    payload = (('device_id', device_id),)
    r = requests.post(endpoint, files=files, data=payload)

    print('Response for file upload')
    print('Status: ' + str(r))
    # print(r.content)
    pprint.pprint(json.loads(r.content))
    print('API Time elapsed: ' + str(r.elapsed))


while True:
    start_time = time.time()
    p = subprocess.call(["arecord", filename, "-d", "3", "-r", "44100", "-f", "S16_LE"])

    print('subprocess: ')
    print(p)

    send_raw(filename)
    print("Predict " + str(count))
    print("Total time: %s seconds" % (time.time() - start_time))
    print('sleep for 10 seconds')
    time.sleep(10)
    count += 1
    print()
