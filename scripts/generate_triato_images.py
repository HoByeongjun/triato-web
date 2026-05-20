from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import math, random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public' / 'images' / 'generated'
OUT.mkdir(parents=True, exist_ok=True)
PUBLIC = ROOT / 'public'
FONT_KO = '/System/Library/Fonts/AppleSDGothicNeo.ttc'
FONT_EN = '/System/Library/Fonts/SFNS.ttf'

def font(size, weight=0):
    # TTC index is ignored by many builds; AppleSDGothic renders Korean reliably.
    try:
        return ImageFont.truetype(FONT_KO, size=size, index=weight)
    except Exception:
        return ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', size=size)

def rgba(hexstr, a=255):
    hexstr = hexstr.lstrip('#')
    return tuple(int(hexstr[i:i+2], 16) for i in (0,2,4)) + (a,)

def rounded_rect(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def gradient(size, top, bottom):
    w,h=size
    img=Image.new('RGBA', size)
    pix=img.load()
    for y in range(h):
        t=y/(h-1)
        col=tuple(int(top[i]*(1-t)+bottom[i]*t) for i in range(4))
        for x in range(w): pix[x,y]=col
    return img

def add_glow(base, cx, cy, color, radius, strength=1.0):
    glow=Image.new('RGBA', base.size, (0,0,0,0))
    gd=ImageDraw.Draw(glow)
    for i in range(16,0,-1):
        r=radius*i/16
        a=int(color[3]*(i/16)**2*strength)
        gd.ellipse((cx-r,cy-r,cx+r,cy+r), fill=color[:3]+(a,))
    base.alpha_composite(glow.filter(ImageFilter.GaussianBlur(radius/6)))

def draw_logo_word(draw, x, y, fill=(255,255,255,255), size=44):
    draw.text((x,y), 'TRIATO', font=font(size, 0), fill=fill, anchor='la')

def hero_image():
    W,H=1600,1000
    img=gradient((W,H), (3,5,8,255), (0,0,0,255))
    draw=ImageDraw.Draw(img)
    # studio glows
    add_glow(img, 1120, 230, (0,200,232,170), 420, .55)
    add_glow(img, 420, 300, (15,45,120,150), 520, .42)
    # subtle grid
    for x in range(0,W,96): draw.line((x,0,x,H), fill=(255,255,255,10), width=1)
    for y in range(0,H,96): draw.line((0,y,W,y), fill=(255,255,255,8), width=1)
    # central glass slab
    slab=(520,185,1420,785)
    rounded_rect(draw, slab, 54, (255,255,255,24), (255,255,255,54), 2)
    # top bar
    rounded_rect(draw, (560,225,1380,286), 26, (255,255,255,24), (255,255,255,34), 1)
    for i,c in enumerate([(255,95,87,180),(255,190,70,180),(45,210,95,180)]):
        draw.ellipse((590+i*28,247,606+i*28,263), fill=c)
    draw.text((1345,255),'MISSION CONTROL', font=font(18), fill=(245,245,247,105), anchor='ra')
    # command card
    rounded_rect(draw, (590,330,1120,500), 34, (245,245,247,245), None)
    draw.text((625,365),'ACTIVE BRIEF', font=font(19), fill=(0,113,227,255))
    draw.text((625,405),'AI 팀이 문제를\n서비스로 압축합니다.', font=font(48), fill=(12,16,24,255), spacing=2)
    # stats cards
    for i,(title,val) in enumerate([('AGENTS','12'),('APPROVAL','100%'),('LAUNCH','READY')]):
        x=1160; y=330+i*112
        rounded_rect(draw,(x,y,x+190,y+88),24,(0,0,0,90),(255,255,255,24),1)
        draw.text((x+20,y+20),title,font=font(16),fill=(0,200,232,210))
        draw.text((x+20,y+43),val,font=font(31),fill=(255,255,255,230))
    # flow nodes
    points=[(640,620),(840,620),(1040,620),(1240,620)]
    for a,b in zip(points, points[1:]): draw.line((a[0]+62,a[1],b[0]-62,b[1]), fill=(0,200,232,95), width=4)
    for idx,(x,y) in enumerate(points):
        fill=(0,200,232,255) if idx==0 else (255,255,255,22)
        txt=(4,16,20,255) if idx==0 else (245,245,247,185)
        rounded_rect(draw,(x-62,y-28,x+62,y+28),28,fill,(255,255,255,44),1)
        draw.text((x,y-11),['PLAN','BUILD','REVIEW','SHIP'][idx],font=font(17),fill=txt,anchor='ma')
    # left title space
    draw_logo_word(draw, 115, 115, (255,255,255,235), 54)
    draw.text((115,210),'AI Product Studio',font=font(32),fill=(0,200,232,235))
    draw.text((115,266),'Designed for\nfast execution.',font=font(86),fill=(255,255,255,240),spacing=-8)
    return img

def service_image():
    W,H=1400,900
    img=gradient((W,H),(250,250,252,255),(235,241,247,255))
    draw=ImageDraw.Draw(img)
    add_glow(img, 1050, 210, (0,200,232,90), 370, .55)
    add_glow(img, 350, 640, (15,45,120,75), 390, .35)
    # floating cards
    cards=[(150,145,600,370,'CUSTOM BUILD','웹 · 앱 · 대시보드'),(720,105,1250,430,'AI OPS','에이전트 워크플로우'),(275,490,760,750,'AUTOMATION','반복 업무 연결'),(840,520,1190,735,'LAUNCH','배포와 운영')]
    for i,(x1,y1,x2,y2,label,title) in enumerate(cards):
        shadow=Image.new('RGBA', img.size,(0,0,0,0)); sd=ImageDraw.Draw(shadow)
        rounded_rect(sd,(x1+10,y1+18,x2+10,y2+18),34,(15,45,120,22),None)
        img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(18)))
        rounded_rect(draw,(x1,y1,x2,y2),34,(255,255,255,238),(15,45,120,25),1)
        draw.text((x1+34,y1+34),label,font=font(18),fill=(0,113,227,230))
        draw.text((x1+34,y1+82),title,font=font(38),fill=(29,29,31,245))
        # bars / nodes
        for j in range(3):
            yy=y1+145+j*34
            rounded_rect(draw,(x1+34,yy,x2-44,yy+12),6,(15,45,120,22),None)
            rounded_rect(draw,(x1+34,yy,x1+34+(x2-x1-120)*(0.42+0.17*j),yy+12),6,(0,200,232,130),None)
    # connection lines
    for (x1,y1),(x2,y2) in [((600,300),(720,240)),((610,610),(840,610)),((760,660),(880,430))]:
        draw.line((x1,y1,x2,y2), fill=(0,200,232,95), width=3)
    draw.text((90,810),'TRIATO',font=font(36),fill=(15,45,120,170))
    return img

def og_image(square=False):
    W,H=(1200,1200) if square else (1200,630)
    img=gradient((W,H),(1,3,6,255),(0,0,0,255))
    draw=ImageDraw.Draw(img)
    add_glow(img, int(W*.72), int(H*.32), (0,200,232,180), int(W*.34), .65)
    add_glow(img, int(W*.25), int(H*.70), (15,45,120,145), int(W*.36), .5)
    # core object
    cx,cy=int(W*.72),int(H*.5)
    for r,a in [(210,30),(150,45),(92,80)]:
        draw.ellipse((cx-r,cy-r,cx+r,cy+r), outline=(0,200,232,a), width=2)
    rounded_rect(draw,(cx-170,cy-92,cx+170,cy+92),36,(255,255,255,22),(255,255,255,58),2)
    draw.text((cx,cy-31),'TRIATO',font=font(44),fill=(255,255,255,230),anchor='ma')
    draw.text((cx,cy+25),'MISSION CONTROL',font=font(18),fill=(0,200,232,210),anchor='ma')
    # copy
    draw.text((72,74),'TRIATO',font=font(42),fill=(255,255,255,230))
    headline='행동이\n시작되는 곳' if square else '행동이 시작되는 곳'
    draw.text((72, H*.34),headline,font=font(86 if not square else 96),fill=(255,255,255,245),spacing=-8)
    draw.text((76, H*.34 + (112 if not square else 240)),'AI 팀 · 기획부터 운영까지',font=font(34),fill=(0,200,232,235))
    return img

assets = {
    'triato-hero-generated.png': hero_image(),
    'triato-service-generated.png': service_image(),
    'triato-og-generated.png': og_image(False),
    'triato-og-square-generated.png': og_image(True),
}
for name,img in assets.items():
    path=OUT/name
    img.convert('RGB').save(path, quality=94, optimize=True)
    print(path)
# overwrite social images with generated final comps
assets['triato-og-generated.png'].convert('RGB').save(PUBLIC/'og-image.png', quality=94, optimize=True)
assets['triato-og-generated.png'].convert('RGB').save(PUBLIC/'twitter-image.png', quality=94, optimize=True)
assets['triato-og-square-generated.png'].convert('RGB').save(PUBLIC/'og-square.png', quality=94, optimize=True)
print(PUBLIC/'og-image.png')
print(PUBLIC/'twitter-image.png')
print(PUBLIC/'og-square.png')
