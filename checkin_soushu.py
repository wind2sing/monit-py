from telethon import TelegramClient, events
import asyncio

# 从 Telegram API 开发者页面获得的 api_id 和 api_hash
api_id = '6879088'
api_hash = '4690f44d3481f070823248c8cce02aa8'

# 登录 Telegram
client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage(from_users='@sosdbot'))
async def handler(event):
    print("Received message from @sosdbot:", event.message.text)
    # 停止监听后续消息，因为我们已经获得了我们想要的回复
    client.disconnect()


async def main():
    # 获取机器人的实体
    bot = await client.get_entity('@sosdbot')

    # 向机器人发送 /chekin 指令
    await client.send_message(bot, '/checkin')

    # 等待机器人的回复，我们设置一个10秒的超时，以防万一机器人没有回应。
    await asyncio.sleep(10)

client.start()
client.loop.run_until_complete(main())
