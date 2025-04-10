from flask import Flask, Response, render_template, jsonify, request
import json
import time
from db import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def get_users():
    """Get all users from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]  # Get column names
    users = [dict(zip(column_names, row)) for row in rows]  # Map column names to values
    cursor.close()
    conn.close()

    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user in the database."""
    new_user = request.get_json()
    name = new_user.get('name')
    email = new_user.get('email')

    # Validate input
    if not name or not email:
        return jsonify({'error': 'Name and email are required fields.'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Use RETURNING to get the id of the newly inserted row
        cursor.execute(
            'INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id',
            (name, email)
        )
        user_id = cursor.fetchone()[0]  # Fetch the returned id
        conn.commit()
        return jsonify({'id': user_id, 'name': name, 'email': email}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to create user. ' + str(e)}), 400
    finally:
        cursor.close()
        conn.close()
        


@app.route('/events')
def sse():
    def event_stream():
        while True:
            data = {
                'message': 'Hello from Server using Flask!',
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            yield f'data: {json.dumps(data)}\n\n'
            time.sleep(5)

    return Response(event_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000, ssl_context=('cert.pem', 'key.pem'))


