import discord
import asyncio
from captcha.image import ImageCaptcha
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["문의 : djs226587#1243", str(user) + "명의 유저들과 함께 하는중입니다.", str(server) + "개의 서버에 참가되어있습니다.", "봇이 오프라인이라면 점검중입니다."]
        for (m) in range(4):
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(10)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith("D-인증"):
        for i in message.author.roles:
            if i.name == '[ 디제이에스 ] 봇테스트':
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
                    await message.channel.send("**[ djs의 gta5 대리 ]** 시간초과입니다.\n- 명령어를 다시 적어 인증을 해주세요.")
                    return

                if msg.content == a:
                    await message.channel.send("**[ djs의 gta5 대리 ]** 정답입니다.\n- 손님 역할을 지급합니다.")
                else:
                    await message.channel.send("**[ djs의 gta5 대리 ]** 오답입니다.\n- 명령어를 다시 적어 인증을 해주세요.")
                    break

    if message.content.startswith("D-출근 관리자"):
        await message.delete()
        for i in message.author.roles:
            if i.name == '[ 디제이에스 ] 관리자':
                cnfrms = discord.Embed(title="**( 봇 ) 디제이에스**", color=0x8affc6)
                cnfrms.add_field(name="출퇴근알림", value=f"관리자 {message.author.mention}님이 출근하셨습니다.", inline=False)
                cnfrms.set_thumbnail(url=message.author.avatar_url)
                cnfrms.set_footer(text="djs의 gta5 대리" , icon_url="https://media.discordapp.net/attachments/711019332477517856/733254434292891709/djsqht.png")
                await client.get_channel(int('728521650022383636')).send(embed=cnfrms)
                break

    if message.content.startswith("D-출근 부관리자"):
        await message.delete()
        for i in message.author.roles:
            if i.name == '[ 디제이에스 ] 부관리자':
                cnfrms1 = discord.Embed(title="**( 봇 ) 디제이에스**", color=0x8affc6)
                cnfrms1.add_field(name="출퇴근알림", value=f"부관리자 {message.author.mention}님이 출근하셨습니다.", inline=False)
                cnfrms1.set_thumbnail(url=message.author.avatar_url)
                cnfrms1.set_footer(text="djs의 gta5 대리" , icon_url="https://media.discordapp.net/attachments/711019332477517856/733254434292891709/djsqht.png")
                await client.get_channel(int('728521650022383636')).send(embed=cnfrms1)
                break
                    
    if message.content.startswith("D-출근 대리인"):
        await message.delete()
        for i in message.author.roles:
            if i.name == '[ 디제이에스 ] 대리인':
                cnfrms2 = discord.Embed(title="**( 봇 ) 디제이에스**", color=0x8affc6)
                cnfrms2.add_field(name="출퇴근알림", value=f"대리인 {message.author.mention}님이 출근하셨습니다.", inline=False)
                cnfrms2.set_thumbnail(url=message.author.avatar_url)
                cnfrms2.set_footer(text="djs의 gta5 대리" , icon_url="https://media.discordapp.net/attachments/711019332477517856/733254434292891709/djsqht.png")
                await client.get_channel(int('728521650022383636')).send(embed=cnfrms2)
                break
                    
    if message.content.startswith("D-출근 임시대리인"):
        await message.delete()
        for i in message.author.roles:
            if i.name == '[ 디제이에스 ] 임시대리인':
                cnfrms3 = discord.Embed(title="**( 봇 ) 디제이에스**", color=0x8affc6)
                cnfrms3.add_field(name="출퇴근알림", value=f"임시대리인 {message.author.mention}님이 출근하셨습니다.", inline=False)
                cnfrms3.set_thumbnail(url=message.author.avatar_url)
                cnfrms3.set_footer(text="djs의 gta5 대리" , icon_url="https://media.discordapp.net/attachments/711019332477517856/733254434292891709/djsqht.png")
                await client.get_channel(int('728521650022383636')).send(embed=cnfrms3)
                break
                    
    if message.content.startswith("D-퇴근 관리자"):
        await message.delete()
        for i in message.author.roles:
            if i.name == '[ 디제이에스 ] 관리자':
                xhlrms = discord.Embed(title="**( 봇 ) 디제이에스**", color=0x8affc6)
                xhlrms.add_field(name="출퇴근알림", value=f"관리자 {message.author.mention}님이 퇴근하셨습니다.", inline=False)
                xhlrms.set_thumbnail(url=message.author.avatar_url)
                xhlrms.set_footer(text="djs의 gta5 대리" , icon_url="https://media.discordapp.net/attachments/711019332477517856/733254434292891709/djsqht.png")
                await client.get_channel(int('728521650022383636')).send(embed=xhlrms)
                break

    if message.content.startswith("D-퇴근 부관리자"):
        await message.delete()
        for i in message.author.roles:
            if i.name == '[ 디제이에스 ] 부관리자':
                xhlrms1 = discord.Embed(title="**( 봇 ) 디제이에스**", color=0x8affc6)
                xhlrms1.add_field(name="출퇴근알림", value=f"부관리자 {message.author.mention}님이 퇴근하셨습니다.", inline=False)
                xhlrms1.set_thumbnail(url=message.author.avatar_url)
                xhlrms1.set_footer(text="djs의 gta5 대리" , icon_url="https://media.discordapp.net/attachments/711019332477517856/733254434292891709/djsqht.png")
                await client.get_channel(int('728521650022383636')).send(embed=xhlrms1)
                break
                    
    if message.content.startswith("D-퇴근 대리인"):
        await message.delete()
        for i in message.author.roles:
            if i.name == '[ 디제이에스 ] 대리인':
                xhlrms2 = discord.Embed(title="**( 봇 ) 디제이에스**", color=0x8affc6)
                xhlrms2.add_field(name="출퇴근알림", value=f"대리인 {message.author.mention}님이 퇴근하셨습니다.", inline=False)
                xhlrms2.set_thumbnail(url=message.author.avatar_url)
                xhlrms2.set_footer(text="djs의 gta5 대리" , icon_url="https://media.discordapp.net/attachments/711019332477517856/733254434292891709/djsqht.png")
                await client.get_channel(int('728521650022383636')).send(embed=xhlrms2)
                break
                    
    if message.content.startswith("D-퇴근 임시대리인"):
        await message.delete()
        for i in message.author.roles:
            if i.name == '[ 디제이에스 ] 임시대리인':
                xhlrms3 = discord.Embed(title="**( 봇 ) 디제이에스**", color=0x8affc6)
                xhlrms3.add_field(name="출퇴근알림", value=f"임시대리인 {message.author.mention}님이 퇴근하셨습니다.", inline=False)
                xhlrms3.set_thumbnail(url=message.author.avatar_url)
                xhlrms3.set_footer(text="djs의 gta5 대리" , icon_url="https://media.discordapp.net/attachments/711019332477517856/733254434292891709/djsqht.png")
                await client.get_channel(int('728521650022383636')).send(embed=xhlrms3)
                break
                    
access_token = os.environ["token"]
client.run(access_token)
