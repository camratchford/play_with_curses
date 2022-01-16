import curses

class Interface(object):
    def __init__(self):

        from keys import Keys, Cursor
        self.config = ""
        self.escaped = False
        self.keys = Keys()
        self.key_pressed = None
        self.cursor = Cursor()
        self.stdscr = curses.initscr()
        self.stdscr.clear()
        curses.noecho()
        self.stdscr.keypad(True)
        self.menu = None
        self.key_map = None
        self.function_map = None

    def generate_function_map(self):
        self.function_map = {
            "output_text": self.menu.draw_output
        }

    def add_menu(self, menu):
        self.menu = menu
        self.generate_function_map()

    def select_item(self):
        self.menu.output = False
        index_max = len(self.menu.window_rows) - 1
        direction = self.key_pressed

        if direction == "DOWN" or direction == "RIGHT":
            new_index = 0
            self.menu.previous_item_index = self.menu.selected_item_index
            if self.menu.selected_item_index + 1 <= index_max:
                new_index = self.menu.selected_item_index + 1
            self.menu.selected_item_index = new_index
            self.menu.draw_selection()

        if direction == "UP" or direction == "LEFT":
            new_index = index_max
            self.menu.previous_item_index = self.menu.selected_item_index
            if self.menu.selected_item_index - 1 >= 0:
                new_index = self.menu.selected_item_index - 1
            self.menu.selected_item_index = new_index
            self.menu.draw_selection()

        if direction == "ENTER":
            self.menu.output = True
            item = self.menu.window_rows[self.menu.selected_item_index]
            self.function_map[item.exec]()

    def listen_for_keys(self):

        key = self.stdscr.getch()
        self.key_pressed = self.keys.map_key(key)
        self.select_item()

    def event_loop(self):
        while not self.escaped:
            self.menu.draw_window()
            self.listen_for_keys()








