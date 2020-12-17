import sqlite3 
# from flask_login import UserMixin

# class User():
#     def __init__(self, name, password):
#         self._name = name 
#         self._password = password


def create_table():
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """
            CREATE TABLE IF NOT EXISTS team (
                id integer PRIMARY KEY,
                name text NOT NULL,
                public text,
                tags text NOT NULL
            )
        """
    )

    c.execute(
        """
            CREATE TABLE IF NOT EXISTS students (
                id integer PRIMARY KEY,
                name text NOT NULL,
                public text,
                tags text,
                password text NOT NULL,
                teamid integer,
                FOREIGN KEY (teamid) REFERENCES team(id)
            )
        """
    )
    conn.commit()
    conn.close()

def get_user_password(user_name):
    conn = sqlite3.connect('./example.db')
    password = None 
    c = conn.cursor() 
    c.execute(
        """
            SELECT password FROM students WHERE name = ?
        """, (user_name,)
    )
    password = c.fetchone()
    conn.close()
    return password[0]

def delete_team(name):
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    try:
        c.execute(
            """
                DELETE FROM team where name = ?
            """, (name,)
        )
    except Exception:
        pass
    conn.commit()
    conn.close()


def add_team(teamid, name):
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    try:
        c.execute(
            """
                update students set teamid = ? where name = ? 
            """, (teamid, name,)
        )
    except Exception:
        pass
    conn.commit()
    conn.close()

def leave_team(name):
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    try:
        c.execute(
            """
                update students set teamid = -1 where name = ? 
            """, (name,)
        )
    except Exception:
        pass
    conn.commit()
    conn.close()

def insert_new_team(name, public, tags):
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """
            INSERT INTO team ('name', 'public', 'tags') VALUES (?, ?, ?)
        """, (name, public, tags)
    )
    conn.commit()
    conn.close()

def insert_team_tag(name, new_tag):
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """
            SELECT tags from team where name = ?
        """, (name,)
    )
    result = c.fetchone()
    tag_col = result[-1]
    if tag_col.endsWith("/"):
        new_tag = tag_col + new_tag
    else:
        new_tag = tag_col + "/" + new_tag
    c.execute(
        """
            update team set tags = ? where name = ? 
        """, (new_tag, name,)
    )
    conn.commit()
    conn.close()
    

def filter_tag(tag):
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """ SELECT * from team"""
    )
    res = c.fetchall()
    result = [t for t in res if t[-1].find(tag) != -1]
    conn.commit()
    conn.close()
    return result

def filter_name(name):
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """ SELECT * from team where team.name=?""", (name,)
    )
    res = c.fetchall()
    conn.commit()
    conn.close()
    return res

def filter_by_me(name):
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """
        SELECT team.id, team.name, team.public, team.tags from team, students where team.id = students.teamid and students.name = ?
        """, (name,)
    )
    res = c.fetchall()
    conn.commit()
    conn.close()
    return res

def select_all_team():
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """
            SELECT * FROM team
        """
    )
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

def select_all_team_students():
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """
            SELECT team.id, team.name, students.id, students.name FROM team, students WHERE team.id = students.teamid
        """
    )
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result


def add_new_user(name, public, tags, password, teamid):
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """
            insert into students (name, public, tags, password, teamid) values (?, ?, ?, ?, ?)
        """, (
            name, public, tags, password, teamid
        )
    )
    conn.commit()
    conn.close()

def select_all_user():
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """
            SELECT name FROM students
        """
    )
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

def select_all_user_info():
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """
            SELECT * FROM students
        """
    )
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

def modify_student(sid, tag):
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """
            update students set tags = ? where name = ? 
        """, (tag, sid,)

    )
    conn.commit()
    conn.close()
def modify_team(tid, tag):
    conn = sqlite3.connect('./example.db')
    c = conn.cursor()
    c.execute(
        """
            update team set tags = ? where id = ? 
        """, (tag, tid)
    )
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
    insert_new_team("hello", 'yes', "fuck")
    add_new_user("Sam", "yes", "genius", "admin", 1)
    print(select_all_team())
    print(select_all_user())
    print(select_all_user_info())
    print(select_all_team_students())

