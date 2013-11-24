__author__ = 'Antoine'
import chat_client
import sys


def conv_host(host):
    return host


def conv_port(i):
    try:
        return int(i)
    except ValueError:
        return None


def conv_pipe(a_pipe):
    try:
        return open(a_pipe, 'w+r')
    except IOError:
        return None


word_eq = {"-host": [None, conv_host],
           "-port": [None, conv_port],
           "-in": [sys.stdin, conv_pipe],
           "-out": [sys.stdout, conv_pipe]}


def start_chat(arg_list, input_conv):
    arg_list.pop(0)
    for i in xrange(0, len(arg_list) - 1):
        if arg_list[i] in input_conv.keys():
            input_conv[arg_list[i]][0] = input_conv[arg_list[i]][1](arg_list[i + 1])
    chat_client.ChatClient(input_conv["-host"][0],
                           input_conv["-port"][0],
                           input_conv["-in"][0],
                           input_conv["-out"][0])  # open("ChatClient/get_req", 'r')

start_chat(sys.argv, word_eq)