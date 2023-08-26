import sqlite3

def create_tables(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Book (
                book_id INTEGER PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255),
                isbn VARCHAR(20),
                genre VARCHAR(50),
                publication_date DATE,
                price DECIMAL(10, 2)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Inventory (
                book_id INTEGER PRIMARY KEY,
                stock_count INTEGER,
                reorder_point INTEGER,
                low_stock_alert BOOLEAN,
                FOREIGN KEY (book_id) REFERENCES Book(book_id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customer (
                customer_id INTEGER PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255),
                phone VARCHAR(20),
                shipping_address VARCHAR(255),
                billing_address VARCHAR(255)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS `Order` (
                order_id INTEGER PRIMARY KEY,
                order_number VARCHAR(20),
                order_date DATETIME,
                customer_id INTEGER,
                total_amount DECIMAL(10, 2),
                order_status VARCHAR(20),
                FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS OrderLineItem (
                line_item_id INTEGER PRIMARY KEY,
                order_id INTEGER,
                book_id INTEGER,
                quantity INTEGER,
                unit_price DECIMAL(10, 2),
                subtotal DECIMAL(10, 2),
                FOREIGN KEY (order_id) REFERENCES `Order`(order_id),
                FOREIGN KEY (book_id) REFERENCES Book(book_id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Payment (
                payment_id INTEGER PRIMARY KEY,
                order_id INTEGER,
                payment_method VARCHAR(50),
                transaction_id VARCHAR(50),
                payment_amount DECIMAL(10, 2),
                payment_status VARCHAR(20),
                FOREIGN KEY (order_id) REFERENCES `Order`(order_id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                userId INTEGER PRIMARY KEY,
                userName VARCHAR(20),
                passWord VARCHAR(20),
                customer_id INTEGER,
                FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
            );
        ''')

        connection.commit()
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def main():
    db_path = 'book-rental.sqlite'

    try:
        connection = sqlite3.connect(db_path)
        create_tables(connection)
        print("SQLite database and tables created successfully.")
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
    finally:
        connection.close()

if __name__ == '__main__':
    main()
  