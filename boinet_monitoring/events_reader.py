import json
import sys

from boinet_monitoring.BalancesCalculator import BalancesCalculator


def calculate_balances(_args):
    calculator = BalancesCalculator()
    for line in sys.stdin:
        data = json.loads(line)
        calculator.process_event(data)
