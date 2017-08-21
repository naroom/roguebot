from roguebot.interface import frame_parser
from roguebot.interface import tmux
from roguebot.interface import state

from roguebot.strategy.naive import naive


def restart_game_if_needed():
    frame = tmux.get_frame()
    if not 'Level:' in frame:
        tmux.quit_game()
        tmux.start_game()


def game_loop():
    restart_game_if_needed()

    frames = state.FrameHistory()
    stats = state.Stats()

    while True:
        frame = tmux.get_frame()
        stats.parse(frame)
        frames.add(frame)

        if frame_parser.check_victory(frame):
            print(frame)
            break

        if frame_parser.check_death(frame):
            print(frame)
            tmux.send_key(' ')  # continue past "killed by" screen
            tmux.send_key(' ')  # continue past top scores screen
            tmux.start_game()  # begin anew
            continue

        if frame_parser.check_more(frame):
            tmux.send_key(' ')
            continue

        move = naive.get_move(frames, stats)
        # print(move)
        tmux.send_key(move)


def main():
    # Before running, You will need to
    # open a terminal and run the command:
    # tmux new-session -s ROGUE
    game_loop()




if __name__ == "__main__":
    main()

    # cmd_newline = "/usr/bin/tmux send-keys -t ROGUE \n"
    # subprocess.call(cmd_newline.split())
