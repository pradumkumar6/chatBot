from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import os
import json

app = Flask(__name__)
CORS(app)

bot = ChatBot('CDK')

trainer=ListTrainer(bot)

#bot.set_trainer(ListTrainer)
for _file in os.listdir('dataset'):
    chats = open('dataset/' + _file,encoding="utf8").readlines()
    #print(chats)
    trainer.train(chats)

@app.route('/')
def newcha():
    return render_template('chatbotUI.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        query = request.get_json()['ques']
        response = bot.get_response(query)
        #print(response)
        # return render_template("dev1.html",response=response)
        return str(response)

    # return "Chal gya re!!!"
    # return render_template('dev1.html')


# if request.method == 'GET':
# response = bot.get_response(request)
# response = str(response)
# response = "this is get"
# print('Bot: '+response)

if __name__ == "__main__":
    app.run()
