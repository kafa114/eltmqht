import discord
import asyncio
import datetime
from captcha.image import ImageCaptcha
import random
import os

client = discord.Client()
@@ -32,11 +34,40 @@ async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith("Ds인증"):
        for i in message.author.roles:
            if i.name == '테스트':
                Image_captcha = ImageCaptcha()
                msg = ""
                a = ""
                for i in range(6):
                    a += str(random.randint(0, 9))

                name = str(message.author.id) + ".png"
                Image_captcha.write(a, name)

                await message.channel.send(file=discord.File(name))

                def check(msg):
                    return msg.author == message.author and msg.channel == message.channel

                try:
                    msg = await client.wait_for("message", timeout=10, check=check)
                except:
                    await message.channel.send("**[ 디스봇 ]** 시간초과입니다.\n- 명령어를 다시 적어 인증을 해주세요.")
                    return

                if msg.content == a:
                    await message.channel.send("**[ 디스봇 ]** 정답입니다.\n- 손님 역할을 지급합니다.")
                else:
                    await message.channel.send("**[ 디스봇 ]** 오답입니다.\n- 명령어를 다시 적어 인증을 해주세요.")
                    break

    if message.content == "Dshelp" or message.content == "Ds도움말":
        Dshelp = discord.Embed(title="**[ 디스봇 ] 도움말**", color=0x8affc6)
        Dshelp.add_field(name="기본명령어", value="- Ds( 명령어 )\n- Dshelp / Ds도움말 : 디스봇 도움말을 보여줍니다.", inline=False)
        Dshelp.set_thumbnail(url="https://media.discordapp.net/attachments/734054856678965292/734055038607163412/d2c8518820b21bd3.png")
        Dshelp.set_footer(text="djs226587#1243 | 디스#5919" , icon_url="https://media.discordapp.net/attachments/734054856678965292/734055038607163412/d2c8518820b21bd3.png")
        Dshelp.set_footer(text="디스#5919 by djs226587#1243" , icon_url="https://media.discordapp.net/attachments/734054856678965292/734055038607163412/d2c8518820b21bd3.png")
        await message.channel.send(embed=Dshelp)

access_token = os.environ["token"]
