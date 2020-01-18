queues = {
    'a': [],
    'b': [],
    'c': []
}

VERY_PRIVATE_PASS = 'admin1'


def officer_handling(officer_choice):
    if officer_choice in queues.keys():
        if len(queues[officer_choice]):
            return queues[officer_choice].pop(0)
        print("Nie ma ludzi :) masz przerwe!")
    else:
        print("Nieprawidlowa nazwa kolejki!")


if __name__ == "__main__":
    while True:
        choice = input("Witaj, wybierz kolejke: ").lower()

        if choice in queues.keys():
            q = queues[choice]
            new_number = q[-1] + 1 if len(q) else 1
            q.append(new_number)
            print(f"Twoj numerek to {choice}{new_number}")
        elif choice == VERY_PRIVATE_PASS:
            oc = input("Wybierz kolejke z ktorej zdjac: ").lower()
            queue_number = officer_handling(oc)
            if queue_number is not None:
                print(f"Urzedniku, obslugujesz teraz {oc}{queue_number}")
        else:
            print("Nieprawidlowa nazwa kolejki!")
