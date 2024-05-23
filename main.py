from tkinter import Tk, Canvas
from datetime import date, datetime

def get_events():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1].strip(), '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events

def days_between_dates(d1, d2):
    return (d1 - d2).days

root = Tk()
root.title("Countdown App")

c = Canvas(root, width=800, height=800, bg='black')
c.pack()
c.create_text(100, 50, anchor='w', fill='orange', font='Arial 28 bold', text='Countdown')

events = get_events()
today = date.today()

y_position = 100
for e in events:
    event_name = e[0]
    days_until = days_between_dates(e[1], today)
    if days_until < 0:
        days_until *= -1
        display = f'It has been {days_until} days since {event_name}'
    else:
        display = f'It is {days_until} days until {event_name}'

    c.create_text(0, y_position, anchor='w', fill='lightblue', font='Arial 15 bold', text=display)
    y_position += 50  # Increment the y position for the next event

root.mainloop()
