from urllib.parse import quote_plus

import praw

QUESTIONS = ["what is", "what are", "who is","why"]
REPLY_TEMPLATE = "[Let me Google it for you](https://google.com/search?q={})"

def process_submission(submission):
    if len(submission.title.split()) > 10 :
        return

    normalized_title = submission.title.lower()
    for question_phrase in QUESTIONS:
        if question_phrase in normalized_title:
            #parses the title for proper URL title such as maps ? to %3f since url has special meaning of ?. also space with '+' sign
            url_title = quote_plus(submission.title)
            #.format in a explictly manner in replt_template format input
            reply_text = REPLY_TEMPLATE.format(url_title)
            print(f"Replying to: {submission.title}")
            #replys to the thread in the Subreddit
            submission.reply(reply_text)
            break

def main():
    reddit = praw.Reddit('bot2')
    subreddit = reddit.subreddit('pythonforengineers')
    #stream continuously checks the subreddit in a infinte loop
    for submission in subreddit.stream.submissions():
        #function call
        process_submission(submission)

if __name__ == "__main__":
    main()