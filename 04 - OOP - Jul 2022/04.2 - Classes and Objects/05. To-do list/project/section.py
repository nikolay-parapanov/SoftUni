from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        for section_task in self.tasks:
            if section_task.name == task.name:
                return f"Task is already in the section {self.name}"
        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        counter = 0
        for task in self.tasks:
            if task.completed:
                counter += 1
                self.tasks.remove(task)
        return f"Cleared {counter} tasks."

    def view_section(self):
        result = f'Section {self.name}:'
        for task in self.tasks:
            result += "\n" + task.details()
        return result
