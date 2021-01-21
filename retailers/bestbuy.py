import json
import os
from util.constants import (
    BESTBUY_QUERY_API_ENDPOINT,
    BESTBUY_API_ENDPOINT,
    BESTBUY_PRODUCTS,
)
import util.notification_handler as notify
from util.helper_functions import (
    print_in_stock_msg,
    get_bestbuy_product_discord_info,
    print_out_of_stock_msg,
    get_specific_webhook_id,
)


async def get_bestbuy_query_response(session, product_query_list, products_in_stock):
    product_string = "3070,3080,3090,6800"  # TODO: replace with real products

    async with session.get(
        BESTBUY_QUERY_API_ENDPOINT.format(product_string, os.getenv("BESTBUY_API_KEY"))
    ) as resp:
        if resp.status != 200:
            print("Error returned by BestBuy's query API:")
            print("Status: {}".format(resp.status))
            print(await resp.text())
        resp_text = await resp.text()
    resp_json = json.loads(resp_text)

    for product in resp_json["products"]:
        is_orderable = product["orderable"]
        is_available_online = product["onlineAvailability"]
        product_sku = product["sku"]
        product_name = product["name"]

        if is_orderable == "Available" and is_available_online:
            if not products_in_stock[product_sku]:
                print_in_stock_msg(product_name)
                discord_info = get_bestbuy_product_discord_info(product_name)

                # we don't want to edit the product while iterating over it
                product_copy = product.copy()
                product_copy["brand"] = product["manufacturer"]
                product_copy["item_number"] = product_sku

                product_copy["discord_channel"] = discord_info["discord_channel"]
                product_copy["series"] = discord_info["series"]
                product_copy["model"] = discord_info["model"]

                notify.send_stock_alert(
                    retailer="BestBuy",
                    product=product_copy,
                    item_name=product_name,
                    product_image=product["thumbnailImage"],
                    quantity="unknown",
                    is_combo=False,
                )
                products_in_stock[product_sku] = True
        else:
            if products_in_stock[product_sku]:
                print_out_of_stock_msg(product_name)
                notify.edit_stock_alert(get_specific_webhook_id(product_sku))
                products_in_stock[product_sku] = False


async def get_bestbuy_response(session, product_list, products_in_stock):
    product_string = "6438943,6439000,6438942,6438941,6428324,6430277,6430161,6426149"  # TODO: replace with real product list

    async with session.get(
        BESTBUY_API_ENDPOINT.format(product_string, os.getenv("BESTBUY_API_KEY"))
    ) as resp:
        if resp.status != 200:
            print("Error returned by BestBuy's product API:")
            print("Status: {}".format(resp.status))
            print(await resp.text())
        resp_text = await resp.text()
    resp_json = json.loads(resp_text)

    for product in resp_json["products"]:
        item_number = str(product["sku"])
        item_name = product["name"]
        is_orderable = product["orderable"]
        is_available_online = product["onlineAvailability"]

        if is_orderable == "Available" and is_available_online:
            if not products_in_stock[
                item_number
            ]:  # TODO: Check if available for purchase
                print_in_stock_msg(item_name)
                notify.send_stock_alert(
                    retailer="BestBuy",
                    product=BESTBUY_PRODUCTS[item_number],
                    item_name=item_name,
                    product_image=product["image"],
                    quantity="unknown",
                    is_combo=False,
                )
                products_in_stock[item_number] = True
        else:
            if products_in_stock[item_number]:
                print_out_of_stock_msg(item_name)
                notify.edit_stock_alert(get_specific_webhook_id(item_number))
                products_in_stock[item_number] = False
