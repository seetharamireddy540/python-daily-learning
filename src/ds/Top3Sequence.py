from collections import defaultdict, Counter
from typing import List, Tuple

class LogEntry:
    def __init__(self, timestamp, customer_id, page):
        self.timestamp = timestamp
        self.customer_id = customer_id
        self.page = page
