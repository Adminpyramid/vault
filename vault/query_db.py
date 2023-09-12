import psycopg2


def execute_database_query(host, port, database, user, password, query):
    try:
        # Create a database connection
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )

        # Create a cursor
        cursor = connection.cursor()

        # Execute the query
        cursor.execute(query)

        # Fetch all the rows from the result
        rows = cursor.fetchall()

        # Get the column names from the cursor.description
        column_names = [desc[0] for desc in cursor.description]

        # Close the cursor and database connection
        cursor.close()
        connection.close()

        # Create a table of values
        table = []
        table.append(column_names)
        table.extend(rows)

        return table

    except Exception as e:
        return str(e)
