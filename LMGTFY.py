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
            url_title = quote_plus(submission.title)
            reply_text = REPLY_TEMPLATE.format(url_title)
            print(f"Replying to: {submission.title}")
            submission.reply(reply_text)
            break

def main():
    reddit = praw.Reddit('bot2')
    subreddit = reddit.subreddit('pythonforengineers')

    for submission in subreddit.stream.submissions():
        process_submission(submission)

if __name__ == "__main__":
    main()