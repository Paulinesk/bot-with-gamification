import sqlite3

conn = sqlite3.connect('levelupbot.db')
conn.execute('PRAGMA journal_mode=WAL;')
conn.commit()
conn.close()

print("WAL режим успешно включён ✅")
