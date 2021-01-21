from util.constants import (
    BESTBUY_PRODUCT_QUERIES,
    COMBO_WEBHOOK_ID,
    SPECIFIC_CHANNEL_WEBHOOK_ID,
)
import random


def print_in_stock_msg(item_name):
    print("++++++++++++++++++++++++")
    print("{} is in stock.".format(item_name))
    print("++++++++++++++++++++++++")


def print_out_of_stock_msg(item_name):
    print("------------------------")
    print("{} is no longer in stock".format(item_name))
    print("------------------------")


def get_specific_webhook_id(item_number):
    return SPECIFIC_CHANNEL_WEBHOOK_ID.format(item_number)


def get_combo_webhook_id(item_number):
    return COMBO_WEBHOOK_ID.format(item_number)


def get_check_interval():
    return random.uniform(3, 6)


def get_bestbuy_product_discord_info(name):
    product_list = ["3070", "3080", "3090", "5600"]  # TODO: get this programatically
    for product in product_list:
        if product in name:
            return BESTBUY_PRODUCT_QUERIES[product]
    else:
        return BESTBUY_PRODUCT_QUERIES["3070"]  # TODO: error handle this later


def get_product_info_from_name(name, keywords):
    for keyword in keywords:
        if keyword in name:
            product_model = keyword

            if product_model in ("6800", "6900"):
                product_discord_channel = "big-navi"
            elif product_model in ("5600X", "5800X", "5900X", "5950X"):
                product_discord_channel = "zen-3"
            else:
                product_discord_channel = product_model

            return product_model, product_discord_channel


def get_product_brand(name):
    return name.split()[0]
