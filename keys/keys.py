

class Keys(object):
    def __init__(self):

        self.key_pressed = ""
        # Map curses.KEY_UP -> "UP" for easier transmission

    def map_key(self, key):
        import curses
        from curses import ascii
        if key:
            key_pressed = ""
            if key == curses.KEY_UP:
                key_pressed = "UP"

            if key == curses.KEY_DOWN:
                key_pressed = "DOWN"

            if key == curses.KEY_LEFT:
                key_pressed = "LEFT"

            if key == curses.KEY_RIGHT:
                key_pressed = "RIGHT"

            if key == curses.KEY_PPAGE:
                key_pressed = "PGUP"

            if key == curses.KEY_NPAGE:
                key_pressed = "PGDN"

            if key == curses.KEY_HOME:
                key_pressed = "HOME"

            if key == curses.KEY_END:
                key_pressed = "END"

            if key == ascii.NL:
                key_pressed = "ENTER"

            if key == ascii.SP:
                key_pressed = "SPACE"

            self.key_pressed = key_pressed
            return key_pressed


class Cursor(object):
    def __init__(self):
        self.cursor_pos = (0, 0)
        self.highlighted_pos = ((0, 0), (0, 0))
        self.prev_cursor_pos = (0, 0)
        self.prev_highlighted_pos = ((0, 0), (0, 0))

    def select_item(self, item_pos, item_length):
        self.prev_cursor_pos, self.prev_highlighted_pos = self.cursor_pos, self.highlighted_pos

        start_x = item_pos[0]
        start_y = item_pos[1]
        end_x = item_pos[0] + item_length
        end_y = item_pos[1]
        self.cursor_pos = item_pos
        self.highlighted_pos = ((start_x, start_y), (end_x, end_y))

    def move_cur(self, pos):
        self.prev_cursor_pos = self.cursor_pos
        self.cursor_pos = pos

