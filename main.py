from ToDoList import DBHelper
import argparse
from datetime import datetime

def main():
    db = DBHelper()

    parser = argparse.ArgumentParser(description="TODO List Manager")
    parser.add_argument('--create', help="Create a new task with title")
    parser.add_argument('--edit', nargs=3, help="Edit task title and task status. Provide task ID , new title and new status")
    parser.add_argument('--mark-complete', help="Mark a task as complete. Provide task ID")
    parser.add_argument('--delete', help="Delete a task. Provide task ID")
    parser.add_argument('--list', choices=['all', 'incomplete', 'complete'], help="List tasks")
    parser.add_argument('--search', help="Search tasks by title")
    args = parser.parse_args()

    try:
        if args.create:
            db.insert_task(args.create,"incomplete")
        elif args.edit:
            task_id, new_title, new_status = args.edit
            db.edit_data(task_id, new_title, new_status)
        elif args.mark_complete:
            db.mark_complete(args.mark_complete)
        elif args.delete:
            db.delete_data(args.delete)
        elif args.list:
            if args.list == 'all':
                db.show_data()
            else:
                db.show_data(args.list)
        elif args.search:
            db.search_by_title(args.search)
        else:
            parser.print_help()
    except Exception as e:
        print(e)
        print("Invalid details! Please try again")


if __name__ == "__main__":
    main()
