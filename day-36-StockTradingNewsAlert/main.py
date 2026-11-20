import os
import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
AV_API_KEY = os.environ.get("AV_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")
to_email = os.environ.get("TO_EMAIL")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": AV_API_KEY,
}

NEW_HEADER = {
    "X-Api-Key": NEWS_API_KEY
}

news_params = {
    "q": COMPANY_NAME,
    "searchIn": "title",
    "sortBy": "publishedAt",
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Stock API
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
data = stock_response.json()
stock_data = data["Time Series (Daily)"]

closing_data = [value['4. close'] for (key, value) in stock_data.items()]
yesterday_price = float(closing_data[0])
day_before_yesterday_price = float(closing_data[1])

diff = yesterday_price - day_before_yesterday_price
up_down = "🔺" if diff > 0 else "🔻"

per_diff = round((diff / yesterday_price) * 100)

# #Run 5 for stock apiendpoint, news 2
if abs(per_diff) > 0:
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params, headers=NEW_HEADER)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in
                          three_articles]
    with smtplib.SMTP('smtp.gmail.com')as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        # Optional TODO: Format the message like this:
        for article_msg in formatted_articles:
            email_body = f"Subject: {STOCK_NAME}: {up_down} {per_diff}%\n\n\n{article_msg}"
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=email_body.encode("utf-8")
            )

