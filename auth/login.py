import bcrypt
from database_utils.db import get_connection


def login_user(username, password):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT password
        FROM users
        WHERE username=?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        return bcrypt.checkpw(
            password.encode("utf-8"),
            user[0].encode("utf-8")
        )

    return False