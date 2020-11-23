import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("상태메시지")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("빈"):
        await message.channel.send("게이")
    if message.content.startswith("bin"):
        await message.channel.send("게이")
    if message.content.startswith("Bin"):
        await message.channel.send("게이")
    if message.content.startswith("빈정보"):
        embed = discord.Embed(color=0xFFC0, title="빈은 게이다",
                              description="빈은 게이입니다")
        embed.set_footer(icon_url=client.user.avatar_url, text='아이스커피 #1611')
        embed.add_field(name='빈', value='성별: `남`\n특징: `세계제일 위대한 게이`')
        await message.channel.send(embed=embed)

client.run("Nzc5MjE1MzU5OTkxMzQ5MjYw.X7dS2g.Thd8I_kwf-k_4duUgERlBYDd53Y")
