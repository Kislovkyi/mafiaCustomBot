class TelegramUser:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def __str__(self):
        return f"User ID: {self.user_id}, User Name: {self.user_name}"