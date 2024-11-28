class InfoConfig:
    _usuario = None

    def __new__(cls):
        if cls._usuario is None:
            cls._usuario = super().__new__(cls)
            cls._usuario.current_user = None
            cls._usuario.language = "en"
            cls._usuario.time = None
            cls._usuario.money = None
            cls._usuario.meter = None
        return cls._usuario

    def __str__(self):
        return f'{self.current_user} {self.language} {self.time} {self.money} {self.meter}'

    def get_current_user(self):
        return self.current_user

    def set_current_user(self, current_user):
        self.current_user = current_user

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def get_language(self):
        return self.language

    def set_language(self, language):
        self.language = language

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money = money

    def get_meter(self):
        return self.meter

    def set_meter(self, meter):
        self.meter = meter