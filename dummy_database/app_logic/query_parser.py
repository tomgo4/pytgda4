import re
from app_logic.app_commands import COMMANDS

# CREATE DOCUMENT uczestnicy (id, imie, nazwisko, wiek, plec)
# ADD (1, Maria, Nowak, 44, K) TO uczestnicy
# SELECT (imie) FROM uczestnicy

class QueryParser:
    def parse(self, query):
        for key, value in COMMANDS.items():
            parsed = re.findall(value["regex"], query)
            if len(parsed) == 0:
                continue
            object_to_return = {
                "command": key
            }
            parsed = parsed[0]
            for index in range(len(parsed)):
                object_to_return[value["order"][index]] = \
                    parsed[index]
            return object_to_return