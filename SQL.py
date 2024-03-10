import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()
cursor.execute('''create table fio(Fam text, Im text, Otch text)''')
cursor.execute("""INSERT INTO fio(Fam, Im, Otch)  values (?,?,?)""", [input('Фамилия: '), input('Имя: '), input('Отчество: ')])
cursor.execute("""INSERT INTO fio(Fam, Im, Otch)  values (?,?,?)""", [input('Фамилия: '), input('Имя: '), input('Отчество: ')])
cursor.execute("""INSERT INTO fio(Fam, Im, Otch)  values (?,?,?)""", [input('Фамилия: '), input('Имя: '), input('Отчество: ')])
conn.commit()
cursor.close()
