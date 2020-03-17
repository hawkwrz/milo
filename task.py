import datetime
import sys
from itertools import permutations

MIN_YEAR = 2000
MAX_YEAR = 2999


class DateChecker:
    year, month, day = 0, 0, 0
    dates = []

    def __init__(self, file_path):
        self.raw_data = file_path
        self._parse_file()
        self._permutations_dates()
        self.result()

    def _parse_file(self):
        with open(self.raw_data, 'r') as f:
            self.line = f.read()
            self.ideal_data = sorted(map(int, self.line.split('/')))

    def _permutations_dates(self):
        for date in [p for p in permutations(self.ideal_data) if 0 < p[1] < 13 if 0 < p[2] < 32]:
            if date[0] < MIN_YEAR:
                self.year = date[0] + MIN_YEAR
            else:
                self.year = date[0]
            self.month = date[1]
            self.day = date[2]
            if self._check_date():
                self.dates.append(self.earliest_date)
                break

    def _check_date(self):
        try:
            self.earliest_date = datetime.date(self.year, self.month, self.day)
            return True
        except ValueError:
            return False

    def result(self):
        if not self.dates:
            print(f"{self.line} is illegal")
        else:
            print(self.earliest_date)


if __name__ == '__main__':
    dc = DateChecker(sys.argv[1])
