import curses


class Menu(object):
    def __init__(self, interface):

        self.screen = interface.stdscr
        self.window_style = self.MenuStyle()
        self.window = self.MenuWindowMain(self.window_style).window # Just the initial value, will be changed when context changes
        self.height = 0
        self.width = 0
        self.output = False
        self.output_line_y = 0
        self.title = ""
        self.footer = ""
        self.items_list = []
        self.window_rows = []
        self.previous_item_index = 0
        self.selected_item_index = 0
        self.set_window_dimensions()

    def set_window_dimensions(self):
        self.height, self.width = self.screen.getmaxyx()

    def load_items(self):
        item_spacing = self.window_style.item_group_x_spacing
        rows = {k: [] for k in range(self.height)}
        item_list = []
        for item in self.items_list:
            rows[item.y].append(item)

        for k in rows.keys():
            v = rows[k]

            for i, item in enumerate(v):
                if i != 0:
                    # Any item but the first item in the list, as that one should keep its original x position
                    # X pos is equal to the previous item's last character x position plus the item spacing
                    item.start_x = item_list[i-1].x_coords[-1] + item_spacing
                    item.get_x_coords()
                item_list.append(item)

        self.window_rows = item_list

    def draw_window(self):

        if self.output:
            self.draw_output()
        else:
            self.screen.erase()

        self.load_items()

        padding_top = self.window_style.padding_top
        padding_left = self.window_style.padding_left

        # Draw Title
        self.screen.attron(curses.color_pair(4))
        self.screen.addstr(padding_top - 2, padding_left + 2, self.title)
        self.screen.attroff(curses.color_pair(4))

        self.set_window_dimensions()
        y_start = 0

        # Get longest title
        comment_start = max([len(i) for i in self.window_rows])

        for item in self.window_rows:

            y_start = item.y + padding_top
            x_start = item.start_x + padding_left

            if item.line_num:
                self.screen.attron(curses.color_pair(3))
                self.screen.addstr(y_start, x_start, f"{item.line_num}.")
                self.screen.attroff(curses.color_pair(3))
                x_start += x_start + 2

            if item.title:
                self.screen.attron(curses.color_pair(item.color_pair))
                self.screen.addstr(y_start, x_start, item.title)
                self.screen.attroff(curses.color_pair(item.color_pair))
                x_start += comment_start + 2

            if item.description:
                self.screen.attron(curses.color_pair(3))
                self.screen.addstr(y_start, x_start, f"- {item.description}")
                self.screen.attroff(curses.color_pair(3))

        self.output_line_y = y_start + 2

        # Draw Footer
        self.screen.attron(curses.color_pair(4))
        self.screen.addstr(y_start + 4, padding_left + 2, self.footer)
        self.screen.attroff(curses.color_pair(4))

        self.screen.refresh()

    def draw_selection(self):
        self.screen.erase()

        # Set newly selected item's color to 2
        self.window_rows[self.selected_item_index].color_pair = 2
        selected_item = self.window_rows[self.selected_item_index]
        y = selected_item.y
        x = selected_item.x_coords[0]
        self.screen.attron(curses.color_pair(selected_item.color_pair))
        self.screen.addstr(y, x, selected_item.title)
        self.screen.attroff(curses.color_pair(selected_item.color_pair))

        # Set previously selected item's color to it's default
        self.window_rows[self.previous_item_index].color_pair = self.window_rows[self.previous_item_index].initial_color_pair
        previously_selected_item = self.window_rows[self.previous_item_index]
        y = previously_selected_item.y
        x = previously_selected_item.x_coords[0]

        self.screen.attron(curses.color_pair(previously_selected_item.initial_color_pair))
        self.screen.addstr(y, x, previously_selected_item.title)
        self.screen.attroff(curses.color_pair(previously_selected_item.initial_color_pair))
        self.screen.refresh()

    def draw_output(self):

        selected_item = self.window_rows[self.selected_item_index]
        y = self.output_line_y
        x = self.window_style.padding_left
        self.screen.attron(curses.color_pair(5))
        self.screen.addstr(y, x, selected_item.argument)
        self.screen.attroff(curses.color_pair(5))

        self.screen.refresh()
        # self.output = False



    class MenuStyle(object):
        def __init__(self):
            self.padding_left = 3
            self.padding_top = 3
            self.item_group_x_spacing = 5 # When items are on the same row
            self.row_spacing = 1 # Space between rows
            curses.start_color()
            # Default
            curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
            # Selected
            curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
            # Success
            curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
            # Caution
            curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            # Danger / Error
            curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)

    class MenuStyleDefault(MenuStyle):
        def __init__(self):
            super().__init__()

    class MenuWindow(object):
        def __init__(self, h, w, y, x, style):
            from curses import newwin
            self.height = h
            self.width = w
            self.begin_y = y
            self.begin_x = x
            self.style = style
            self.window = newwin(self.height, self.width, self.begin_y, self.begin_x)



    class MenuWindowMain(MenuWindow):
        def __init__(self, style):
            self.height = 60
            self.width = 80
            self.begin_y = 2
            self.begin_x = 2
            self.style = style
            super().__init__(self.height, self.width, self.begin_y, self.begin_x, self.style)