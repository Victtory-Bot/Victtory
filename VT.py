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
    game = discord.Game("클랜원 감우시")
    await client.change_presence(status=discord.Status.online, activity=game)

# 봇이 새로운 메시지를 수신했을때
@client.event
async def on_message(message):
    if message.author.bot:  # 메시지를 보낸사람이 봇
        return None  # 무시
    # 특정 메세지 출력

    if message.content.startswith("!빅또리"):
        embed = discord.Embed(
            title="클랜소개",
            description="햄보카자 아프지망고(KT위즈랑 노상관)",
            color=0xffdc5d
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/600270081729101824/615203635286245386/banner.png"
        )
        embed.add_field(
            name="생성일",
            value="2018/10/13"
        )
        embed.add_field(
            name="인원",
            value="38명"
        )
        embed.add_field(
            name="시즌레벨",
            value="Lv.6"
        )
        embed.add_field(
            name="관리자",
            value="빅깨#3412, 감우#3634<:battle_net:615300518847315971>"
        )
        embed.add_field(
            name="디스코드",
            value="Click [link](https://discord.gg/htZYs4r)"
        )
        embed.add_field(
            name="오픈채팅",
            value="Click [link](https://open.kakao.com/o/g4Jv7Ywb)"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!주간"):
        embed = discord.Embed(
            title="2019/09/25-10/01",
            description="- 시즌 마지막 주\n- 용맹 · 악명 부스트",
            color=0xffdc5d
        )
        embed.set_author(
            name="주간 리셋",
            url="",
            icon_url=""
        )
        embed.add_field(
            name="화약고",
            value="화성"
        )
        embed.add_field(
            name="꿈의 도시 저주",
            value="1주차"
        )
        embed.add_field(
            name="승천",
            value="에실라의 정원"
        )
        embed.add_field(
            name="시련의 장",
            value="아수라장"
        )
        embed.add_field(
            name="거미 현상금",
            value="""피투성이 대검\n(이오)"""
        )
        embed.add_field(
            name="확대 프로토콜",
            value="IKELOS_SR_v1.0.1"
        )
        embed.add_field(
            name="영웅 전시장｜결단의 장소",
            value="아루낙(오우거)｜오릭스의 화상"
        )
        embed.add_field(
            name="황혼전",
            value="""<:Legendary:615302557535043635> 긴 작별 - 통찰의 종착지\n<:Exotic:615302557312614523> 트리크로마티카 - 뒤집어진 첨탑\n<:Legendary:615302557535043635> 벌레 신 현신 - 수천 명의 의지"""
        )
        embed.add_field(
            name="레이드",
            value="""슬픔의 왕관: 완전한 승리\n과거의 고통: 하나는 모두를 위해….\n마지막 소원: 기억의 힘
            \n리바이어던\n┖ 순서  <:Baths_challenge:616005868995084308><:Gauntlet:615302624438255723><:Dog:615302624329072700><:Throne:615302624027082776>\n┖ 고급  <:Modifier_3:618557788553084970>프리즘 + 핸드 캐논/저격총/아무거나"""
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!조왕"):
        embed = discord.Embed(
            title="조각난 왕관",
            description="꿈의 도시 저주 3주차에만 입장할 수 있습니다.",
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

    if message.content.startswith("!영웅"):
        embed = discord.Embed(
            title="",
            description="",
            color=0xffdc5d
        )
        embed.set_author(
            name="일일 영웅 이야기｜Click here",
            url="http://www.inven.co.kr/board/destinyguardians/5316/3768",
            icon_url=""
        )
        embed.add_field(
            name="임무",
            value="\n".join(["1AU", "강탈", "경멸자", "고리", "관문", "귀향", "기술자", "깊이 숨겨진 것", "마지막 부름", "__무시무시한 시험 ★__", "무한 그 너머에", "보복", "분노", "불꽃", "__불패 ★__", "선택받은 자", "순례", "식스", "신성 모독", "__얼음과 그림자 ★__", "연소", "오메가", "유구무언", "유토피아", "작별", "절도", "조류", "출입구", "평원의 노래", "행성 밖 회복", "희망"])
        )
        embed.add_field(
            name="소요시간",
            value="\n".join(["13 mins", "6 mins", "13 mins", "7 mins", "6 mins", "-", "12 mins", "7 mins", "15 mins", "__5 mins__", "11 mins", "11 mins", "8 mins", "-", "__4 mins__", "9 mins", "6 mins", "10 mins", "6 mins", "__3 mins__", "7 mins", "12 mins", "12 mins", "8 mins", "-", "7 mins", "10 mins", "6 mins", "9 mins", "7 mins", "7 mins"])
        )
        embed.add_field(
            name="세계기록",
            value="\n".join(["5m 23s", "3m 17s", "4m 29s", "3m 17s", "2m 58s", "-", "5m 32s", "3m 22s", "9m 02s", "__2m 47s__", "6m 28s", "3m 48s", "4m 25s", "-", "__1m 59s__", "4m 32s", "3m 37s", "4m 02s", "3m 28s", "__1m 38s__", "3m 11s", "6m 37s", "4m 33s", "4m 49s", "-", "3m 13s", "2m 59s", "-", "6m 06s", "3m 10s", "2m 52s"])
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
            name="이슈타르 컬렉티브｜D1부터 D2까지 존재하는 모든 로어",
            value="[ishtar-collective.net](https://www.ishtar-collective.net/)",
            inline=False
        )
        embed.add_field(
            name="체크리스트｜일일·주간 도전 현황",
            value="[d2checklist.com](https://www.d2checklist.com/home)",
            inline=False
        )
        embed.add_field(
            name="레이드 리포트｜레이드 기록",
            value="[raid.report](https://raid.report/)",
            inline=False
        )
        embed.add_field(
            name="트래커 네트워크｜시련의 장 전적",
            value="[destinytracker.com](https://destinytracker.com/)",
            inline=False
        )
        embed.add_field(
            name="워마인드｜갬빗 전적",
            value="[warmind.io](https://warmind.io/gambit)",
            inline=False
        )
        embed.add_field(
            name="로우라이뎁｜상호 작용 가능한 모든 사물·지식의 위치",
            value="[lowlidev.com.au/destiny](https://lowlidev.com.au/destiny/)",
            inline=False
        )
        embed.add_field(
            name="라이트지지｜인게임에선 알 수 없는 무기의 히든스탯까지",
            value="[light.gg](https://www.light.gg/)",
            inline=False
        )
        embed.add_field(
            name="히트맵｜월별·일별·활동별 플레이 타임",
            value="[chrisfried.github.io/secret-scrublandeux](https://chrisfried.github.io/secret-scrublandeux/)",
            inline=False
        )
        embed.add_field(
            name="데스티니 아이템 매니저(DIM)｜아이템 이동과 로드아웃 지원",
            value="[destinyitemmanager.com](https://destinyitemmanager.com/)",
            inline=False
        )
        embed.add_field(
            name="데스티니 가디언즈 Teams｜대규모 디스코드 커뮤니티",
            value="[discord.gg/uX4WtSC](https://discord.gg/uX4WtSC)",
            inline=False
        )
        embed.add_field(
            name="번지넷｜공식 홈페이지",
            value="[bungie.net/ko](https://www.bungie.net/ko)",
            inline=False
        )
        await message.channel.send(embed=embed)        
        
    if message.content.startswith("!도램쥐"):
        embed = discord.Embed(
            title="도램쥐",
            description="""종합 게임 스트리머\n방송시간: 수, 목 저녁 9시 이후""",
            color=0xffdc5d
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/615212078453751818/624262658547384336/drg.png"
        )
        embed.add_field(
            name="Twitch",
            value="[팔로우](https://www.twitch.tv/s2doram_g)"
        )
        embed.add_field(
            name="YouTube",
            value="[구독](https://www.youtube.com/channel/UC5EsXpxVE_4KpBQXt6CE1Bg)"
        )
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!고웅"):
        embed = discord.Embed(
            title="고웅",
            description="""종합 게임 스트리머""",
            color=0xffdc5d
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/616026203299643435/616072719275917313/Go_woong.png"
        )
        embed.add_field(
            name="Twitch",
            value="[팔로우](https://www.twitch.tv/gowoong)"
        )
        embed.add_field(
            name="YouTube",
            value="[구독](https://www.youtube.com/channel/UCKvDmMKEYTrKDXCRsxcVQaw)"
        )        
        embed.add_field(
            name="Discord",
            value="[초대](https://discord.gg/MNGnYAq)"
        )
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!루엘"):
        embed = discord.Embed(
            title="루엘",
            description="종합 게임 스트리머",
            color=0xffdc5d
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/615212078453751818/616738998555115552/luel.png"
        )
        embed.add_field(
            name="Twitch",
            value="[팔로우](https://www.twitch.tv/lc_luel)"
        )        
        embed.add_field(
            name="Youtube",
            value="[구독](https://www.youtube.com/channel/UCShgH1SIEg44x0YonQpHeGQ)"
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!이리구"):
        embed = discord.Embed(
            title="이리구",
            description="데스티니 가디언즈 유튜버",
            color=0xffdc5d
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/615212078453751818/623541077281865748/049515676baad64f.png"
        )
        embed.add_field(
            name="Youtube",
            value="[구독](https://www.youtube.com/channel/UCui7NEHSbLiblR3Ttd8fVlw)"
        )
        await message.channel.send(embed=embed)        

    if message.content.startswith("!핀치"):
        embed = discord.Embed(
            title="핀치",
            description="배틀그라운드 스트리머",
            color=0xffdc5d
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/615212078453751818/623554300140060682/pinch.jpg"
        )
        embed.add_field(
            name="Twitch",
            value="[팔로우](https://www.twitch.tv/pinchtv_)"
        )                                  
        embed.add_field(
            name="Youtube",
            value="[구독](https://www.youtube.com/channel/UCZq4YyjDXSLbOQB9XLFT1Pg)"
        )
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!비버"):
        embed = discord.Embed(
            title="어쨌든술집",
            description="""서울 영등포구 당산로47길 12 1층\n\n· 평일 19:00 - 02:00\n· 주말 19:00 - 02:00\n· 일요일 휴무\n\n???: 김가무 지인 할인 어림두 없지ㅋ""",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/619045666789916712/bb.png"
        )        
        await message.channel.send(embed=embed)         
        
    if message.content.startswith("!캘린더"):
        embed = discord.Embed(
            title="캘린더",
            description="시즌 일정",
            color=0xffdc5d
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/615212078453751818/626117742944059392/Destiny_SoU_Calendar_KR.png"
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

    if message.content.startswith("!화면공유"):
        embed = discord.Embed(
            title="화면 공유 링크",
            description="음성 채널에 입장한 뒤, 채널 이름과 일치하는 링크를 클릭하세요.",
            color=0xffdc5d
        )
        embed.add_field(
            name="스쿼드",
            value="[스쿼드 채널에서 화면 공유](http://discordapp.com/channels/333653458681069578/610331274544021505)"
        )
        embed.add_field(
            name="화력팀",
            value="[화력팀 채널에서 화면 공유](http://discordapp.com/channels/333653458681069578/564580117720858625)"
        )
        embed.add_field(
            name="만담방",
            value="[만담방 채널에서 화면 공유](http://discordapp.com/channels/333653458681069578/582517225412624385)"
        )
        embed.add_field(
            name="분분",
            value="[분분 채널에서 화면 공유](http://discordapp.com/channels/333653458681069578/619032688564764702)"
        )
        await message.channel.send(embed=embed)        

    if message.content.startswith("!계정이관"):
        embed = discord.Embed(
            title="계정 이관",
            description="""10월 2일, 데스티니 가디언즈 PC가 Steam으로 이동합니다. 아래 링크를 눌러 이관 신청을 완료해주세요.""",
            color=0xffdc5d
        )
        embed.add_field(
            name="PC 이동",
            value="[https://www.bungie.net/7/ko/PCMove](https://www.bungie.net/7/ko/PCMove)"
        )
        await message.channel.send(embed=embed)      
        
access_token=os.environ["BOT_TOKEN"]
client.run(access_token)
