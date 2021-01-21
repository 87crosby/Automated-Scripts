import aiohttp
import asyncio
import os
import schedule
import sys
import time
import util.notification_handler as notify

from collections import defaultdict
from datetime import datetime
from retailers.newegg import get_newegg_combo_response, get_newegg_standalone_response
from util.constants import (
    NEWEGG_COMBO_QUERY_LIST,
    NEWEGG_STANDALONE_QUERY_LIST,
)


async def main():
    products_in_stock = defaultdict(lambda: False)
    combos_in_stock = defaultdict(lambda: False)
    # Configure HTTP connector & session
    connector = aiohttp.TCPConnector(ssl=False)
    timeout = aiohttp.ClientTimeout(total=15)
    headers = {"cache-control": "max-age=0, no-cache"}
    session = aiohttp.ClientSession(
        connector=connector, timeout=timeout, headers=headers
    )

    # Track how long we've been checking stock for
    script_start_time = datetime.now()
    script_end_time = datetime.now()
    script_run_time = 0
    script_run_time_in_min = 0

    while script_run_time_in_min < 20:
        tasks = []
        for standalone_query in NEWEGG_STANDALONE_QUERY_LIST:
            timestamp = int(round(time.time() * 1000))
            tasks.append(
                asyncio.create_task(
                    get_newegg_standalone_response(
                        session, standalone_query, timestamp, products_in_stock
                    )
                )
            )

        for combo_query in NEWEGG_COMBO_QUERY_LIST:
            timestamp = int(round(time.time() * 1000))
            tasks.append(
                asyncio.create_task(
                    get_newegg_combo_response(
                        session, combo_query, timestamp, combos_in_stock
                    )
                )
            )

        # Track how long it takes for all queries to complete
        start_time = datetime.now()
        await asyncio.gather(*tasks, return_exceptions=True)
        end_time = datetime.now()

        time_elapsed = end_time - start_time
        current_time = end_time.strftime("%I:%M:%S %p PST")

        print(
            "Stock checked at {}, which took {} seconds.".format(
                current_time, round(time_elapsed.total_seconds(), 2)
            )
        )

        script_end_time = datetime.now()
        script_run_time = script_end_time - script_start_time
        script_run_time_in_min = round(script_run_time.total_seconds() / 60, 2)

    print("Stock bot stopped running after {} minutes.".format(script_run_time_in_min))
    notify.end_bot_status()
    session.close()


def job():
    try:
        notify.start_bot_status()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except:
        print("Interrupted")
        try:
            notify.end_bot_status()
            sys.exit(0)
        except SystemExit:
            os._exit(0)


schedule.every().monday.at("16:29").do(job)
schedule.every().tuesday.at("16:29").do(job)
schedule.every().wednesday.at("16:29").do(job)
schedule.every().thursday.at("16:29").do(job)
schedule.every().friday.at("16:29").do(job)
schedule.every().monday.at("16:59").do(job)
schedule.every().tuesday.at("16:59").do(job)
schedule.every().wednesday.at("16:59").do(job)
schedule.every().thursday.at("16:59").do(job)
schedule.every().friday.at("16:59").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

if __name__ == "__main__":
    job()
