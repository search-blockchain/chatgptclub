from chatgpt import question
from search import google
from club import db
from apscheduler.schedulers.blocking import BlockingScheduler


def initDB():
    db_con = db.DBSqlite("chat.db")  
    keywords_sql = '''
    create table if not exists keywords (
	origin TEXT,
	word TEXT,
	limit_time INTEGER
    );'''
    db_con.updateData(keywords_sql)

    gpt_answer_sql = '''
    create table if not exists gpt_answer (
	question TEXT,
	answer TEXT,
	limit_time INTEGER,
	checkout INTEGER
    );'''
    db_con.updateData(gpt_answer_sql)

    question_model_sql = '''
    create table if not exists question_model (
	prefix TEXT,
	suffix TEXT
    , model INTEGER);'''
    db_con.updateData(question_model_sql)

def jobKeyWords():
    google_trend = google.Trends()
    keywords, sql = google_trend.getKeyWord()
    db_con = db.DBSqlite("chat.db")  
    db_con.updateData(sql)

limit_time = 0
def jobChatGpt():
    db_con = db.DBSqlite("chat.db")  
    global limit_time
    chat_robot = question.Chat("you open ai api key")
    sql = 'SELECT word, limit_time FROM keywords WHERE limit_time > %d;'%(limit_time)
    keywords_row = db_con.getData(sql)
    sql_prefix = '''INSERT INTO gpt_answer (question, answer, limit_time, checkout) VALUES '''
    sql_value = ''
    for i in range(len(keywords_row)):
        row= keywords_row[i]
        word = row[0]
        result = chat_robot.ask(word)
        if i == 0:
            sql_value = sql_value + str(result)
        else :
            sql_value = sql_value + ',' +str(result)
        time = row[1]
        if time > limit_time :
            limit_time = time

    sql = sql_prefix + sql_value
    db_con.updateData(sql)
    
def jobPushClub():
    print("waiting club .......")

def jobRealtimeTrends():
    print("waiting club .......")
    google_trend = google.Trends()
    realtime_trends = google_trend.getRealTrends()
    

if __name__ == '__main__':
    initDB()
    scheduler = BlockingScheduler()
    #scheduler.add_job(jobKeyWords, 'interval', seconds=10)
    #scheduler.add_job(jobChatGpt, 'interval', minutes=10)
    scheduler.add_job(jobRealtimeTrends, 'interval', seconds=10)
    scheduler.add_job(jobPushClub, 'interval', seconds=10)
    scheduler.start()
