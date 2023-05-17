from event import Event
from eventDatabase import EventDatabase

event_data = EventDatabase('event.db')
while True:
    print("You can choose various action to implement database")
    print("1: create")
    print("2: read")
    print("3: update")
    print("4: delete")
    print("0: exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        category = input("Enter category: ")
        date = input("Enter date: ")
        start_time = input("Enter start time: ")
        location = input("Enter location: ")
        age = int(input("Enter your age: "))
        age_restrict = int(input("Enter avaliable age: "))
        id = int(input("Enter id: "))
        event_data.add_event(Event(category, date, start_time, location, age_restrict), id)
    if choice == 2:
        choice1 = input("which do you want? read by id or read by start_time? ")
        if choice1 == "id":
            id = int(input("Enter id: "))
            print(event_data.get_one_event(id))
        elif choice1 == "start_time":
            start_time = input("enter start_time: ")
            event_data.get_events(start_time)
    if choice == 3:
        id = int(input("Enter id: "))
        category = input("Enter category: ")
        date = input("Enter date: ")
        start_time = input("Enter start time: ")
        location = input("Enter location: ")
        age = int(input("Enter avaliable age: "))
        event_data.update_event(Event(category, date, start_time, location, age), id)
    if choice == 4:
        id = int(input("Enter id: "))
        event_data.delete_event(id)
    if choice == 0:
        print('you have left this game')
        break
