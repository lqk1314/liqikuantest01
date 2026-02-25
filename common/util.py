import json
import logging
import os





class GetLog:
    log=None
    @classmethod
    def get_log(cls):
        if cls.log is None:
            cls.log=logging.getLogger()
            cls.log.setLevel(logging.INFO)
            current_dir = os.path.dirname(__file__)
            log_dir = os.path.join(current_dir, 'log')
            file_path = os.path.join(log_dir, 'log_web.txt')
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            from logging.handlers import TimedRotatingFileHandler
            tf= TimedRotatingFileHandler(filename=file_path,
                                                 when="midnight",
                                                 interval=1,
                                                 backupCount=3,
                                                 encoding="utf_8"
                                                 )
            fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm=logging.Formatter(fmt)
            tf.setFormatter(fm)
            cls.log.addHandler(tf)

        return cls.log




def web_login_data(key):
    current_dir=os.path.dirname(__file__)
    file_path=os.path.join(current_dir,'data','data.json')
    list=[]
    with open(file_path,"r",encoding='utf-8') as f:
        for i in json.load(f).get(key):
            data=tuple(i.values())
            list.append(data)
        return list

if __name__=='__main__':
    aa=web_login_data('web_log')
    bb=web_login_data('web_day')
