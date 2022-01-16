

class Item(object):
    def __init__(self, y, start_x):
        # Row
        self.y = y
        # Which column to start writing content
        self.start_x = start_x
        self.line_num = 0
        self.title = ""
        self.description = ""
        self.len = len(self.title)
        self.x_coords = None
        self.color_pair = 1
        self.initial_color_pair = 1
        self.exec = None
        self.argument = ""
        self.get_x_coords()

    def __len__(self):
        return len(self.title)

    def absolute_coords(self):
        return [(self.y, x) for x in self.x_coords]

    def get_x_coords(self):
        self.x_coords = [i for i in range(self.start_x, self.start_x + len(self.title))]

    @staticmethod
    def create_item(item_dict):
        item = Item(0, 0)
        for attr in item_dict.keys():
            if hasattr(item, attr):
                setattr(item, attr, item_dict[attr])
        item.get_x_coords()
        item.initial_color_pair = item.color_pair
        return item

