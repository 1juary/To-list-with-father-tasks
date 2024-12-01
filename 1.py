import sqlite3

# 创建或连接到数据库
connection = sqlite3.connect('example.db')

# 创建一个游标对象
cursor = connection.cursor()

# 创建表
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    completed BOOLEAN DEFAULT 0
)
''')

# 插入数据
cursor.execute('''
INSERT INTO Tasks (task_name, completed) VALUES (?, ?)
''', ('Learn SQLite', 0))

# 提交事务
connection.commit()

# 查询数据
cursor.execute('SELECT * FROM Tasks')
tasks = cursor.fetchall()

# 打印查询结果
for task in tasks:
    print(task)

# 关闭连接
connection.close()