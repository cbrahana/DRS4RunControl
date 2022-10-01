import keyboard
import time

HOST = 128.111.19.39
PORT = 52090

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        #Section for handling data
        oper_data = data.decode("ascii")
        decoded_commands_list = oper_data.split(" ")
        if decoded_commands_list[0] == "startRun":
            keyboard.press_and_release('ctrl+s')
            time.sleep(0.1)
            keyboard.write(decoded_commands_list[1] + ".dat")
            time.sleep(0.1)
            keyboard.press_and_release("enter")
            time.sleep(0.1)
            keyboard.write(decoded_commands_list[2])
            time.sleep(0.1)
            keyboard.press_and_release("enter")
        if not data:
            break
