import praw, time

keywords = ['XXXX', 'XXXX', 'XXXX']


reddit = praw.Reddit(client_id='client id',
                    client_secret='client secret',
                    password='password',
                    user_agent='something',
                    username='username')


subreddit = reddit.subreddit('soccer')
yesterday = int(time.time()) - (24*60*60)


def get_info():
    '''
    Get subreddit title and link if the keywords are found
    '''
    for submission in subreddit.stream.submissions():
        title = submission.title
        for key in keywords:
            if submission.created_utc > yesterday and key in title:
                wanted_title = submission.title
                link = submission.permalink
                full_url = f'https://reddit.com/{link}'
                message = f'Title: {wanted_title}, Link: {full_url}'
                print(message)


get_info()





            







