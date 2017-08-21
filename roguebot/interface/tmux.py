import subprocess
import time

from roguebot.constants import SCREENSHOT_FILE


def send_key(key):
    """
    Executes a single keystroke command.
    """
    cmd_list = 'tmux send-keys -t ROGUE'.split()
    cmd_list.append(key)
    subprocess.call(cmd_list)
    time.sleep(0.0001)


def start_game():
    cmd_start = '/usr/bin/tmux send-keys -t ROGUE "/usr/games/rogue"'
    cmd_as_list = cmd_start.split()
    cmd_as_list.append("\n")
    subprocess.call(cmd_as_list)
    time.sleep(0.5)


def get_frame():
    """Tells tmux to write a screenshot. Reads it in."""
    cmd_take_screenshot = 'tmux capture-pane -t ROGUE'
    cmd_save_screenshot = 'tmux save-buffer %s' % SCREENSHOT_FILE
    subprocess.call(cmd_take_screenshot.split())
    subprocess.call(cmd_save_screenshot.split())

    time.sleep(0.0001)
    with open(SCREENSHOT_FILE) as fh:
        return fh.read()


def quit_game():
    send_key('Q')
    send_key('y')
    send_key(' ')
    send_key(' ')
    send_key('\n')
