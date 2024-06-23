import sqlite3
import re
class ValueParser:
    @staticmethod
    def parse_value(value):
        # Regular expression to match the number and unit
        match = re.match(r"([0-9\.]+)([a-zA-Z%]*)", value)
        if match:
            number = float(match.group(1))
            unit = match.group(2)
            return number, unit
        else:
            return None, None

    @staticmethod
    def get_number(value):
        number, _ = ValueParser.parse_value(value)
        return number

    @staticmethod
    def get_unit(value):
        _, unit = ValueParser.parse_value(value)
        return unit

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

    def insert_data(self, id_name="id", type="label", padding="1111", x="10mm", y="10mm", width="20mm", height="10mm", class_="styleClass", extra_css=''):
        id_name = self.generate_unique_id_name(id_name)
        self.cursor.execute('''
            INSERT INTO Data (id_name, type, padding, x, y, width, height, class, extra_css)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id_name, type, padding, x, y, width, height, class_, extra_css))
        self.connection.commit()
        print(f"Inserted data with id_name: {id_name}")
        return id_name
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
    def update_data(self, id_name, type=None, padding=None, x=None, y=None, width=None, height=None, class_=None, extra_css=None):
        update_query = 'UPDATE Data SET'
        update_values = []

        if type is not None:
            update_query += ' type=?,'
            update_values.append(type)
        if padding is not None:
            update_query += ' padding=?,'
            update_values.append(padding)
        if x is not None:
            update_query += ' x=?,'
            update_values.append(x)
        if y is not None:
            update_query += ' y=?,'
            update_values.append(y)
        if width is not None:
            update_query += ' width=?,'
            update_values.append(width)
        if height is not None:
            update_query += ' height=?,'
            update_values.append(height)
        if class_ is not None:
            update_query += ' class=?,'
            update_values.append(class_)
        if extra_css is not None:
            update_query += ' extra_css=?,'
            update_values.append(extra_css)

        # Remove the last comma and add the WHERE clause
        update_query = update_query.rstrip(',') + ' WHERE id_name=?'
        update_values.append(id_name)

        self.cursor.execute(update_query, update_values)
        self.connection.commit()
        print(f"Updated data with id_name: {id_name}")

    def find_one_data(self, id_name, field):
        self.cursor.execute(f'''
            SELECT {field} FROM Data WHERE id_name=?
        ''', (id_name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]  # Return the value of the specified field
        else:
            return None  # Return None if no matching record found


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
