from flask import Flask, request, jsonify
from confluent_kafka import Producer

app = Flask(__name__)

# Kafka 설정
kafka_config = {
    'bootstrap.servers': 'YOUR_KAFKA_SERVER',  # Kafka 서버 주소
}
kafka_topic = 'step-count-topic'  # Kafka 토픽 이름

producer = Producer(**kafka_config)

# 걸음수 데이터를 Kafka로 전송하는 함수
def send_to_kafka(data):
    producer.produce(kafka_topic, data.encode('utf-8'))
    producer.flush()

# REST API 엔드포인트: 걸음수 데이터를 받는다
@app.route('/steps', methods=['POST'])
def receive_steps():
    data = request.json  # 클라이언트로부터 받은 JSON 데이터
    steps_data = data.get('steps')
    if steps_data is not None:
        send_to_kafka(str(steps_data))  # Kafka로 데이터 전송
        return jsonify({'message': 'Data received and sent to Kafka'}), 200
    else:
        return jsonify({'error': 'Missing data'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
