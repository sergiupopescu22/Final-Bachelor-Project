def ack(master, type, blocking, timeout):

    print('Waiting for confirmation...')
    msg = master.recv_match(type=type, blocking=blocking, timeout=timeout)
    if msg:
        print(msg)
        if msg.result == 0:
            print("----COMMAND ACCEPTED----")
        else:
            print("----COMMAND DENIED----")
        return True

    else:
        print("Command failed! Trying again...\n")
        return False
