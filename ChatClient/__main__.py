__author__ = 'Antoine'
import chat_client
import sys


def start_chat(arg_list, pipe_in, pipe_out):
    arg_list.pop(0)
    if len(arg_list) == 2:
        host = arg_list[0]
        try:
            port = int(arg_list[1])
        except e:
            return
        chat_client.ChatClient(host, port, pipe_in, pipe_out)  # open("ChatClient/get_req", 'r')
    else:
        print "usage: python ChatClient <host> <port>"

start_chat(sys.argv, sys.stdin, sys.stdout)