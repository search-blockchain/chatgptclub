from google_trends import daily_trends, realtime_trends
import datetime 
class Trends(object):
    
    sql_keywords_prefix = '''INSERT INTO keywords (origin, word, limit_time) VALUES '''
    sql_keywords_value = ''

    def __init__(self):
        print("init trends")

    def getKeyWord(self):
        today_trends = daily_trends(country='US')
        print(today_trends)
        now_time = int(datetime.datetime.now().timestamp())
        self.sql_keywords_value = ''
        for i in range(len(today_trends)):
            value = ('google', today_trends[i] ,now_time)
            if i == 0:
                self.sql_keywords_value = self.sql_keywords_value + str(value)
            else :
                self.sql_keywords_value = self.sql_keywords_value + "," + str(value)

        sql = self.sql_keywords_prefix + self.sql_keywords_value
        return today_trends, sql

    def getRealTrends(self):
        real_trends = realtime_trends(country='DE', category='t', language='en-UK', num_results=2)
        print(real_trends)
        return real_trends