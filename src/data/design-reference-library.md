# Design Reference Library for AI Designer (이서연)

TRIATO 디자인 에이전트 전용 레퍼런스. 모든 디자인 작업 시 이 문서를 참조할 것.
"AI가 만든 것 같은" 느낌을 없애고, 사람이 심혈을 기울여 만든 디자인을 목표로 한다.

---

## 1. Top 20 IT/AI Startup Websites

### Tier S: 디자인 완성도 최상위

**1. Linear** — linear.app
- 핵심 강점: 극도로 절제된 다크 UI. 모든 요소가 "필요한 것만" 존재
- 팔레트: `#000000` 배경, `#FFFFFF` 텍스트, 보라 액센트 `#5E6AD2`, 미묘한 그레이 `#8A8F98`
- 배울 점: 카드에 1px border `rgba(255,255,255,0.05)` + subtle glow로 depth 표현. 배경색 차이만으로 섹션 구분 (divider 없음)

**2. Vercel** — vercel.com
- 핵심 강점: 흑백 미니멀리즘의 정석. 타이포그래피만으로 hierarchy 완성
- 팔레트: `#000000`, `#FFFFFF`, `#888888`, 가끔 gradient `linear-gradient(to right, #00DFD8, #007CF0, #7928CA, #FF0080)`
- 배울 점: Hero에서 h1이 56-72px, subtext가 20px에 `#888`으로 명확한 위계. 여백이 콘텐츠만큼 중요하게 쓰임

**3. Stripe** — stripe.com
- 핵심 강점: 복잡한 금융 제품을 시각적으로 우아하게 설명. 메쉬 그라디언트 배경의 교과서
- 팔레트: `#635BFF` 메인, `#0A2540` 다크, `#00D4AA` 보조, `#FBFCFE` 라이트 배경
- 배울 점: 코드 블록과 UI 데모를 인라인으로 보여주는 방식. gradient mesh가 배경에서 은은하게 움직임

**4. Anthropic** — anthropic.com
- 핵심 강점: 학술적 신뢰감 + 현대적 미니멀. 과하지 않은 세리프 사용
- 팔레트: `#191919` 텍스트, `#CC785C` 시그니처 테라코타, `#FFFFFF` 배경, `#D4A574` 웜톤
- 배울 점: serif + sans-serif 혼합 타이포. heading에 serif, body에 sans-serif로 품격 표현

**5. Figma** — figma.com
- 핵심 강점: 컬러풀하면서도 정돈된 느낌. 인터랙티브 데모가 페이지 자체
- 팔레트: `#0ACF83` 그린, `#A259FF` 퍼플, `#F24E1E` 레드, `#FF7262`, `#1ABCFE`
- 배울 점: 다색 팔레트를 써도 각 색이 특정 기능/의미에 1:1 매핑되어 혼란 없음

### Tier A: 특정 분야 최고 수준

**6. Notion** — notion.so
- 강점: 일러스트레이션과 UI 스크린샷의 조화. 친근하면서 프로페셔널
- 팔레트: `#FFFFFF`, `#000000`, `#2EAADC` 블루, 따뜻한 아이보리 `#FFFDF5`
- 배울 점: hand-drawn 느낌 일러스트가 차갑지 않은 SaaS 이미지를 만듦

**7. Supabase** — supabase.com
- 강점: 다크 테마에서 네온 그린 액센트의 완벽한 사용
- 팔레트: `#1C1C1C` 배경, `#3ECF8E` 그린 액센트, `#6EE7B7` 밝은 그린, `#EDEDED`
- 배울 점: 코드 에디터 스타일의 hero. 개발자 타겟 사이트의 모범. 그린 하나로 전체 아이덴티티 구축

**8. Resend** — resend.com
- 강점: Vercel 스타일 미니멀 + 코드 중심 데모. 극단적으로 깔끔한 레이아웃
- 팔레트: `#000000`, `#FFFFFF`, `#EEEEEE` 보더, 미니멀 블루 `#3B82F6`
- 배울 점: 기능 설명에 실제 코드 snippet을 hero 급으로 크게 배치. 개발자 제품의 정석

**9. Raycast** — raycast.com
- 강점: 제품 UI 자체를 웹사이트 디자인 요소로 활용. glassmorphism 적절한 사용
- 팔레트: `#131315` 배경, `#FF6363` 레드 액센트, gradient purple-pink
- 배울 점: 실제 앱 인터페이스를 3D perspective로 보여주는 hero. `backdrop-filter: blur(20px)`

**10. Arc** — arc.net
- 강점: 대담한 컬러 사용과 유기적인 곡선. 브라우저답게 "열린" 느낌
- 팔레트: 계절/테마별로 바뀜. 핵심은 saturated 파스텔 — `#FC5C7D`, `#6A82FB`, 옐로우 톤
- 배울 점: 정형화된 그리드를 벗어난 비대칭 레이아웃이 오히려 기억에 남음

**11. Lemon Squeezy** — lemonsqueezy.com
- 강점: 일러스트 + 3D 요소. 친근하고 재미있는 SaaS 디자인
- 팔레트: `#7047EB` 퍼플, `#FFC233` 옐로우, `#FFFFFF`, 부드러운 그래디언트
- 배울 점: 3D 오브젝트와 2D UI가 자연스럽게 공존하는 방법

**12. Cal.com** — cal.com
- 강점: 오픈소스 프로젝트의 투명함을 디자인으로 표현. 깔끔한 SaaS 레이아웃
- 팔레트: `#111827` 다크, `#FFFFFF`, `#292929`, 액센트 없이도 성립하는 모노톤
- 배울 점: 제품 스크린샷을 `border-radius: 12px` + 그림자로 떠있는 느낌 연출

**13. Clerk** — clerk.com
- 강점: Auth UI 컴포넌트를 제품 데모이자 디자인 요소로 활용
- 팔레트: `#1F0256` 딥 퍼플, `#6C47FF` 밝은 퍼플, `#F5F5F5`, `#FFFFFF`
- 배울 점: 라이브 데모 임베드가 천 마디 설명을 대체

**14. PlanetScale** — planetscale.com
- 강점: DB 제품인데 디자인이 프리미엄. 기술 브랜딩의 모범
- 팔레트: `#000000`, `#FFFFFF`, 오렌지 `#FF9900`, 그래디언트 라인아트
- 배울 점: 와이어프레임 스타일의 기하학적 라인이 배경에서 depth 연출

**15. Neon** — neon.tech
- 강점: 이름에 맞는 네온 glow 효과. 다크 테마 + glow의 정석
- 팔레트: `#0A0A0A` 배경, `#00E699` 네온 그린, `#7B61FF` 퍼플, glow 효과 `box-shadow: 0 0 40px rgba(0,230,153,0.3)`
- 배울 점: text에 `text-shadow: 0 0 20px rgba(0,230,153,0.5)` 적용하여 네온 사인 느낌

**16. Railway** — railway.app
- 강점: 컬러풀한 그래디언트가 개성을 만듦. 개발 도구인데 재미있음
- 팔레트: `#13111A` 배경, 멀티컬러 그래디언트 `#C049FF → #4CC9F0 → #43E97B`
- 배울 점: 배포 프로세스를 시각적 다이어그램으로 설명하는 방식

**17. Fly.io** — fly.io
- 강점: 개발자 친화적인 터미널 스타일 미학. 텍스트 중심 디자인
- 팔레트: `#24175A` 딥 퍼플, `#7B3FE4` 퍼플, `#FFFFFF`, 따뜻한 톤 믹스
- 배울 점: CLI output 스타일을 시각적 요소로 활용. 코드가 곧 디자인

**18. Turso** — turso.tech
- 강점: 엣지 DB라는 기술적 콘셉트를 시각적으로 잘 표현
- 팔레트: `#0B1120` 다크, `#4FF8D2` 민트 액센트, `#FFFFFF`
- 배울 점: 글로벌 네트워크를 지도/노드 시각화로 표현하는 hero

**19. Convex** — convex.dev
- 강점: 리액티브 데이터의 "실시간" 느낌을 애니메이션으로 전달
- 팔레트: `#121212` 배경, `#F3B01C` 옐로우 액센트, `#EE5533` 오렌지
- 배울 점: 데이터 흐름을 시각화한 animated diagram이 제품 이해를 돕는 방법

**20. WorkOS** — workos.com
- 강점: 엔터프라이즈 타겟인데 모던한 디자인. B2B도 아름다울 수 있음
- 팔레트: `#000000`, `#FFFFFF`, `#6C6C6C`, 민트 `#68DBAF` 액센트
- 배울 점: SSO/SAML 같은 지루한 기능을 깔끔한 UI 미리보기로 매력적으로 표현

---

## 2. Component-Level Best Practices

### Hero Section

**Great:**
- h1: 48-72px, font-weight 600-700, letter-spacing `-0.02em` (약간 좁혀야 고급스러움)
- 서브텍스트: 18-22px, `#888888` 또는 `rgba(255,255,255,0.6)`, line-height 1.6, 최대 2줄
- CTA 버튼: h1 아래 32-48px 간격. Primary는 배경색 + 흰 텍스트, Secondary는 ghost 스타일
- 전체 섹션 패딩: 상하 120-160px. **좁으면 싸구려 느낌**
- 배경: 단색 또는 극도로 미묘한 gradient/noise texture

**Mediocre (피할 것):**
- h1과 서브텍스트 크기 차이가 적음 (예: 36px / 24px)
- CTA 버튼 2-3개가 나란히 있는데 크기/색이 비슷
- 배경에 stock photo를 깔아놓은 것
- 섹션 높이가 화면의 60% 미만

### Navigation Bar

**Great:**
- 높이: 64px. 스크롤 시 `backdrop-filter: blur(12px)` + `background: rgba(0,0,0,0.8)` (Linear 방식)
- 로고 왼쪽, 메뉴 중앙, CTA 오른쪽 — 이 3분할이 기본
- 스크롤 시 `border-bottom: 1px solid rgba(255,255,255,0.1)` 추가
- 모바일: 햄버거 아이콘 터치영역 44px 이상. 메뉴 오픈 시 전체화면 오버레이
- 폰트: 14-15px, medium weight, letter-spacing `0.01em`

**Mediocre:**
- 스크롤해도 아무 변화 없는 static nav
- 메뉴 항목이 7개 이상
- 드롭다운이 hover로만 작동 (모바일 대응 불가)

### Feature/Service Cards

**Great:**
- 그리드: 3열 기본, gap `24-32px`. 카드 패딩 `32-40px`
- 아이콘: 32-40px, 커스텀 또는 Phosphor/Lucide. **절대 FontAwesome 기본 아이콘 쓰지 말 것**
- 카드 배경: 메인 배경보다 1-2단계 밝게. `#0A0A0A` 배경이면 카드는 `#141414`
- 제목: 20-24px semibold, 설명: 15-16px regular `#999`
- hover: `translateY(-2px)` + 그림자 약간 증가. 과하면 안 됨
- border: `1px solid rgba(255,255,255,0.06)` — 있을까 말까 하게

**Mediocre:**
- 모든 카드에 두꺼운 그림자 `box-shadow: 0 4px 20px rgba(0,0,0,0.3)`
- 아이콘이 전부 같은 색, 같은 스타일이 아닌 경우
- 카드 안 콘텐츠가 중앙 정렬 (좌측 정렬이 가독성 높음)

### Process / How It Works

**Great:**
- 스텝 넘버: 작게 (14px), `#555` 색상 또는 accent color로 subtle하게
- 세로 타임라인: `border-left: 2px solid #222` + 각 단계에 dot
- 또는 가로 3-4단계: 화살표 대신 번호만으로 순서 표현
- 각 단계에 코드 snippet이나 mini screenshot 포함

**Mediocre:**
- 커다란 원 안에 1, 2, 3을 넣고 화살표로 연결하는 90년대 인포그래픽
- 모든 단계 설명 길이가 똑같음 (비현실적이고 AI스러움)

### Testimonials

**Great:**
- 인용문 크기: 20-24px, italic이면 serif 폰트 사용
- 인용문 위에 회사 로고 (그레이스케일), 아래에 이름 + 직책
- 배경: 별도 색상 영역으로 구분. 또는 카드 안에 넣기
- 최대 3개 동시 표시. 슬라이더보다 고정 배치가 더 신뢰감

**Mediocre:**
- 별점 5개 + 평범한 문구 반복
- 프로필 사진이 stock photo 느낌

### FAQ Accordion

**Great:**
- 질문: 18px medium, 답변: 16px regular `#888`
- 열림/닫힘 아이콘: `+` 또는 chevron, 회전 애니메이션 `200ms ease`
- 구분선: `1px solid #1a1a1a` (다크) 또는 `#eee` (라이트)
- 최대 너비: 720px, 중앙 정렬
- 답변 펼쳐질 때 `max-height` + `opacity` 트랜지션 조합

### Footer

**Great:**
- 4-5열 링크 그룹. 그룹 제목 12px uppercase `#666`, 링크 14px `#999`
- 최하단: 로고 + 카피라이트 + 소셜 아이콘
- 전체 패딩: 상 80px 하 40px
- 배경: 본문보다 약간 어둡게 (구분감)

**Mediocre:**
- 링크가 10개 이상 한 줄에 나열
- footer에 또 다른 CTA가 있어서 시선이 분산

### CTA Section

**Great:**
- 풀 width 배경 색상 변경으로 시선 집중
- 헤드라인 32-40px + 서브텍스트 + 버튼 하나. 이 조합만으로 충분
- Linear 방식: gradient border가 있는 카드 안에 CTA
- 버튼: `padding: 12px 32px`, `border-radius: 8px`, hover시 밝기만 5% 증가

---

## 3. Color Combination Guide

### Dark Background Depth 만들기

단순 `#000` 대신 layer로 깊이 표현:
```
배경 기본:    #0A0A0A (순수 검정은 눈이 피로)
카드/섹션:    #111111 또는 #141414
Hover 상태:   #1A1A1A
Border:       rgba(255,255,255,0.06)
비활성 텍스트: #666666
본문 텍스트:   #A1A1A1
제목 텍스트:   #EDEDED (순백보다 부드러움)
```

### Accent Color 규칙

1. **5% 규칙**: 전체 화면에서 accent는 5% 이하. CTA 버튼, 배지, 중요 링크에만
2. **한 페이지에 accent 1개**: 브랜드 컬러 하나만. 두 번째 accent가 필요하면 첫 번째의 밝기/채도 변형
3. **텍스트에 accent 쓸 때**: 배경 대비 최소 4.5:1 비율 (WCAG AA)
4. **hover 상태**: accent 색의 밝기를 10% 올리기. 색상 자체를 바꾸지 말 것

### Gradient Best Practices

**좋은 그래디언트:**
```css
/* 미묘한 배경 — Stripe 스타일 */
background: linear-gradient(135deg, #0A0A2E 0%, #1A0A3E 50%, #0A1628 100%);

/* 텍스트 그래디언트 — Vercel 스타일 */
background: linear-gradient(to right, #FFFFFF 20%, #AAAAAA 80%);
-webkit-background-clip: text;

/* 버튼 테두리 그래디언트 — Linear 스타일 */
border: 1px solid transparent;
background-image: linear-gradient(#111, #111), linear-gradient(135deg, #5E6AD2, #8B5CF6);
background-clip: padding-box, border-box;
```

**나쁜 그래디언트:**
- 2색 이상의 rainbow gradient (초보 느낌)
- 시작점과 끝점 색상 차이가 너무 큰 것 (예: `red → blue`)
- 방향 없이 radial gradient를 화면 중앙에 때려넣는 것

### 검증된 다크모드 팔레트 조합

| 이름 | 배경 | 표면 | 액센트 | 레퍼런스 |
|------|------|------|--------|---------|
| Linear Purple | `#0A0A0A` | `#161616` | `#5E6AD2` | linear.app |
| Supabase Green | `#1C1C1C` | `#252525` | `#3ECF8E` | supabase.com |
| Neon Glow | `#0A0A0A` | `#131313` | `#00E699` | neon.tech |
| Stripe Deep | `#0A2540` | `#0D3356` | `#635BFF` | stripe.com |
| Warm Mono | `#111111` | `#1A1A1A` | `#F5A623` | — |

---

## 4. "AI가 만든 것 같은" 디자인 실수 목록

### 4.1 균일한 간격 (Over-Uniform Spacing)
- **문제**: 모든 섹션 간격이 정확히 80px. 모든 카드 패딩이 정확히 24px
- **해결**: 의미적 그룹 간 간격에 변화를 줌. 관련 요소는 더 가깝게 (24px), 섹션 전환은 더 넓게 (120-160px). **근접성 원칙(proximity)**을 의식적으로 적용

### 4.2 완벽한 대칭
- **문제**: 좌우가 픽셀 단위로 대칭. 현실 세계의 디자인은 의도적 비대칭이 있음
- **해결**: 텍스트는 좌측 60%, 이미지는 우측 40% 같은 비대칭 분할. 또는 이미지를 그리드 밖으로 살짝 빼기

### 4.3 Generic 아이콘
- **문제**: Heroicons/Feather에서 shield-check, lightning-bolt, globe 등 AI가 좋아하는 아이콘만 반복
- **해결**: 브랜드에 맞는 커스텀 아이콘 세트 사용. 최소한 Phosphor Icons에서 duotone weight 활용. 아이콘 색을 accent로 tint

### 4.4 시각적 위계 부재
- **문제**: 페이지의 모든 텍스트가 비슷한 크기와 무게. 어디를 먼저 봐야 할지 모름
- **해결**: 최소 4단계 크기 위계 — Display(48-72px) > Heading(28-36px) > Subheading(20-24px) > Body(16px). 색상 명도로도 위계 표현: 제목 `#FFF`, 본문 `#999`, 보조 `#555`

### 4.5 모노톤 배경
- **문제**: 페이지 전체가 같은 배경색. 섹션 구분이 없음
- **해결**: 2-3가지 배경 톤을 교차 사용. `#0A0A0A` → `#111111` → `#0A0A0A`. 또는 특정 섹션만 accent 배경 `rgba(94,106,210,0.05)`

### 4.6 마이크로 인터랙션 부재
- **문제**: hover하면 아무 변화 없음. 클릭해도 피드백 없음
- **해결**: 버튼 hover시 `transform: translateY(-1px)` + 미세한 shadow 변화. 링크는 underline offset 애니메이션. 카드는 border 색상 밝아지기. **모든 인터랙션은 200ms ease-out**

### 4.7 이미지/미디어 부재
- **문제**: 텍스트와 아이콘만 있는 페이지. 제품 스크린샷이나 실제 데모가 없음
- **해결**: hero에 제품 UI 스크린샷 또는 짧은 비디오. feature 섹션에 해당 기능의 실제 화면. 이미지는 `border-radius: 12px` + `border: 1px solid rgba(255,255,255,0.1)`

### 4.8 반복적인 레이아웃 구조
- **문제**: 3열 카드 → 좌우 2분할 → 3열 카드 → 좌우 2분할의 기계적 반복
- **해결**: 풀스크린 섹션 → 비대칭 2분할 → 1열 대형 카드 → 3열 → 풀폭 CTA처럼 리듬감 있는 변화

### 4.9 과도한 둥근 모서리
- **문제**: 모든 요소에 `border-radius: 16px` 이상. 풍선처럼 통통한 느낌
- **해결**: 카드 `12px`, 버튼 `8px`, 인풋 `6px`, 뱃지 `4px` — 크기에 비례하여 차등 적용

### 4.10 의미 없는 장식 요소
- **문제**: 배경에 떠다니는 원, 그래디언트 블롭이 콘텐츠와 무관
- **해결**: 장식이 필요하면 콘텐츠의 맥락을 강화하는 것만. DB 서비스면 노드 연결 그래픽, AI 서비스면 뉴런 패턴 등

---

## 5. Typography Rules

### Font Size Scale (Desktop)

```
Display:     56-72px  / weight 700  / line-height 1.1  / letter-spacing -0.03em
H1:          40-48px  / weight 600  / line-height 1.15 / letter-spacing -0.02em
H2:          32-36px  / weight 600  / line-height 1.2  / letter-spacing -0.02em
H3:          24-28px  / weight 600  / line-height 1.3  / letter-spacing -0.01em
H4:          20px     / weight 500  / line-height 1.4  / letter-spacing 0
Body Large:  18px     / weight 400  / line-height 1.7  / letter-spacing 0
Body:        16px     / weight 400  / line-height 1.7  / letter-spacing 0
Small:       14px     / weight 400  / line-height 1.5  / letter-spacing 0.01em
Caption:     12px     / weight 500  / line-height 1.4  / letter-spacing 0.04em (uppercase일 때)
```

### Line Height 규칙
- 큰 글씨(32px+)는 line-height를 **줄인다** (1.1-1.2). 행간이 넓으면 산만함
- 작은 글씨(16px 이하)는 line-height를 **넓힌다** (1.6-1.8). 가독성 확보
- 한국어는 영문보다 line-height +0.1 추가 (글자 높이가 균일해서 행간 부족하면 답답함)

### Letter Spacing
- Display/H1: 반드시 마이너스 (`-0.02em` ~ `-0.04em`). 안 줄이면 헐렁함
- Body: `0`이 기본. 건드리지 말 것
- 12px 이하 uppercase: `0.04em`~`0.08em` 추가. 안 하면 뭉쳐 보임

### Weight Hierarchy
- **한 페이지에 weight 3개까지**: Regular(400), Medium(500), Semibold(600)
- Bold(700)는 Display에서만. 본문에 Bold 쓰면 소리 지르는 것
- Light(300)는 40px 이상에서만. 작은 글씨에 Light 쓰면 안 보임

### Korean + English 혼합 타이포

**추천 폰트 조합:**
```
영문 heading:  Inter, Geist (Vercel), Satoshi
한글 heading:  Pretendard, SUIT
영문 body:     Inter, Geist
한글 body:     Pretendard
코드:          JetBrains Mono, Geist Mono
```

**핵심 규칙:**
1. `font-family` 선언 시 영문 폰트를 먼저: `"Inter", "Pretendard", sans-serif`
2. 한영 혼합 문장에서 한글 font-size를 영문과 동일하게 유지 (Pretendard는 x-height이 잘 맞음)
3. 숫자는 항상 영문 폰트로 렌더되게 할 것 — 한글 폰트의 숫자는 대체로 어색함
4. heading에서 한영 섞일 때, 영문만 weight 한 단계 낮추면 시각적 무게가 균형잡힘 (한글 600이면 영문 500)
5. 줄바꿈: `word-break: keep-all` 필수. 한글 단어 중간에서 끊기면 읽기 어려움

---

## Quick Checklist (매 디자인 완료 시 확인)

- [ ] 시각적 위계가 3초 안에 파악되는가? (눈이 자연스럽게 h1 → subtext → CTA 순으로 가는가)
- [ ] 색상이 3개 이내로 제한되었는가? (배경/텍스트 제외)
- [ ] 모든 interactive 요소에 hover 상태가 있는가?
- [ ] 섹션 간 간격에 의도적 변화가 있는가? (전부 동일하지 않은가)
- [ ] 제품의 실제 모습(screenshot/demo)이 포함되어 있는가?
- [ ] `word-break: keep-all`이 적용되어 있는가?
- [ ] 가장 중요한 CTA가 화면에 하나만 있는가?
- [ ] 배경에 장식 요소가 있다면, 그것이 콘텐츠와 관련이 있는가?
- [ ] border-radius가 요소 크기에 비례하는가?
- [ ] 다크 배경에서 순수 `#000`과 `#FFF`를 피하고 있는가?
