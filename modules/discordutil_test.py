from discordutil import DiscordEmbed
from discordutil import WebhookMessage
from discordutil import DiscordWebhook
import discordutil
import asyncio

async def main():

    webhook_worker = asyncio.create_task(discordutil.webhook_worker_task())
    embed = DiscordEmbed()

    embed.setTitle("woweeee")
    embed.setDescription("how cool")
    embed.setUrl("www.google.com")
    embed.applyTimestamp(True)
    embed.setColor(0)
    embed.setFooter("Look at this", icon="www.coolimage.com", proxy="proxyurl.net")
    embed.setImage(url="anotherimage.wow", proxy="lookaproxy.net", width=64, height=64)
    embed.setThumbnail(url="thumbrl.url", proxy="proxwow.cool", width=128, height=128)
    embed.setVideo(url="https://www.youtube.com/watch?v=jNQXAC9IVRw", width=426, height=240)
    embed.setProvider(name="the provider", url="iamtheprovider.provide")
    embed.setAuthor(name="the author", url="iwrotethis.com", icon="wowanimage.net", proxy="anotherproxy.net")
    embed.addField("field1", "Hello I am field 1", True)
    embed.addField("field2", "hello I am field 2", False)

    embedData = embed.getData()

    print(str(embed))

    message = WebhookMessage()

    message.setContent("Wowee a webhook message")
    message.setUsername("User 1")
    message.setAvatar("avatar.cool")
    message.setTTS(False)
    message.addEmbed(embed)
   
    print(str(message))

    for x in range(100):
        test_embed = DiscordEmbed()
        test_embed.setTitle("This is a test")
        test_embed.setDescription("Hello World! Message " + str(x) + " of 100")
    
        msg = WebhookMessage()
        msg.addEmbed(test_embed)
        msg.setContent("Testing...")
    
        hook = DiscordWebhook("https://discordapp.com/api/webhooks/789662307780788244/YlJZ7qw4gX9-0SHgzRgZtr1iqhRQAcMtmtckBwBbwXU0oCxDRdKBtzgagK-eyCfX8YGK")
        hook.setContent(msg)
        await discordutil.sending_queue.put(hook)
    await asyncio.sleep(100)

if __name__ == "__main__":
    asyncio.run(main())
