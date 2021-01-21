import asyncio
import random
import util.notification_handler as notify

from bs4 import BeautifulSoup
from util.helper_functions import (
    get_product_brand,
    get_product_info_from_name,
    print_in_stock_msg,
)


async def get_newegg_standalone_response(
    session, product_query, timestamp, products_in_stock
):
    await asyncio.sleep(random.uniform(0.2, 1))
    power_search = product_query["power_search"]

    async with session.get(product_query["query_url"].format(timestamp)) as resp:
        if resp.status != 200:
            print(
                "Error returned by Newegg's API for {}, timestamp was {}".format(
                    power_search, timestamp
                )
            )
            print("Status: {}".format(resp.status))

        resp_text = await resp.text()
        if "Are you a human?" in resp_text:
            print("Ran into captcha on {} search.".format(power_search))

        soup = BeautifulSoup(resp_text, "html.parser")

        for item in soup.body.find_all("div", class_="item-container"):
            buttons = item.find_all("button", class_="btn btn-primary btn-mini")

            item_info = item.find_all("a", class_="item-title")[0]

            item_name = item_info.string
            item_url = item_info["href"]
            is_in_stock = False
            product_image = item.find_all("img")[0]["src"]

            for button in buttons:
                if button and button.text.strip() == "Add to cart":
                    is_in_stock = True
                    break

            if is_in_stock:
                product_model, product_discord_channel = get_product_info_from_name(
                    item_name, product_query["keywords"]
                )

                if not products_in_stock[item_name]:
                    print_in_stock_msg(item_name)
                    product = {
                        "brand": get_product_brand(item_name),
                        "item_number": item_name,
                        "model": product_model,
                        "series": product_model,
                        "discord_channel": product_discord_channel,
                        "url": item_url,
                    }
                    print(product, item_name, product_image)
                    try:
                        notify.send_stock_alert(
                            retailer="Newegg",
                            product=product,
                            item_name=item_name,
                            product_image=product_image,
                            is_combo=False,
                        )
                    except Exception as err:
                        print("Error when sending out alert. Error: {}".format(err))
                    products_in_stock[item_name] = True


async def get_newegg_combo_response(session, product_query, timestamp, combos_in_stock):
    await asyncio.sleep(random.uniform(0.2, 5))
    product_model = product_query["model"]
    product_discord_channel = product_query["discord_channel"]

    async with session.get(product_query["query_url"].format(timestamp)) as resp:
        if resp.status != 200:
            print(
                "Error returned by Newegg's API for {}, timestamp was {}".format(
                    product_model, timestamp
                )
            )
            print("Status: {}".format(resp.status))

        resp_text = await resp.text()
        if "Are you a human?" in resp_text:
            print("Ran into captcha on {} search.".format(product_model))

        soup = BeautifulSoup(resp_text, "html.parser")

        for item in soup.body.find_all("div", class_="item-container"):
            buttons = item.find_all("button", class_="btn btn-primary btn-mini")

            item_info = item.find_all("a", class_="item-title")[0]
            item_name = item_info.string
            item_url = item_info["href"]
            combo_id = item_url.rsplit("=", 1)[1]
            is_in_stock = False

            for button in buttons:
                if button and button.text.strip() == "Add to cart":
                    is_in_stock = True
                    break

            if is_in_stock:
                if not combos_in_stock[combo_id]:
                    print_in_stock_msg(item_name)
                    product = {
                        "brand": None,
                        "item_number": combo_id,
                        "model": product_model,
                        "series": product_model,
                        "discord_channel": product_discord_channel,
                        "url": item_url,
                    }
                    try:
                        notify.send_stock_alert(
                            retailer="Newegg",
                            product=product,
                            item_name=item_name,
                            product_image="https://c1.neweggimages.com/ProductImageCompressAll35/combo{}.jpg".format(
                                combo_id.rsplit(".", 1)[1]
                            ),
                            is_combo=True,
                        )
                    except Exception as err:
                        print("Error when sending out alert. Error: {}".format(err))
                    combos_in_stock[combo_id] = True
