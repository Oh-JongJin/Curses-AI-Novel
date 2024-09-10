# import curses
# import sys
# import time
#
# from draw import draw_label_centered
#
#
# class Letgo:
#     def __init__(self, stdscr):
#         self.stdscr = stdscr
#         curses.curs_set(0)
#         self.height, self.width = stdscr.getmaxyx()
#         self.text_win = curses.newwin(3, self.width, self.height - 3, 0)
#         self.main_win = curses.newwin(self.height - 3, self.width, 0, 0)
#         curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
#         curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
#
#         curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)
#         curses.init_pair(7, curses.COLOR_RED, curses.COLOR_BLACK)
#         curses.init_pair(8, curses.COLOR_GREEN, curses.COLOR_BLACK)
#         curses.init_pair(9, curses.COLOR_BLUE, curses.COLOR_BLACK)
#
#         draw_label_centered(stdscr, 3,
#                             " █████╗ ███╗  ██╗██╗   ██╗ █████╗ ███╗  ██╗ ██████╗   ██████╗ ██████╗ ██╗███████╗████████╗",
#                             curses.color_pair(3))
#         draw_label_centered(stdscr, 4,
#                             "██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ██║██╔════╝   ██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝",
#                             curses.color_pair(3))
#         draw_label_centered(stdscr, 5,
#                             "███████║██╔██╗██║ ╚████╔╝ ███████║██╔██╗██║██║  ██╗   ██║  ██║██████╔╝██║█████╗     ██║   ",
#                             curses.color_pair(3))
#         draw_label_centered(stdscr, 6,
#                             "██╔══██║██║╚████║  ╚██╔╝  ██╔══██║██║╚████║██║  ╚██╗  ██║  ██║██╔══██╗██║██╔══╝     ██║   ",
#                             curses.color_pair(3))
#         draw_label_centered(stdscr, 7,
#                             "██║  ██║██║ ╚███║   ██║   ██║  ██║██║ ╚███║╚██████╔╝  ██████╔╝██║  ██║██║██║        ██║   ",
#                             curses.color_pair(3))
#         draw_label_centered(stdscr, 8,
#                             "╚═╝  ╚═╝╚═╝  ╚══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚══╝ ╚═════╝   ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   ",
#                             curses.color_pair(3))
#
#         draw_label_centered(stdscr, 15,
#                             "╚═╝  ╚═╝╚═╝  ╚══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚══╝ ╚═════╝   ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   ",
#                             curses.color_pair(3))
#
#     def draw_menu(self, stdscr, selected_row_idx, start_y, start_x):
#         menu_items = ['Continue', 'New Game', 'Settings', 'Quit']
#         for idx, item in enumerate(menu_items):
#             x = start_x + (20 - len(item)) // 2
#             y = start_y + idx
#             if idx == selected_row_idx:
#                 stdscr.attron(curses.color_pair(1))
#                 stdscr.addstr(y, x, item)
#                 stdscr.attroff(curses.color_pair(1))
#             else:
#                 stdscr.addstr(y, x, item)
#
#         # Draw menu border
#         stdscr.box()
#         stdscr.addch(start_y - 1, start_x - 1, curses.ACS_ULCORNER)
#         stdscr.addch(start_y - 1, start_x + 20, curses.ACS_URCORNER)
#         stdscr.addch(start_y + 4, start_x - 1, curses.ACS_LLCORNER)
#         stdscr.addch(start_y + 4, start_x + 20, curses.ACS_LRCORNER)
#         for i in range(4):
#             stdscr.addch(start_y + i, start_x - 1, curses.ACS_VLINE)
#             stdscr.addch(start_y + i, start_x + 20, curses.ACS_VLINE)
#         for i in range(20):
#             stdscr.addch(start_y - 1, start_x + i, curses.ACS_HLINE)
#             stdscr.addch(start_y + 4, start_x + i, curses.ACS_HLINE)
#
#     def display_text(self, text):
#         self.text_win.clear()
#         self.text_win.addstr(0, 0, text)
#         self.text_win.refresh()
#
#     def display_scene(self, scene):
#         self.main_win.clear()
#         for i, line in enumerate(scene.split('\n')):
#             self.main_win.addstr(i, 0, line)
#         self.main_win.refresh()
#
#     def display_title_screen(self):
#         self.main_win.clear()
#         title = "ANYANG DRIFT"
#         start_button = "[ Start Game ]"
#
#         # Display title
#         title_y = self.height // 4
#         title_x = (self.width - len(title)) // 2
#         self.main_win.attron(curses.color_pair(1) | curses.A_BOLD)
#         self.main_win.addstr(title_y, title_x, title)
#         self.main_win.attroff(curses.color_pair(1) | curses.A_BOLD)
#
#         # Display start button
#         button_y = self.height // 2
#         button_x = (self.width - len(start_button)) // 2
#         self.main_win.attron(curses.color_pair(2))
#         self.main_win.addstr(button_y, button_x, start_button)
#         self.main_win.attroff(curses.color_pair(2))
#
#         self.main_win.refresh()
#
#         # Wait for user input
#         while True:
#             key = self.stdscr.getch()
#             if key == ord('\n'):  # Enter key
#                 break
#
#     def run(self):
#         self.display_title_screen()
#
#         scenes = [
#             "You're at the starting line of the biggest motorcycle race in Anyang.",
#             "The crowd is roaring, and you can feel the adrenaline pumping.",
#             "As you rev your engine, you notice two paths ahead on the track."
#         ]
#
#         choices = [
#             ["1. Take the inside lane", "2. Go for the outside lane"],
#             ["1. Push your bike to the limit", "2. Maintain a steady pace"],
#             ["1. Take a risky shortcut", "2. Stick to the main track"]
#         ]
#
#         for i, scene in enumerate(scenes):
#             self.display_scene(scene)
#             self.display_text("Press any key to continue...")
#             self.stdscr.getch()
#
#             if i < len(choices):
#                 self.display_text("\n".join(choices[i]))
#                 while True:
#                     key = self.stdscr.getch()
#                     if key in [ord('1'), ord('2')]:
#                         break
#
#
# def main(stdscr):
#     curses.start_color()
#     game = Letgo(stdscr)
#     game.run()
#
#
# curses.wrapper(main)
# sys.exit()


######################

import curses
import random


def game_over():
    screen = curses.initscr()
    width = screen.getmaxyx()[1]
    height = screen.getmaxyx()[0]
    size = width * height
    char = [" ", ".", ":", "^", "*", "x", "s", "S", "#", "$"]
    b = []

    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, 0, 0)
    curses.init_pair(4, 1, 0)
    curses.init_pair(3, 6, 0)
    curses.init_pair(2, 4, 0)
    screen.clear

    for i in range(size + width + 1):
        b.append(0)

    while True:
        for i in range(int(width / 9)):
            b[int((random.random() * width) + width * (height - 1))] = 65
        for i in range(size):
            b[i] = int((b[i] + b[i + 1] + b[i + width] + b[i + width + 1]) / 4)
            color = (4 if b[i] > 15 else (3 if b[i] > 9 else (2 if b[i] > 4 else 1)))
            if i < size - 1:
                screen.addstr(int(i / width), i % width, char[(9 if b[i] > 9 else b[i])],
                              curses.color_pair(color) | curses.A_BOLD)

        screen.refresh()
        screen.timeout(30)
        if screen.getch() != -1: break

    curses.endwin()


def draw_title(stdscr, start_y, start_x):
    title = [
        "        ,----,",
        "      ,/   .`|",
        "    ,`   .'  :",
        "  ;    ;     /                    ,--,",
        ".'___,/    ,' __  ,-.           ,--.'|         ,---,",
        "|    :     |,' ,'/ /|           |  |,      ,-+-. /  |",
        ";    |.';  ;'  | |' | ,--.--.   `--'_     ,--.'|'   |",
        "`----'  |  ||  |   ,'/       \  ,' ,'|   |   |  ,\"' |",
        "    '   :  ;'  :  / .--.  .-. | '  | |   |   | /  | |",
        "    |   |  '|  | '   \__\/: . . |  | :   |   | |  | |",
        "    '   :  |;  : |   ,\" .--.; | '  : |__ |   | |  |/",
        "    ;   |.' |  , ;  /  /  ,.  | |  | '.'||   | |--'",
        "    '---'    ---'  ;  :   .'   \;  :    ;|   |/",
        "                   |  ,     .-./|  ,   / '---'",
        "                    `--`---'     ---`-'       "
    ]
    for i, line in enumerate(title):
        stdscr.addstr(start_y + i, start_x, line)

    # version = "v0.0.1"
    # stdscr.addstr(start_y + len(title), start_x + len(title[0]) - len(version), version)


def draw_menu(stdscr, selected_row_idx, start_y, start_x):
    menu_items = ['Continue', 'New Game', 'Settings', 'Quit']
    menu_width = 20
    for idx, item in enumerate(menu_items):
        x = start_x + (menu_width - len(item)) // 2
        y = start_y + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, item)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, item)

    # Draw menu border
    stdscr.box()
    stdscr.addch(start_y - 1, start_x - 1, curses.ACS_ULCORNER)
    stdscr.addch(start_y - 1, start_x + 20, curses.ACS_URCORNER)
    stdscr.addch(start_y + 4, start_x - 1, curses.ACS_LLCORNER)
    stdscr.addch(start_y + 4, start_x + 20, curses.ACS_LRCORNER)
    for i in range(4):
        stdscr.addch(start_y + i, start_x - 1, curses.ACS_VLINE)
        stdscr.addch(start_y + i, start_x + 20, curses.ACS_VLINE)
    for i in range(menu_width):
        stdscr.addch(start_y - 1, start_x + i, curses.ACS_HLINE)
        stdscr.addch(start_y + 4, start_x + i, curses.ACS_HLINE)

    # draw_road(stdscr, start_y + len(menu_items), start_x, menu_width)


def draw_road(stdscr, y, x, menu_width):
    height, width = stdscr.getmaxyx()
    line_length = int(width * 0.4)

    road_start_x = x - (line_length - menu_width) // 2
    road_end_x = road_start_x + line_length

    for i in range(3):
        stdscr.addch(y + i, road_start_x + i, '\\')

    for i in range(3):
        stdscr.addch(y + i, road_end_x - i - 1, '/')


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    selected_row_idx = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        title_start_y = height // 10
        title_start_x = (width - 50) // 2  # 96 is the width of the title ASCII art

        # menu_start_y = title_start_y + 10
        menu_start_y = int(height // 1.3)
        menu_start_x = (width - 20) // 2

        draw_title(stdscr, title_start_y, title_start_x)
        # draw_title(stdscr, 5, 5)
        draw_menu(stdscr, selected_row_idx, menu_start_y, menu_start_x)

        key = stdscr.getch()

        if key == curses.KEY_UP and selected_row_idx > 0:
            selected_row_idx -= 1
        elif key == curses.KEY_DOWN and selected_row_idx < 3:
            selected_row_idx += 1
        elif key == 10:  # Enter key
            if selected_row_idx == 2:
                game_over()
                break
            elif selected_row_idx == 3:  # Quit option
                break
            # Here you would typically handle other menu options

        stdscr.refresh()


curses.wrapper(main)
