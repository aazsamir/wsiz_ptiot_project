from datetime import datetime


class Result:
    def __init__(
            self,
            date: datetime,
            result: bool,
            name: str
    ):
        self._date = date
        self._result = result
        self._name = name

    def date(self) -> datetime:
        return self._date

    def result(self) -> bool:
        return self._result

    def name(self) -> str:
        return self._name
