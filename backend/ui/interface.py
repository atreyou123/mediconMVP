class ConsoleUI:
    """
    Minimal console interface prototype (SRS: User Interface Module).
    """

    def get_user_input(self):
        return input("Describe your symptom: ")

    def show(self, message: str):
        print(message)
