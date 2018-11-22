import json
import sys

from rx import Observable


def read_events():
    return Observable.create(read_from_stdin)


def read_from_stdin(observer):
    for line in sys.stdin:
        data = json.loads(line)
        observer.on_next(data)
