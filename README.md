# python-flask-getting-started
[![codecov](https://codecov.io/gh/gsaini/python-flask-getting-started/graph/badge.svg?token=VGBPGOC9JE)](https://codecov.io/gh/gsaini/python-flask-getting-started)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![CodeCov](https://img.shields.io/badge/codecov-%23ff0077.svg?style=for-the-badge&logo=codecov&logoColor=white)

[Flask](https://flask.palletsprojects.com/en/stable/) is a lightweight, flexible, and popular Python microframework for building web applications, known for its simplicity and ease of use, allowing developers to focus on application logic rather than infrastructure. 


## PostgreSQL: The World's Most Advanced Open Source Relational Database
PostgreSQL is a powerful, open source object-relational database system with over 35 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.


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
