#from threading import Thread

#from apscheduler.schedulers.background import BackgroundScheduler#
# import time
# import atexit

import sys

path = '/home/news_focus_backend/app'

if path not in sys.path
    sys.path.append(path)

from app import app

from app.all_news.controllers import delete_all_news, insert_all_news
from app import db


#def refresh_all_news(database):
#    delete_all_news(database)
#    insert_all_news(database)


#def execute_refresh_thread(database):
#    thread = Thread(target=lambda: refresh_all_news(database))
#    thread.start()


#def init_scheduler(database):
#    scheduler = BackgroundScheduler()
#    scheduler.add_job(func=lambda: execute_refresh_thread(database), trigger="interval", seconds=120)
#    scheduler.start()

    # Shut down the scheduler when exiting the app
#    atexit.register(lambda: scheduler.shutdown())

delete_all_news(db)
insert_all_news(db)
