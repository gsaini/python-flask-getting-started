# python-flask-getting-started
[Flask](https://flask.palletsprojects.com/en/stable/) is a lightweight, flexible, and popular Python microframework for building web applications, known for its simplicity and ease of use, allowing developers to focus on application logic rather than infrastructure. 


## Server-Sent Events (SSE)

Server-Sent Events (SSE) provide a simple way to push updates from a server to a browser (client) over HTTP. SSE is unidirectional, meaning data flows only from the server to the client, and it is natively supported in browsers via the `EventSource` API.

### Use Cases for SSE
SSE is ideal for scenarios such as:
- Live notifications
- Stock price updates
- News feeds
- Chat messages (read-only streams)

### 📦 Key Characteristics of SSE

| **Feature**         | **Description**                     |
|----------------------|-------------------------------------|
| **Protocol**         | HTTP (not WebSocket)               |
| **Direction**        | Server → Client                    |
| **Reconnect Support**| Built-in automatic reconnects      |
| **Format**           | Text-based (`text/event-stream`)   |
| **Browser API**      | `EventSource`                      |

## Generate a Self-Signed SSL Certificate
Run the following in terminal (Python must be installed):

```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```


## How to Run
Run the Flask server:

```
python server.py
```
