from typing import Union
import requests
import time
import json
import re

from requests.api import head


def main():
    latest_announcement = json.loads(requests.get(
        "https://www.binance.com/bapi/composite/v1/public/cms/article/catalog/list/query?catalogId=48&pageNo=1&pageSize=15&rnd=" + str(time.time())).text)
    # print(json.dumps(latest_announcement["data"], indent=4, sort_keys=True))

    print("Got binance announcements. Checking against cached...")
    previous_announcements = {"data":{"articles":[]}}
    try:
        with open("previous_announcements.json") as f:
            previous_announcements = json.load(f)
    except:
        print("No previous announcements found.")
        previous_announcements = {"data":{"articles":[]}}
        
    new_announcements = [a for a in latest_announcement["data"]["articles"] if a not in previous_announcements["data"]["articles"]]
    if not new_announcements:
        print("Nothing new.")
        return

    symbols = []
    symbols_to_ignore = ["USDT", "BTC", "BNB", "BUSD", "ETH", "AUD", "USD"]
    for article in new_announcements:
        print("New article:\n\t" + article["title"])
        [symbols.append(s) for s in re.findall(
            "[A-Z]{2,15}", article["title"]) if s not in (symbols_to_ignore + symbols)]
        
    with open("previous_announcements.json", "w") as f:
        json.dump(latest_announcement, f)
    
    # Alternate re: "[A-Z\/\_]{2,15}"
    print("Extracted symbols:")
    print("\t" + str(symbols))

    host = "https://api.gateio.ws/api/v4{}"
    headers = {"Accept": "application/json",
                "Content-Type": "application/json"}

    gateio_tickers = json.loads(requests.get(
        host.format("/spot/tickers", headers=headers)).text)
    # print(json.dumps(gateio_tickers, indent=4, sort_keys=True))

    hit = []
    for ticker in gateio_tickers:
        hit = list(filter(lambda el: (
            el not in symbols_to_ignore and el in symbols),
            str(ticker["currency_pair"]).split("_")))
        if hit:
            print(f"Found binance announcement currency {hit} on GateIO:")
            print(json.dumps(ticker, indent=4, sort_keys=True))

    if not hit:
        print("No hits on GateIO.")


if __name__ == '__main__':
    while(True):
        print("Starting new cycle...")
        main()
        print("Cycle done.")
        time.sleep(60 * 10)

# Copy log
# Save log

# Button to open window to edit priority list

# Listen to authorizedcapabilityuserlist

# Listen to route_validation.hpp

# 155:

# Make dds conversion files for rsp/route_validation.hpp



def add_two_numbers(x: int, y: int) -> int:
    x + y

add_two_numbers("hi", 2)
