from flask import Flask, Response
import json
import time

app = Flask(__name__)

@app.route('/events')
def sse():
    def event_streams():
        while True:
            data = {
                'message': 'Hello from python server',
                'time': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            yield f"data: {json.dumps(data)}\n\n"
            time.sleep(5)
    return Response(event_streams(), content_type='text/event-stream')

if __name__ == 'main':
    app.run(port=5000, debug=True, threaded=True)
