users = [
   {
       "first_name": "Jan",
       "last_name": "Nowak",
       "nick": "jano",
       "phone": "123123123",
       "active": True,
       "other": {}
   },
   {
       "first_name": "Ewa",
       "last_name": "Nowak",
       "nick": "eno",
       "phone": "789789789",
       "active": False
   }
]


def add_user(first_name: str, last_name, nick=None, phone=None,
             active=True, **other) -> None:
    if 'other' in other:
        other = other['other']

    users.append({
        "first_name": first_name,
        "last_name": last_name,
        "nick": (first_name[:3] + last_name[:3] if nick is None else nick).lower(),
        "phone": phone,
        "active": active,
        "other": other
   })


if __name__ == "__main__":
    # add_user("Imie", "Nazwisko", "Nicjkfasdf", "59875", False)
    # add_user("Imie2", "Nazwisko2")
    # add_user("Imie", "nazwisko", city="Gdansk")
    add_user(**users[0])
    print(users)
