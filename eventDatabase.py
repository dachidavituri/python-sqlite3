import sqlite3
from event import Event


class EventDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY,
        category text,
        date text,
        start_time text,
        location text,
        age_restrict real
        )
        """)

    def add_event(self, event, id):
        self.cursor.execute("""
        INSERT INTO events VALUES (?, ?, ?, ?, ?, ?)""",
                            (id, event.category, event.date, event.start_time, event.location, event.age_restrict))
        self.conn.commit()

    def update_event(self, event, id):
        self.cursor.execute("""
        UPDATE events SET category = ?, date = ?, start_time = ?, location = ?, age_restrict = ? WHERE id = ?
        """, (event.category, event.date, event.start_time, event.location, event.age_restrict, id))
        self.conn.commit()

    def get_one_event(self, event_id):
        self.cursor.execute("""
        SELECT * FROM events WHERE id = ?
        """, (event_id,))
        row = self.cursor.fetchone()
        if row:
            return row
        else:
            return None

    def delete_event(self, event_id):
        self.cursor.execute("""
        DELETE FROM events WHERE id = ?
        """, (event_id,))
        self.conn.commit()

    def get_events(self, time):
        self.cursor.execute("""
        SELECT * FROM events WHERE start_time = ?
        """, (time,))
        result = self.cursor.fetchall()
        for row in result:
            print(row)
