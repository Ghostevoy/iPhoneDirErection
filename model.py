import json

import text
import view

phone_book = {}
path = "phones.json"


def open_file():
    global phone_book
    try:
        with open(path, "r", encoding="UTF-8") as file:
            phone_book = json.load(file)
        return True
    except:
        return False


def save_file():
    try:
        with open(path, "w", encoding="UTF-8") as file:
            json.dump(phone_book, file, ensure_ascii=False)
        return True
    except:
        return False


def check_id():
    if phone_book:
        return max(list(map(int, phone_book)))+1
    else:
        return 1


def add_contact(new: {int:dict[str,str]}):
    contact = {check_id(): new}
    phone_book.update(contact)


def search(word: str) -> dict[int:dict[str, str]]:
    result = {}
    for index, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
    return result

def remove(index):
    name = phone_book.pop(str(index))
    return name.get('name')

def change(index, choice):

    match int(choice):
        case 1:
            phone_book[index]["name"] = view.search_word(text.new_contact["name"])
        case 2:
            phone_book[index]["phone"] = view.search_word(text.new_contact["phone"])
        case 3:
            phone_book[index]["comment"] = view.search_word(text.new_contact["comment"])
        case 4:
            view.print_message(text.the_end)
