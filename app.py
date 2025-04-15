from flask import Flask, request, send_file
import socket
import datetime
import os

app = Flask(__name__)

@app.route('/asset-verification/confirm')
def fake_report():
    ip = request.remote_addr
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except:
        hostname = "Unknown"

    log_entry = f"{datetime.datetime.now()} - IP: {ip} - Hostname: {hostname}\n"
    with open("click_log.txt", "a") as f:
        f.write(log_entry)

    return '''
    <html>
    <head><title>Cybersecurity Awareness Test</title></head>
    <body>
        <h1>This was a cybersecurity awareness test.</h1>
        <p>Your visit has been logged.</p>
        <img src='/static/meme.jpg' alt='Meme'>
    </body>
    </html>
    '''

@app.route('/static/meme.jpg')
def serve_meme():
    return send_file("static/meme.jpg", mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
