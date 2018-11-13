class BalanceCalculatorBySubjectType:

    def __init__(self, subject_type):
        self.subject_type = subject_type
        self.users = []
        self.accounts = {}

    def process(self, event):
        if self._is_user_registration_event(event):
            self._register_user(event)

        if self._is_contract_account_event(event):
            self._register_contract(event)

        if not self._belongs_to_me(event):
            return

        self._accumulate_balance(event)

    def get_summary(self):
        return sum([value for key, value in self.accounts.items()])

    def reset(self):
        pass

    def _is_user_registration_event(self, event):
        return event["eventType"] == "registerUser" and event["type"] == self.subject_type

    def _register_user(self, event):
        self.users.append(event["user"])

    def _belongs_to_me(self, event):
        return "user" in event and event["user"] in self.users or "iban" in event and event["iban"] in self.accounts

    def _is_contract_account_event(self, event):
        return event["eventType"] == "contractCurrentAccount" and event["user"] in self.users

    def _register_contract(self, event):
        self.accounts[event["iban"]] = 0

    def _accumulate_balance(self, event):
        if "balance" not in event or "iban" not in event:
            return

        self.accounts[event["iban"]] = event["balance"]["value"]
