[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/asishb212/tcp_chatroom/blob/master/LICENSE)
# TCP Chatroom
![Python](https://img.shields.io/badge/-Python-black?style=plastic&logo=Python)
![Ngrok](https://img.shields.io/badge/-Ngrok-1F1E37?style=plastic&logo=ngrok)

A ngrok based tcp chatroom designed to simulate text-to-text communication. 

## Installation

* Install the required libraries:

		pip install -r requirements.txt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**For server only**:

* Create an [account](https://dashboard.ngrok.com/signup) in ngrok and follow the setup instructions [here](https://dashboard.ngrok.com/get-started/setup).

* Finally run the server script:

		python3 server.py

* This will output a customized hostname and port number in the terminal, make sure you note these down beforehand.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sample output:

		HOSTNAME = 4.tcp.ngrok.io
		PORT = 11947

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**For client only**:

* Run the client script with the above hostname and port:

		python3 client.py 4.tcp.ngrok.io 11947 bright_magenta

* Note that the third argument indicates the colour of your messages in the chatroom.
<br/>
Currently there are six colours to choose from - `green`, `red`, `yellow`, `light_cyan`, `light_yellow`, and `bright_magenta`.
