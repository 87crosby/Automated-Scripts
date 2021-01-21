import asyncio
import aiohttp
import json

from collections import defaultdict
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
from util.constants import (
    DISCORD_CHANNEL_INFO,
    RETAILER_ICONS,
    STOCK_BOT_DISCORD_CHANNEL_URL,
    COMBO_WEBHOOK_ID,
    SPECIFIC_CHANNEL_WEBHOOK_ID,
    NEWEGG_COMBO_URL,
    BOT_STATUS_DISCORD_CHANNEL_URL,
)


sent_webhook_messages = {}
sent_role_pings = defaultdict(lambda: datetime.min)


def send_stock_alert(
    retailer,
    product,
    item_name,
    is_combo,
    product_image=None,
    quantity=None,
):
    item_number = product["item_number"]
    discord_channel = product["discord_channel"]
    discord_role_id = DISCORD_CHANNEL_INFO[discord_channel]["role_id"]

    sent_webhooks = []
    webhook_id = ""

    webhook_id = SPECIFIC_CHANNEL_WEBHOOK_ID.format(item_number)
    discord_channel_url = DISCORD_CHANNEL_INFO[discord_channel]["channel_url"]

    sent_webhooks.append(
        send_webhook_message(
            retailer,
            product,
            item_name,
            product_image,
            quantity,
            is_combo,
            discord_role_id,
            discord_channel_url,
            in_stock_bot_chat=False,
        )
    )

    sent_webhook_messages[webhook_id] = sent_webhooks


def send_webhook_message(
    retailer,
    product,
    item_name,
    product_image,
    quantity,
    is_combo,
    discord_role_id,
    discord_channel,
    in_stock_bot_chat,
):

    webhook = DiscordWebhook(discord_channel)
    # create embed object for webhook
    embed = DiscordEmbed(description=item_name, color=0x10AC00)

    product_url = product["url"]
    # set description
    if is_combo:
        embed.set_description("{} is available IN A COMBO.".format(item_name))
        embed.set_title("COMBO IN STOCK!!")
    else:
        embed.set_description("{} is now in stock.".format(item_name))
        embed.set_title("{} IN STOCK!!".format(item_name))

    # set author
    embed.set_author(name=retailer, url=product_url, icon_url=RETAILER_ICONS[retailer])

    # set thumbnail
    if product_image:
        embed.set_thumbnail(url=product_image)

    # set footer
    embed.set_footer(
        text="Please report any issues by sending the @programmer role a message."
    )

    # set timestamp (default is now)
    embed.set_timestamp()

    # add fields to embed
    if product["brand"]:
        embed.add_embed_field(name="Brand", value=product["brand"])

    if product["model"]:
        embed.add_embed_field(name="Model", value=product["model"])

    if product["series"]:
        embed.add_embed_field(name="Series", value=product["series"])
    embed.add_embed_field(name="URL", value=product_url)

    # add embed object to webhook
    webhook.add_embed(embed)

    # ping discord roles if not in stock-bot
    if not in_stock_bot_chat:
        time_since_last_ping = datetime.now() - sent_role_pings[discord_role_id]
        time_since_last_ping_in_sec = round(time_since_last_ping.total_seconds(), 2)

        if time_since_last_ping_in_sec > 600:
            webhook.set_content("<@&{}>".format(discord_role_id))
            sent_role_pings[discord_role_id] = datetime.now()

    sent_webhook = webhook.execute()

    # add not-in-stock edited webhook message and save it for later
    webhook.remove_embed(0)
    embed.set_color(0xC90000)

    if is_combo:
        embed.set_title("Combo is no longer in stock.")
        embed.set_description("{} is no longer available in a combo.".format(item_name))
    else:
        embed.set_title("Item is no longer in stock.")
        embed.set_description(
            "{} is not in stock.\n Quantity sold: {}".format(item_name, quantity)
        )
    webhook.add_embed(embed)

    return (webhook, sent_webhook)


def edit_stock_alert(webhook_id):
    # send out edited stock alert message in #stock-bot and specific / combo channel
    for webhook_message in sent_webhook_messages[webhook_id]:
        webhook, sent_webhook = webhook_message

        sent_webhook = webhook.edit(sent_webhook)


def start_bot_status():
    webhook = DiscordWebhook(BOT_STATUS_DISCORD_CHANNEL_URL)
    # create embed object for webhook
    embed = DiscordEmbed(
        description="BOT IS RUNNING\nStarted running on {}".format(
            datetime.now().strftime("%Y-%m-%d, %I:%M %p PST")
        ),
        color=0x10AC00,
    )

    # add embed object to webhook
    webhook.add_embed(embed)
    sent_webhook = webhook.execute()
    sent_webhook_messages["bot_status"] = (webhook, sent_webhook)


def end_bot_status():
    webhook, sent_webhook = sent_webhook_messages["bot_status"]
    webhook.remove_embed(0)
    embed = DiscordEmbed(
        description="BOT IS NO LONGER RUNNING\nStopped running on {}".format(
            datetime.now().strftime("%Y-%m-%d, %I:%M %p PST")
        ),
        color=0xC90000,
    )
    webhook.add_embed(embed)
    sent_webhook = webhook.edit(sent_webhook)
