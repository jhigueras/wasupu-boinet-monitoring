from boinet_monitoring import terminal_printer
from boinet_monitoring.BalanceCalculatorBySubjectType import BalanceCalculatorBySubjectType


class BalancesCalculator:

    def __init__(self):
        self.tick = 0
        self.financial_events_processors = [BalanceCalculatorBySubjectType(subject_type)
                                            for subject_type
                                            in self.SUBJECT_TYPES]
        header_row = ["Tick"] + self.SUBJECT_TYPES + ["Total balance"]
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
        return sum([processor.get_balance() for processor in self.financial_events_processors])

    def _balances_by_subject_type(self):
        return [processor.get_balance() for processor in self.financial_events_processors]

    SUBJECT_TYPES = ["peopleBalance", "companiesBalance", "treasuryAccount"]
