'''h'''
def main():
    """M"""
    menu = []
    while True:
        order = input().strip()
        if order == "DONE":
            break
        if order == "SOMETHING'S WRONG":
            menu = []
        elif order == "CLOSED":
            menu.clear()
            break
        elif "Can't do:" in order:
            item = order.split(": ")[1]
            menu.remove(item)
        else:
            item, position = order.split(" #")
            if position == "N":
                menu.append(item)
            else:
                menu.insert(int(position) - 1, item)
    print(f"Full Course: {menu} Reversed: {menu[::-1]}")
main()
