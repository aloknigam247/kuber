"""Module: logger """

class Logger:
    def error(*message: str):
        print("ERROR:", *message)

    def info(*message: str):
        print("INFO:", *message)
        
    def wait(*message: str):
        print(*message, "...")

    def warn(*message: str):
        print("WARNING:", *message)