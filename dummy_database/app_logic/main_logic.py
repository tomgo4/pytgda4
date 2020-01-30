from app_interface.user_io import UserIO
from app_logic.create_logic import CreateLogic
from app_logic.query_parser import QueryParser


class MainLogic:
    def run(self):
        uio = UserIO()
        uio.print_menu()
        while True:
            query = uio.user_input()
            if query.lower() == "exit":
                break
            if query.lower() == "help":
                uio.print_help()
                continue
            qp = QueryParser()
            parsed_obj = qp.parse(query)
            if parsed_obj["command"] == "create":
                cl = CreateLogic()
                cl.create(parsed_obj)
