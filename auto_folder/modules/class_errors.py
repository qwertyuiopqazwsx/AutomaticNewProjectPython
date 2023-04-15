class AutomaticError(Exception):
    def __init__(self, *args: Exception) -> None:
        super().__init__(*args)
        if args:
            self.message_error = args[0]
        else:
            self.message_error = None
    
    def __str__(self) -> str:
        if self.message_error:
            return f'AutomaticError {self.message_error}'
        else:
            return f'AutomaticError error without a error'

if __name__ == "__main__":
    raise AutomaticError