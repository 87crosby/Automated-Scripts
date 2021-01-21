######################
#   DISCORD URLs     #
######################

STOCK_BOT_DISCORD_CHANNEL_URL = "https://discord.com/api/webhooks/782191097534349322/l7VakY6PIagys_dLSvIThebmlFosbplFDNGknrg6w5FsYWNfXmt4uLQgOs_I3xir39hr"  # CHANGE THIS URL FOR TESTING
BOT_STATUS_DISCORD_CHANNEL_URL = "https://discord.com/api/webhooks/786029741190807562/mngz_t_OvDi5DB5GdY4_fv11m6rNQ28gmhKl5Y75jfFTLT6wmJq9QQYUFClg5nftSHYd"
COMBO_WEBHOOK_ID = "{}-combo"
SPECIFIC_CHANNEL_WEBHOOK_ID = "{}-specific"
DISCORD_CHANNEL_INFO = {
    "3060": {
        "role_id": "783909133505396746",
        "channel_url": "https://discord.com/api/webhooks/784031455554568204/DMcuVUsyeyouDLsIao4Ypg24CNjSEmpT97qZTzQPQdWGsi9t32vq_xHiGX7Hwe-53G3L",
    },
    "3070": {
        "role_id": "766837495006232626",
        "channel_url": "https://discord.com/api/webhooks/781239002409205821/uJxKvAx5LVcoCi8CZedTY8PXJ7YeaFCZwxGt5qX7j9ZKUnJ8ui9_1pOx85hwQC4nD4x_",
    },
    "3080": {
        "role_id": "766837175378640916",
        "channel_url": "https://discord.com/api/webhooks/781239102422646854/tv5naNlvUpc9nr-KoCIUIEIP5N4jIw_uVPqmM4_1woDd-aqeoq00CXGsPEMNW4H7BfLR",
    },
    "3090": {
        "role_id": "766837418753785857",
        "channel_url": "https://discord.com/api/webhooks/781239250993414175/8gpI5Erqw6wFlkTwrfSHhVWkSZcXLTNnmVFkZdwh1NakhqIO-GWnJfZZ0TH-tnBt8PkN",
    },
    "zen-3": {
        "role_id": "767466498067267604",
        "channel_url": "https://discord.com/api/webhooks/781240663722164304/NJQE4RiMxPNKUh0k5LhvLq77WLhxK4F0mfy3eUeDC0Z-1PUNqAkHyCYNtPi-sT1Dc-jC",
    },
    "big-navi": {
        "role_id": "767466546820939838",
        "channel_url": "https://discord.com/api/webhooks/782004095485214721/JYymoEYovPQadXyFSjFWzQyXVUKnqoD6qplwvGZFR2GY6W3-VI0g4NuKi3IvSNcPfhCt",
    },
    "newegg-combos": {
        "role_id": "",  # we currently do not ping the newegg combo role
        "channel_url": "https://discord.com/api/webhooks/782828788576157736/lAPW3JNxQbmEmR6AKE9pT4vKlUcgE6EyPOGVXjJFJAWtMgz8PmeINX-EVLR6upKUVlby",
    },
    "xbox-sx": {
        "role_id": "767150005760294952",
        "channel_url": "https://discord.com/api/webhooks/782802847539920906/l8jYaZ_LzhLgEBbGtmXEu8b0OXpnAdcPQY22Gw1TWZrnXEVYKDwVk9V9A4YyO6QYLfHl",
    },
    "ps5": {
        "role_id": "766837776058155058",
        "channel_url": "https://discord.com/api/webhooks/782803025374609408/6M7ZtFPjMtog644TkA4APDh2WbJ44u0lyHX-q8I87-tRinngDNWb-qnsGy87LZUOpbnL",
    },
    "test": {
        "role_id": "fake-id",
        "channel_url": "https://discord.com/api/webhooks/780714021899862016/qwDHyxnVsD5U3eqopD_HoadAWpZi6e0GSzNE4eZEu2RCPSLyE4CVkP7HWofbhVe2G2sZ",
    },
}

######################
#    NEWEGG URLs     #
######################


#################
#  How to test  #
#################
# 1) Change STOCK_BOT_DISCORD_CHANNEL_URL to "https://discord.com/api/webhooks/782858772024131654/LCDC6YzgrvGqa-s98fS5vb3tBpBoZyqXk1hKTNrs_eWsbA1EhhdzL5RIRYZkKADWoYXN"
# 2) Comment out everything in NEWEGG_QUERY_LIST, uncomment the test object
# 3) Run bot!

NEWEGG_COMBO_IMAGE_URL = (
    "https://c1.neweggimages.com/ProductImageCompressAll35/combo{}.jpg"
)

NEWEGG_COMBO_URL = "https://www.newegg.com/p/pl?d={}+combo"
NEWEGG_COMBO_QUERY_LIST = [
    {
        "discord_channel": "3060",
        "model": "3060",
        "query_url": "https://www.newegg.com/p/pl?d=rtx+3060+combo&N=100006662&PageSize=96&timestamp={}",
    },
    {
        "discord_channel": "3070",
        "model": "3070",
        "query_url": "https://www.newegg.com/p/pl?d=rtx+3070+combo&N=100006662&PageSize=96&timestamp={}",
    },
    {
        "discord_channel": "3080",
        "model": "3080",
        "query_url": "https://www.newegg.com/p/pl?d=rtx+3080+combo&N=100006662&PageSize=96&timestamp={}",
    },
    {
        "discord_channel": "3090",
        "model": "3090",
        "query_url": "https://www.newegg.com/p/pl?d=rtx+3090+combo&N=100006662&PageSize=96&timestamp={}",
    },
    {
        "discord_channel": "big-navi",
        "model": "6800 / 6800 XT",
        "query_url": "https://www.newegg.com/p/pl?d=6800+combo&N=100007709&isdeptsrh=1&timestamp={}",
    },
    {
        "discord_channel": "big-navi",
        "model": "6900 XT",
        "query_url": "https://www.newegg.com/p/pl?d=6900+xt+combo&N=100007709&isdeptsrh=1&timestamp={}",
    },
    {
        "discord_channel": "zen-3",
        "model": "5900X",
        "query_url": "https://www.newegg.com/p/pl?d=5900x+combo&N=100007671&isdeptsrh=1&PageSize=96&timestamp={}",
    },
    {
        "discord_channel": "zen-3",
        "model": "5950X",
        "query_url": "https://www.newegg.com/p/pl?d=5950x+combo&N=100007671&isdeptsrh=1&PageSize=96&timestamp={}",
    },
    {
        "discord_channel": "zen-3",
        "model": "5600X",
        "query_url": "https://www.newegg.com/p/pl?d=5600x+combo&N=100007671&isdeptsrh=1&PageSize=96&timestamp={}",
    },
    {
        "discord_channel": "zen-3",
        "model": "5800X",
        "query_url": "https://www.newegg.com/p/pl?d=5800x+combo&N=100007671&isdeptsrh=1&PageSize=96&timestamp={}",
    },
    {
        "discord_channel": "xbox-sx",
        "model": "XBox",
        "query_url": "https://www.newegg.com/p/pl?d=xbox+series+combo&N=101696839&isdeptsrh=1&timestamp={}",
    },
    {
        "discord_channel": "ps5",
        "model": "PS5",
        "query_url": "https://www.newegg.com/p/pl?d=ps5&N=101696840&timestamp={}",
    },
    # COMMENT ALL OTHER QUERIES OUT AND UNCOMMENT THIS TO TEST NEWEGG QUERIES
    # {
    #     "discord_channel": "test",
    #     "model": "test",
    #     "query_url": "https://www.newegg.com/p/pl?d=combo&timestamp={}",
    # },
]

NEWEGG_STANDALONE_QUERY_LIST = [
    {
        "power_search": "Standalone GPUs, page 1",
        "keywords": ["3060", "3070", "3080", "3090", "6800", "6900"],
        "query_url": "https://www.newegg.com/p/pl?Submit=Property&Subcategory=48&N=100007709%20601359415%20601357250%20601357247%20601357248%20601359427%20601359422%20601359957%208000&IsPowerSearch=1&PageSize=96&timestamp={}",
    },
    {
        "power_search": "Standalone GPUs, page 2",
        "keywords": ["3060", "3070", "3080", "3090", "6800", "6900"],
        "query_url": "https://www.newegg.com/p/pl?Submit=Property&Subcategory=48&N=100007709%20601359415%20601357250%20601357247%20601357248%20601359427%20601359422%20601359957%208000&IsPowerSearch=1&PageSize=96&timestamp={}&page=2",
    },
    {
        "power_search": "Standalone CPUs",
        "keywords": ["5600X", "5800X", "5900X", "5950X"],
        "query_url": "https://www.newegg.com/p/pl?Submit=Property&Subcategory=343&N=100007671%20601359154%20601359143%20601359147%208000&IsPowerSearch=1&timestamp={}",
    },
]

######################
#    BESTBUY URLs    #
######################

BESTBUY_QUERY_API_ENDPOINT = "https://api.bestbuy.com/v1/products(search in ({})&categoryPath.id=abcat0507002)?apiKey={}&format=json&show=sku,name,orderable,onlineAvailability,url,addToCartUrl,thumbnailImage,manufacturer&pageSize=50"
BESTBUY_API_ENDPOINT = (
    "https://api.bestbuy.com/v1/products(sku in({}))?apiKey={}&format=json"
)

BESTBUY_PRODUCT_QUERIES = {
    "3070": {
        "model": "3070",
        "series": "3070",
        "discord_channel": "3070",
    },
    "3080": {
        "model": "3080",
        "series": "3080",
        "discord_channel": "3080",
    },
    "3090": {
        "model": "3090",
        "series": "3090",
        "discord_channel": "3090",
    },
    "6800": {
        "model": "6800 / 6800 XT",
        "series": "Big Navi",
        "discord_channel": "big-navi",
    },
}


BESTBUY_PRODUCTS = {
    "6438943": {
        "brand": "AMD",
        "item_number": "6438943",
        "model": "5600X",
        "series": "Ryzen",
        "discord_channel": "zen-3",
        "url": "https://www.bestbuy.com/site/amd-ryzen-5-5600x-4th-gen-6-core-12-threads-unlocked-desktop-processor-with-wraith-stealth-cooler/6438943.p?skuId=6438943",
    },
    "6439000": {
        "brand": "AMD",
        "item_number": "6439000",
        "model": "5800X",
        "series": "Ryzen",
        "discord_channel": "zen-3",
        "url": "https://www.bestbuy.com/site/amd-ryzen-7-5800x-4th-gen-8-core-16-threads-unlocked-desktop-processor-without-cooler/6439000.p?skuId=6439000",
    },
    "6438942": {
        "brand": "AMD",
        "item_number": "6438942",
        "model": "5900X",
        "series": "Ryzen",
        "discord_channel": "zen-3",
        "url": "https://www.bestbuy.com/site/amd-ryzen-9-5900x-4th-gen-12-core-24-threads-unlocked-desktop-processor-without-cooler/6438942.p?skuId=6438942",
    },
    "6438941": {
        "brand": "AMD",
        "item_number": "6438941",
        "model": "5950X",
        "series": "Ryzen",
        "discord_channel": "zen-3",
        "url": "https://www.bestbuy.com/site/amd-ryzen-9-5950x-4th-gen-16-core-32-threads-unlocked-desktop-processor-without-cooler/6438941.p?skuId=6438941",
    },
    "6428324": {
        "brand": "Microsoft",
        "item_number": "6428324",
        "model": "Series X",
        "series": "Xbox",
        "discord_channel": "xbox-sx",
        "url": "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324",
    },
    "6430277": {
        "brand": "Microsoft",
        "item_number": "6430277",
        "model": "Series S",
        "series": "Xbox",
        "discord_channel": "xbox-sx",
        "url": "https://www.bestbuy.com/site/microsoft-xbox-series-s-512-gb-all-digital-console-disc-free-gaming-white/6430277.p?skuId=6430277",
    },
    "6430161": {
        "brand": "Sony",
        "item_number": "6430161",
        "model": "Digital Edition",
        "series": "PlayStation 5",
        "discord_channel": "ps5",
        "url": "https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161",
    },
    "6426149": {
        "brand": "Sony",
        "item_number": "6426149",
        "model": "Disc Edition",
        "series": "PlayStation 5",
        "discord_channel": "ps5",
        "url": "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149",
    },
}


######################
#     MISC. URLs     #
######################

RETAILER_ICONS = {
    "Newegg": "https://c1.neweggimages.com/WebResource/Themes/2005/Nest/logo_424x210.png",
    "BestBuy": "https://pisces.bbystatic.com/image2/BestBuy_US/Gallery/BestBuy_Logo_2020-190616.png",
}
