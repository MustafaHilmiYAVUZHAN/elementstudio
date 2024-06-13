import sqlite3

class DM:
    def __init__(self, file_name):
        self.file_name = file_name
        self.connect()

    def connect(self):
        self.connection = sqlite3.connect(self.file_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Data(
                number INTEGER PRIMARY KEY,
                id_name TEXT UNIQUE,
                type TEXT,
                padding INTEGER,
                x TEXT,
                y TEXT,
                width TEXT,
                height TEXT,
                class TEXT,
                extra_css TEXT
            )
        ''')
        self.connection.commit()

    def generate_unique_id_name(self, id_name):
        original_id_name = id_name
        count = 1
        while True:
            self.cursor.execute('''
                SELECT COUNT(*) FROM Data WHERE id_name=?
            ''', (id_name,))
            if self.cursor.fetchone()[0] == 0:
                break
            id_name = f"{original_id_name}{count:03}"
            count += 1
        return id_name

    def insert_data(self, id_name, type, padding, x, y, width, height, class_, extra_css=''):
        id_name = self.generate_unique_id_name(id_name)
        self.cursor.execute('''
            INSERT INTO Data (id_name, type, padding, x, y, width, height, class, extra_css)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id_name, type, padding, x, y, width, height, class_, extra_css))
        self.connection.commit()
        print(f"Inserted data with id_name: {id_name}")

    def delete_data(self, id_name):
        self.cursor.execute('''
            DELETE FROM Data WHERE id_name=?
        ''', (id_name,))
        self.connection.commit()

    def find_data(self, id_name):
        self.cursor.execute('''
            SELECT * FROM Data WHERE id_name=?
        ''', (id_name,))
        return self.cursor.fetchone()
    def get_all_ids(self):
        self.cursor.execute('''
            SELECT id_name FROM Data
        ''')
        return [row[0] for row in self.cursor.fetchall()]
    def close_connection(self):
        self.connection.close()



# Usage example
if __name__ == "__main__":
    db_manager = DM('example_database.db')
    db_manager.create_table()

    # Attempt to insert data
    db_manager.insert_data('button', 'BTN', 3120, '20', '30', '120', '220', 'example_class_3', 'text-align: center;')
    db_manager.insert_data('button', 'BTN', 3120, '20', '30', '120', '220', 'example_class_3', 'text-align: center;')
    # Find data
    data = db_manager.find_data('button')
    # Delete data
    db_manager.delete_data('button')

    db_manager.close_connection()
