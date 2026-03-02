"""
1.1 Create Your Own Class
DailyLog (practical second-brain style)
"""

#ok im am 8 shots deep and felt let coding lets do this!!
#ok got the basic info done lets get the basic infor imput done
#ok lets do the fancy display now
#ok lets do a use case now
#and done and ready to submit!

from datetime import date


class DailyLog:
    def __init__(self, log_date=None):
        self.log_date = log_date if log_date else date.today().isoformat()
        self.wins = []
        self.tasks_todo = []
        self.tasks_done = []
        self.mood = None
        self.notes = ""

    # ---basic info---

    def add_win(self, win):
        self.wins.append(win)

    def add_task(self, task):
        self.tasks_todo.append(task)

    def complete_task(self, task):
        if task in self.tasks_todo:
            self.tasks_todo.remove(task)
            self.tasks_done.append(task)
        else:
            print("have not done it.")

    def set_mood(self, mood):
        self.mood = mood

    def add_notes(self, notes):
        if self.notes:
            self.notes += "\n" + notes
        else:
            self.notes = notes

    # ---fancy display (might change later)---

    def summary(self):
        print("\n===== DAILY =====")
        print(f"Date: {self.log_date}")
        print(f"Mood: {self.mood if self.mood else 'Not set'}")

        print("\nWins:")
        if self.wins:
            for w in self.wins:
                print(f"  - {w}")
        else:
            print("  (none yet)")

        print("\nTasks To-Do:")
        if self.tasks_todo:
            for t in self.tasks_todo:
                print(f"  - {t}")
        else:
            print("  (none)")

        print("\nTasks Done:")
        if self.tasks_done:
            for d in self.tasks_done:
                print(f"  - {d}")
        else:
            print("  (none yet)")

        print("\nNotes:")
        print(self.notes if self.notes else "(none)")

        print("=====================\n")


# ---use case---
log = DailyLog()

log.set_mood("Focused")

log.add_win("Got my assignment started early")
log.add_task("Finish DailyLog class")
log.add_task("Push code to GitHub")
log.complete_task("Finish DailyLog class")

log.add_notes("Keep it simple, but make it expandable for later assignments.")

log.summary()