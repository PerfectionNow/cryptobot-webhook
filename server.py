from flask import Flask, request, jsonify

app = Flask(__name__)

# Токен вашего бота (для проверки подлинности запросов)
WEBHOOK_TOKEN = "ВАШ_СЕКРЕТНЫЙ_ТОКЕН"

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    if request.headers.get('X-Crypto-Pay-API-Token') != WEBHOOK_TOKEN:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.json
    if data['status'] == 'paid':
        user_id = data['user_id']
        # Здесь логика вашего бота (отправка предсказания)
        print(f"Оплата получена от user_id: {user_id}")
    
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run()
