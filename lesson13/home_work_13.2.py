class Counter:

    def __init__(self, current: int=1, min_value: int=0, max_value: int=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start: int):
        self.current = start

    def set_max(self, max_max: int):
        self.max_value = max_max

    def set_min(self, min_min: int):
        self.min_value = min_min

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Достигнут максимум")
        else:
            self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Достигнут минимум")
        else:
            self.current -= 1

    def get_current(self):
        return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'