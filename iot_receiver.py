from flask import Flask, request, jsonify

app = Flask(__name__)

# 가속도계 데이터를 받는 라우트 정의
@app.route('/accelerometer-data', methods=['POST'])
def receive_accelerometer_data():
    data = request.json  # 클라이언트로부터 받은 JSON 데이터
    print("Received accelerometer data:", data)

    # 처리 결과를 클라이언트에게 응답
    return jsonify({"status": "success", "message": "Data received successfully."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
