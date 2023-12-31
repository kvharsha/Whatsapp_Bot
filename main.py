from flask import Flask, request
from googlesearch import search
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

@app.route("/", methods=["POST"])
def bot():
    try:
        # user input
        usermsg = request.values.get('Body')

        searchresults = search(usermsg, num_results=5)

        # creating object of MessagingResponse
        response = MessagingResponse()

        # searching and storing urls
        for i in searchresults:
            message = Message()
            message.body(i)
            response.append(message)

        return str(response)
    except Exception as e:
    
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
