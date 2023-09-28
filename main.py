import socket
import keyboard
import json

PORT = 5801
dict_to_send = {}
class Action:
    def __init__(self, name: str, button: str):
        self.button = button
        self.name = name
    
    def register_action(self):
        dict_to_send[self.name] = keyboard.is_pressed(self.button)
        


def send():
    j = json.dumps(dict_to_send)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(j.encode(), ("255.255.255.255", PORT))

# TODO: change all change me's
def main():
    all_actions = [ Action("ARM_TO_0", "backspace"),
                    Action("ARM_TO_CONE_3", "q"),
                    Action("ARM_TO_CONE_2", "a"),
                    Action("ARM_TO_CONE_1", "z"),

                    Action("ARM_TO_CUBE_3", "w"),
                    Action("ARM_TO_CUBE_2", "s"),
                    Action("ARM_TO_CUBE_1", "x"),

                    Action("ARM_COLLECT_CUBE_SHELF", "o"),
                    Action("ARM_COLLECT_CONE_SHELF", "p"),
                    
                    Action("GRIPPER_TO_CUBE", "9"),
                    Action("GRIPPER_TO_CONE", "0"),
                    Action("GRIPPER_TO_OPEN", "8"),

                    Action("GRIPPER_IN", "f"),
                    Action("GRIPPER_OUT", "h"),
                    Action("GRIPPER_STOP", "g")]
    while True:
        for action in all_actions:
            action.register_action()
        send()
        # print(dict_to_send.values()) # for debugging 
        

if __name__ == '__main__':
    main()
    