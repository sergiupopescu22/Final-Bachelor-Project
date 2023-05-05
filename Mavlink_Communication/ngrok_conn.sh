#!/bin/bash
xterm -e "ngrok http --domain=drone-server.ngrok.app 1234; exec bash"