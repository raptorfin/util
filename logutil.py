import logging

def init_log(lvl, log):
    vlevel = getattr(logging, lvl.upper(), None)
    if not isinstance(vlevel, int):
        raise ValueError('Invalid log level: %s' % vlevel)
    logging.basicConfig(level=vlevel,
                        format='%(asctime)s|%(name)s|%(levelname)s|%(message)s',
                        filename=log,
                        filemode='w')
    con = logging.StreamHandler()
    con.setLevel(logging.INFO)
    logging.getLogger('').addHandler(con)