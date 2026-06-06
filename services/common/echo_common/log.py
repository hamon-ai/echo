import colorlog
import logging

LOG_FMT = "%(log_color)s%(asctime)s %(levelname)s%(reset)s %(message)s"
TIME_FMT = "%H:%M:%S"
COLOR_FMT = {
    "DEBUG": "cyan",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "bold_red",
}


def configure(debug=False):
    level = logging.DEBUG if debug else logging.INFO
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(LOG_FMT, TIME_FMT, log_colors=COLOR_FMT)
    )
    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(level)


logger = logging.getLogger()
