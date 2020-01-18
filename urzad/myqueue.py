class MyQueue:
    q = []

    def add_element(self, number):
        self.q.append(number)

    def remove_element(self):
        self.q.pop(0)

    def get_last(self):
        return self.q[-1] if len(self.q) else 0
