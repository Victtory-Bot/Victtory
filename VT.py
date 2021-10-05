# -*- coding:utf-8 -*-
import asyncio
import discord
import os


# 탭 넣어주는 함수
def list2str(_list, tapping=False):
    if tapping == False:
        return "\n".join(_list)

    else:
        tmp = ""
        for attr in _list:
            tmp += "\t%s\n" % attr
        return tmp

client = discord.Client()

# 토큰입력


# 봇이 켜졌을때
@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("클랜원 합류 기대")
    await client.change_presence(status=discord.Status.online, activity=game)

# 봇이 새로운 메시지를 수신했을때
@client.event
async def on_message(message):
    if message.author.bot:  # 메시지를 보낸사람이 봇
        return None  # 무시
    # 특정 메세지 출력


    if message.content.startswith("!조왕"):
        embed = discord.Embed(
            title="조각난 왕관",
            description="",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615212895009243141/shattered_throne.png"
        )
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!소원"):
        embed = discord.Embed(
            title="소원의 벽",
            description="소원 목록입니다. 키워드를 찾고 그에 맞는 명령어를 입력하세요.",
            color=0xffdc5d
        )
        embed.add_field(
            name="!first",
            value="에테르 열쇠"
        )
        embed.add_field(
            name="!second",
            value="'빛나는 열쇠' 상자"
        )
        embed.add_field(
            name="!third",
            value="'파워 수' 문양"
        )
        embed.add_field(
            name="!fourth",
            value="슈로 치"
        )
        embed.add_field(
            name="!fifth",
            value="모르게스"
        )
        embed.add_field(
            name="!sixth",
            value="금고"
        )
        embed.add_field(
            name="!seventh",
            value="리븐"
        )
        embed.add_field(
            name="!eighth",
            value="음악 재생"
        )
        embed.add_field(
            name="!ninth",
            value="안전장치 빙의"
        )
        embed.add_field(
            name="!tenth",
            value="방랑자 빙의"
        )
        embed.add_field(
            name="!eleventh",
            value="폭죽 놀이"
        )
        embed.add_field(
            name="!twelfth",
            value="가면 축제"
        )
        embed.add_field(
            name="!thirteenth",
            value="페트라의 경주"
        )
        embed.add_field(
            name="!fourteenth",
            value="부패한 알"
        )
        embed.add_field(
            name="!fifteenth",
            value="샤크스 경 빙의"
        )
        await message.channel.send(embed=embed)

        
    if message.content.startswith("!first"):
        embed = discord.Embed(
            title="첫 번째 소원",
            description="욕구를 충족하려는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615219700628062221/wish_1.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!second"):
        embed = discord.Embed(
            title="두 번째 소원",
            description="첫 번째 소원이 실현되는지 실제로 확인하기 위한 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220712692776981/wish_2.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!third"):
        embed = discord.Embed(
            title="세 번째 소원",
            description="다른 사람들에게 성공의 축복을 받으려는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220733861298333/wish_3.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!fourth"):
        embed = discord.Embed(
            title="네 번째 소원",
            description="품격있는 몸짱처럼 보이려는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220749988397058/wish_4.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!fifth"):
        embed = discord.Embed(
            title="다섯 번째 소원",
            description="밝은 미래를 비는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220769344978991/wish_5.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!sixth"):
        embed = discord.Embed(
            title="여섯 번째 소원",
            description="시간을 움직이려는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220785623203849/wish_6.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!seventh"):
        embed = discord.Embed(
            title="일곱 번째 소원",
            description="곤경에 처한 친구를 도우려는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220805466587141/wish_7.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!eighth"):
        embed = discord.Embed(
            title="여덟 번째 소원",
            description="이곳에 영원히 머무르려는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220824227446797/wish_8.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!ninth"):
        embed = discord.Embed(
            title="아홉 번째 소원",
            description="이곳에 영원히 머무르려는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220843370512384/wish_9.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!tenth"):
        embed = discord.Embed(
            title="열 번째 소원",
            description="이곳에 영원히 머무르려는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220863725207680/wish_10.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!eleventh"):
        embed = discord.Embed(
            title="열한 번째 소원",
            description="이곳에 영원히 머무르려는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220884398932088/wish_11.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!twelfth"):
        embed = discord.Embed(
            title="열두 번째 소원",
            description="마음을 열어 새로운 아이디어를 떠올리려는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220904968060948/wish_12.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!thirteenth"):
        embed = discord.Embed(
            title="열세 번째 소원",
            description="욕구를 충족할 방법을 알려는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220927969361930/wish_13.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!fourteenth"):
        embed = discord.Embed(
            title="열네 번째 소원",
            description="사랑과 지지를 받으려는 소원입니다.",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/615220955371012120/wish_14.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!fifteenth"):
        embed = discord.Embed(
            title="열다섯 번째 소원",
            description="이건 마음에 들 거야. ─천의 목소리를 내는 리븐",
            color=0xffdc5d
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!영광"):
        embed = discord.Embed(
            title="시련의 장｜영광 점수",
            description="경쟁 플레이리스트 경기를 통해 획득",
            color=0x532c2c
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/617930183059439636/comp2.png"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!악명"):
        embed = discord.Embed(
            title="갬빗｜악명 점수",
            description="갬빗 클래식/프라임 활동을 통해 획득",
            color=0x2c534a
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/617928041343221762/gambit.png"
        )
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!결단"):
        embed = discord.Embed(
            title="결단의 장소",
            description="",
            color=0x2c534a
        )
        embed.add_field(
            name="오릭스의 화상",
            value="""생존 가방(기관단총)\n__여분의 배급 식량(핸드 캐논)__\n영혼을 갉아먹는 허기(자동 소총)\000\n종말의 날(유탄 발사기)\n필사적인 생존(파동 소총)"""
        )
        embed.add_field(
            name="검",
            value="""고독(보조 무기)\n만약의 경우(검)\n불침번(정찰 소총)\n유일한 생존자(저격총)\n__최후의 승자(산탄총)__"""
        )
        await message.channel.send(embed=embed)  

    if message.content.startswith("!정찰"):
        embed = discord.Embed(
            title="정찰 임무",
            description="",
            color=0xffdc5d
        )
        embed.add_field(
            name="<:patrol_1:615347021141901395> 적 처치",
            value="일정 수의 적을 처치하는 임무",
            inline=False
        )
        embed.add_field(
            name="<:patrol_2:615347020915539969> 아이템 수집",
            value="특정 적으로부터 아이템을 수집하는 임무",
            inline=False
        )
        embed.add_field(
            name="<:patrol_3:615347020932317187> 장소 조사",
            value="특정 장소를 오가며 조사하는 임무",
            inline=False
        )
        embed.add_field(
            name="<:patrol_4:615347020684591106> 사물 조사",
            value="특정 사물을 스캔하는 임무",
            inline=False
        )
        embed.add_field(
            name="<:patrol_5:615347021167198258> 표적 처치",
            value="특정 적을 처치하는 임무",
            inline=False
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!사이트"):
        embed = discord.Embed(
            title="데스티니 가디언즈 커뮤니티",
            description="게임 플레이에 많은 도움이 됩니다. 즐겨찾기 해두세요!",
            color=0xffdc5d
        )
        embed.add_field(
            name="브레이테크｜팬 사이트의 정점",
            value="[braytech.org](https://braytech.org/)",
            inline=False
        )
        embed.add_field(
            name="DIM｜아이템 이동과 로드아웃 지원",
            value="[destinyitemmanager.com](https://destinyitemmanager.com/)",
            inline=False
        )
        embed.add_field(
            name="아머 피커｜스탯 세팅",
            value="[mijago.github.io/D2ArmorPicker](https://mijago.github.io/D2ArmorPicker/)",
            inline=False
        )
        embed.add_field(
            name="리셋데가｜일일·주간 도전 정보",
            value="[d2reset.kr](https://d2reset.kr/)",
            inline=False
        )        
        embed.add_field(
            name="TID｜에버버스 캘린더",
            value="[todayindestiny.com/eververseCalendar](https://www.todayindestiny.com/eververseCalendar)",
            inline=False
        )
        embed.add_field(
            name="건스미스｜총기 정보",
            value="[d2gunsmith.com](https://d2gunsmith.com/)",
            inline=False
        )        
        embed.add_field(
            name="레이드 리포트｜레이드 기록",
            value="[raid.report](https://raid.report/)",
            inline=False
        )        
        embed.add_field(
            name="던전 리포트｜던전 기록",
            value="[dungeon.report](https://dungeon.report/)",
            inline=False
        )        
        embed.add_field(
            name="TRN｜시련의 장 전적",
            value="[destinytracker.com](https://destinytracker.com/)",
            inline=False
        )
        await message.channel.send(embed=embed)        
                
    if message.content.startswith("!캘린더"):
        embed = discord.Embed(
            title="캘린더",
            description="시즌 일정 (Update 21/06/03)",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/849752269808992347/S14_Calendar_KR.png"
        )        
        await message.channel.send(embed=embed)    

    if message.content.startswith("!성배"):
        embed = discord.Embed(
            title="풍요의 성배",
            description="무기 레시피",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/620100022322724894/recipe.png"
        )        
        await message.channel.send(embed=embed)

    if message.content.startswith("!잊구"):
        embed = discord.Embed(
            title="잊혀진 구역",
            description="로테이션 정보",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/894003953019289630/10_lost_sector.png"
        )
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!황혼"):
        embed = discord.Embed(
            title="황혼전",
            description="로테이션 정보",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/894966163589722122/nightfall_rotation_cut.png"
        )
        await message.channel.send(embed=embed)        
               
        
access_token=os.environ["BOT_TOKEN"]
client.run(access_token)
