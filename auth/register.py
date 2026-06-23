import bcrypt
from database_utils.db import get_connection


def register_user(username, password):

    conn = get_connection()

    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    try:

        cursor.execute(
            """
            INSERT INTO users(username,password)
            VALUES (?,?)
            """,
            (
                username,
                hashed_password.decode("utf-8")
            )
        )

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()