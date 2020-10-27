class LogMixin:
    @staticmethod
    def write_file(msg):
        with open("log.txt", "a+") as f:
            f.write(msg)
            f.write("\n")

    def log_erro(self, msg):
        self.write_file(f"Error: {msg}")

    def wrn_erro(self, msg):
        self.write_file(f"Wrn: {msg}")
