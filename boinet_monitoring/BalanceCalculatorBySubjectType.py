class BalanceCalculatorBySubjectType:

    def __init__(self, subject_type):
        self.subject_type = subject_type
        self.balance = 0

    def process(self, event):
        if "eventType" not in event or event["eventType"] != "bankBalance":
            return

        self._update_balance(event)

    def get_balance(self):
        return self.balance

    def _update_balance(self, event):
        self.balance = event[self.subject_type]
