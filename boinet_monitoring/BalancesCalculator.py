from boinet_monitoring.BalanceCalculatorBySubjectType import BalanceCalculatorBySubjectType
from boinet_monitoring.BankAccountCalculator import BankAccountCalculator
from boinet_monitoring import terminal_printer


class BalancesCalculator:

    def __init__(self):
        self.tick = 0
        self.financial_events_processors = [BalanceCalculatorBySubjectType(subject_type)
                                            for subject_type
                                            in self.SUBJECT_TYPES] + [BankAccountCalculator()]
        header_row = ["Tick"] + self.SUBJECT_TYPES + ["Bank", "Total balance"]
        terminal_printer.print_summary(header_row)

    def accumulate(self, event):
        if "eventType" not in event:
            self.tick = event["tick"]

        return event, self._process_financial_event(event)

    def _process_financial_event(self, event):
        for processor in self.financial_events_processors:
            processor.process(event)
        return [self.tick] + self._balances_by_subject_type() + [self._total_balance()]

    def _total_balance(self):
        return sum([processor.get_summary() for processor in self.financial_events_processors])

    def _balances_by_subject_type(self):
        return [processor.get_summary() for processor in self.financial_events_processors]

    SUBJECT_TYPES = ["PERSON", "COMPANY"]
