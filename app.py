from flask import Flask, render_template, Response, jsonify
import parking

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(parking.generate_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/status')
def status():
    free, occupied, suggested = parking.get_parking_status()
    return jsonify({'free': free, 'occupied': occupied, 'suggested': suggested})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
