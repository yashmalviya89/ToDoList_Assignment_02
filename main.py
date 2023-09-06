# Import necessary modules and classes
from ToDoList import DBHelper 
import argparse  
from datetime import datetime 

def main():
    db = DBHelper()

    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description="TODO List Manager")

    # Define command-line arguments and their descriptions
    parser.add_argument('--create', help="Create a new task with title")
    parser.add_argument('--edit', nargs=3, help="Edit task title and task status. Provide task ID, new title, and new status")
    parser.add_argument('--mark-complete', help="Mark a task as complete. Provide task ID")
    parser.add_argument('--delete', help="Delete a task. Provide task ID")
    parser.add_argument('--list', choices=['all', 'incomplete', 'complete'], help="List tasks")
    parser.add_argument('--search', help="Search tasks by title")
    args = parser.parse_args()

    try:
        # Check the provided command-line arguments and execute the corresponding actions
        if args.create:
            # Create a new task with the provided title and default status 'incomplete'
            db.insert_task(args.create, "incomplete")
        elif args.edit:
            # Edit a task by providing task ID, new title, and new status
            task_id, new_title, new_status = args.edit
            db.edit_data(task_id, new_title, new_status)
        elif args.mark_complete:
            # Mark a task as complete by providing the task ID
            db.mark_complete(args.mark_complete)
        elif args.delete:
            # Delete a task by providing the task ID
            db.delete_data(args.delete)
        elif args.list:
            if args.list == 'all':
                # List all tasks
                db.show_data()
            else:
                # List tasks based on the specified status (incomplete or complete)
                db.show_data(args.list)
        elif args.search:
            # Search for tasks by title
            db.search_by_title(args.search)
        else:
            # Display help message if no valid arguments are provided
            parser.print_help()
    except Exception as e:
        print(e)
        print("Invalid details! Please try again")


if __name__ == "__main__":
    main()  
