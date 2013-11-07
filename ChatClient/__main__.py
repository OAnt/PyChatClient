__author__ = 'Antoine'
import chat_client
import sys

chat_client.ChatClient("localhost", 4000, sys.stdin, sys.stdout)
