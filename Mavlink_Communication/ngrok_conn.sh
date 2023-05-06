#!/bin/bash
# xterm -e "ngrok http --hostname=drone-server.ngrok.app 1234; exec bash"
sleep 20
ngrok http --hostname=drone-server.ngrok.app 1234; exec bash