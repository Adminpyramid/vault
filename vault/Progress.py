import logging


class ProgressBar:
    def __init__(self, total, bar_length=50, fill_char="#"):
        self.total = total
        self.bar_length = bar_length
        self.fill_char = fill_char
        self.rotating_chars = ["|", "/", "-", "\\"]

        # Initialize logging
        logging.basicConfig(filename='progress.log', level=logging.INFO,
                            format='%(asctime)s - %(message)s')

    def print_progress(self, iteration):
        progress = (iteration / self.total)
        filled_length = int(self.bar_length * progress)
        bar = self.fill_char * filled_length
        empty = " " * (self.bar_length - filled_length)

        rotating_char = self.rotating_chars[iteration % len(self.rotating_chars)]
        log_message = "\r\033[32;1m[{}] {:.0f}% {}\033[0m".format(bar + empty, progress * 100, rotating_char)
        logging.info(log_message)
