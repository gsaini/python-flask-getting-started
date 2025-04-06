from flask import Flask, Response, render_template
import json
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def sse():
    def event_stream():
        while True:
            data = {
                'message': 'Hello from Python server',
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            yield f'data: {json.dumps(data)}\n\n'
            time.sleep(5)

    return Response(event_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)
