class Task:
    class Task:
        def __init__(self, name, description, due_date, urgency=None):
            self.name = name
            self.description = description
            self.due_date = due_date
            self.urgency = urgency
            self.completed = False

        def mark_as_complete(self):
            self.completed = True

        def edit_task(self, name=None, description=None, due_date=None):
            if name is not None:
                self.name = name
            if description is not None:
                self.description = description
            if due_date is not None:
                self.due_date = due_date

        def set_urgency(self, urgency):
            self.urgency = urgency


