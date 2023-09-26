import socket
import keyboard
import json

PORT = 5801
dict_to_send = {}
class Action:
    def __init__(self, button: str, name: str):
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
    all_actions = [ Action("ARM_TO_0", "change me"),
                    Action("ARM_TO_CONE_3", "change me"),
                    Action("ARM_TO_CONE_2", "change me"),
                    Action("ARM_TO_CONE_1", "change me"),

                    Action("ARM_TO_CUBE_3", "change me"),
                    Action("ARM_TO_CUBE_2", "change me"),
                    Action("ARM_TO_CUBE_1", "change me"),

                    Action("ARM_COLLECT_CUBE_SHELF", "change me"),
                    Action("ARM_COLLECT_CONE_SHELF", "change me"),

                    Action("GRIPPER_TO_CUBE", "change me"),
                    Action("GRIPPER_TO_CONE", "change me"),
                    Action("GRIPPER_TO_CLOSED", "change me"),

                    Action("GRIPPER_IN", "change me"),
                    Action("GRIPPER_OUT", "change me")]
    while True:
        for action in all_actions:
            action.register_action()
        send()
        

if __name__ == '__main__':
    main()
    