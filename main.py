if __name__ == "__main__":
    from interface import interface
    from menu import Menu, Item
    from config import main_menu_items

    menu = Menu(interface)
    menu.title = "Cam's Python Curses Test"
    menu.footer = "https://github.com/camratchford/python_curses_test/"
    menu.load_items()
    interface.add_menu(menu)
    item_list = [Item.create_item(item) for item in main_menu_items]
    interface.menu.items_list = item_list
    event_loop = interface.event_loop
    event_loop()


