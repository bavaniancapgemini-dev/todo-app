from plyer import notification
from playsound import playsound
from datetime import datetime


def show_notification(title, message):

    try:

        notification.notify(

            title=title,
            message=message,
            timeout=5

        )

        playsound("alert.mp3")

    except:

        pass


def check_due_tasks(tasks):

    today = datetime.now().strftime("%Y-%m-%d")

    for task in tasks:

        task_name = task[2]
        status = task[3]
        priority = task[4]
        due = task[7]

        # OVERDUE
        if due < today and status != "Completed":

            show_notification(

                "⚠ OVERDUE TASK",

                f"{task_name} is overdue!"

            )

        # DUE TODAY
        elif due == today and status != "Completed":

            show_notification(

                "⏰ TASK DUE TODAY",

                f"{task_name} is due today"

            )

        # HIGH PRIORITY
        if priority == "High" and status != "Completed":

            show_notification(

                "🔥 HIGH PRIORITY TASK",

                f"{task_name} requires attention"

            )