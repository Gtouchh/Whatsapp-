from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Rota para receber mensagens de WhatsApp
@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    msg_body = request.form.get('Body')
    
    # Resposta automática para a mensagem recebida
    resp = MessagingResponse()
    msg = resp.message()

    if 'oi' in msg_body.lower():
        msg.body('Olá! Como posso ajudar?')
    else:
        msg.body('Desculpe, não entendi sua mensagem.')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
