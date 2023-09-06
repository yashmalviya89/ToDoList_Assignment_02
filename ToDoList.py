import mysql.connector as connector
from datetime import datetime

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='Jordan@yash6989',
                                     database='pythontodolist')

        query = "create table if not exists todolist(taskId int primary key auto_increment,taskTitle varchar(200),createdAt datetime,completedAt datetime,status varchar(200) default 'incomplete')"
        cur = self.con.cursor()
        cur.execute(query)
        print("Table Created Successfully...")

    def insert_task(self, taskTitle, status):
        # Check if a task with the same title and incomplete status exists
        check_query = "select taskId from todolist where taskTitle = '{}' and status = '{}'".format(taskTitle, status)
        cur = self.con.cursor()
        cur.execute(check_query)
        existing_task = cur.fetchone()

        if existing_task:
            print("Task with the same title and incomplete status exists.")
            return

        # Insert the task
        insert_query = "insert into todolist(taskTitle, createdAt, status) values('{}', '{}', '{}')".format(taskTitle, str(datetime.now()), status)
        cur.execute(insert_query)
        self.con.commit()
        print("Task Inserted to DB")

    # Fetch all: Show data from the table
    def show_data(self, status=None):
        query = "select * from todolist"

        if status:
            if status == 'complete':
                query += " where status = 'complete'"
            elif status == 'incomplete':
                query += " where status = 'incomplete'"

        cur = self.con.cursor()
        cur.execute(query)

        for row in cur:
            print("taskId : ", row[0])
            print("taskTitle : ", row[1])
            print("createdAt : ", row[2])
            print("completedAt : ", row[3])
            print("status : ", row[4])
            print()

    def edit_data(self, taskId, newTitle, newStatus):
         # Check if a task with the same title and incomplete status exists
        check_query = "select taskId from todolist where taskTitle = '{}' and status = '{}'".format(newTitle, newStatus)
        cur = self.con.cursor()
        cur.execute(check_query)
        existing_task = cur.fetchone()
        if existing_task:
            print("Task with the same title and incomplete status exists.")
            return
        query = "update todolist set taskTitle = '{}', status = '{}', completedAt = '{}' where taskId = '{}'".format(newTitle, newStatus, str(datetime.now()), taskId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data Updated Successfully..")
        print(f"newTitle : {newTitle} and newStatus : {newStatus}")

    def mark_complete(self, taskId):
        check_query = "select * from todolist where taskId = '{}' and status = 'complete' and not exists(select 1 from todolist where taskId = '{}')".format(taskId,taskId)
        cur = self.con.cursor()
        cur.execute(check_query)
        existing_task_id = cur.fetchone()
        if existing_task_id:
            print("Task is not present or already completed...")
            return 
        query = "update todolist set status = 'complete', completedAt = '{}' where taskId = {}".format(str(datetime.now()), taskId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Task Marked as Complete.")

    def delete_data(self, taskId):
        query = "delete from todolist where taskId = '{}'".format(taskId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data deleted successfully...")

    def search_by_title(self, taskTitle):
        query = "select * from todolist where taskTitle like '%{}%'".format(taskTitle)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("taskId : ", row[0])
            print("taskTitle : ", row[1])
            print("createdAt : ", row[2])
            print("completedAt : ", row[3])
            print("status : ", row[4])
