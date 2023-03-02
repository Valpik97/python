import sqlite3


try:
    conn = sqlite3.connect(r"C:\Users\111040.ITIP\Downloads\Chinook_Sqlite_AutoIncrementPKs.sqlite")
except sqlite3.Error:
    print("cannot connect")
    exit(-1)

c = conn.cursor()
c.execute("CREATE TABLE Users(UserId Integer, Username CHARACTER(29))")
c.execute('INSERT INTO Users VALUES(0, "name")')
# print(c.execute("SELECT * FROM Users").fetchall())
# print(c.execute("SELECT * FROM Employee").fetchall())
# print(c.execute("SELECT * FROM Employee").fetchone())
# print(c.execute("SELECT * FROM Employee").fetchmany(2))
# c.execute("DROP TABLE Employee").fetchall()
conn.commit()
