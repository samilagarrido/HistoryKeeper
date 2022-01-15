from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

with open('file.txt','r') as file:
    conversation = file.read()

bott = ChatBot("History Keeper Chatbot")
trainer2 = ListTrainer(bott)
trainer2.train([        "Hello",
    "Hello!",
    "Hi",
    "Hi!",
    "Tell me about Samila's mother",
    "Her name is Maria. She is a self-employed worker. She has 3 children. Samila is the youngest. She works together with her husband. When the children arrived, she took as long as she needed from work. She had a support network, people who contributed to raising her children.",
    "Want to hear a story?",
    "Yes",
    "Her name is Maria. She is a self-employed worker. She has 3 children. Samila is the youngest. She works together with her husband. When the children arrived, she took as long as she needed from work. She had a support network, people who contributed to raising her children.",
    "How nice!",
    "She is Samila's mother.",
    "Goodbye",
    "Goodbye!"
    
    ])
trainer = ChatterBotCorpusTrainer(bott)
trainer.train("chatterbot.corpus.english")
#trainer2.train(["Thank You","Welcome"])

@app.route("/")
def home(): 
	return render_template("home.html")

@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	return str(bott.get_response(userText))
if __name__ == "__main__":
	app.run()