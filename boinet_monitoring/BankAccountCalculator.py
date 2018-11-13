class BankAccountCalculator:

    def __init__(self):
        self.accounts = {"bankTreasuryAccount": 0}

    def process(self, event):
        if not self._belongs_to_me(event):
            return

        self._accumulate_balance(event)

    def get_summary(self):
        return sum([value for key, value in self.accounts.items()])

    def _belongs_to_me(self, event):
        return "iban" in event and event["iban"] in self.accounts

    def _accumulate_balance(self, event):
        if "balance" not in event or "iban" not in event:
            return

        self.accounts[event["iban"]] = event["balance"]["value"]