from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

users = None

@app.route('/')
def index():
	return render_template('./index.html')

@socketio.on('my event')
def event_handler(json):
	print('Received response from ' + str(json))
	# d = dict(json)
	# users = []
	# if d['user'] not in users:
	# 	users.append(d['user'])
	# print(users)
	socketio.emit('my response', json)

if __name__ == '__main__':
    socketio.run(app, debug=True)