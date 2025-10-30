import logging, sys
FMT='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
def get_logger(name='fortis'):
    lg=logging.getLogger(name)
    if not lg.handlers:
        lg.setLevel(logging.DEBUG)
        h=logging.StreamHandler(sys.stdout); h.setFormatter(logging.Formatter(FMT)); lg.addHandler(h)
        lg.propagate=False
    return lg
