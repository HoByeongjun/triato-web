# TRIATO 홈페이지 화이트 베이스 리디자인 — 상세 시안 명세서

**작성**: 이서연 (디자인)  
**일시**: 2026-04-07  
**관련 이슈**: [TRI-23](/TRI/issues/TRI-23)  
**레퍼런스 리포트**: [00-reference-report.md](./00-reference-report.md)  
**상태**: 수빈 검토 요청 중

---

## 0. 개요

현재 다크 베이스(Blackspike 템플릿)에서 화이트 베이스로 전환.  
색상만 바꾸는 게 아니라 **화이트 베이스에 맞는 구성·여백·타이포 전체 재설계**.

> 레퍼런스 근거: Stripe(구성), 토스(한글 타이포+여백), 채널톡(CTA 스타일), Anthropic(신뢰감 톤)

---

## 1. 디자인 토큰 (CSS Variables)

### 1.1 현재 vs 화이트 베이스 비교

```
현재 (다크)                          →  화이트 베이스
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--color-bs-surface-0: #080E1A       →  --color-bs-bg:      #FFFFFF
--color-bs-surface-1: #0C1322       →  --color-bs-bg-alt:  #F8FAFB
--color-bs-surface-2: #10182A       →  --color-bs-card:    #FFFFFF
--color-bs-foreground-light: #E6EDF5 →  --color-bs-text:    #1A1A2E
--color-bs-foreground-dark: #7A8BA3  →  --color-bs-muted:   #6B7684
--color-bs-border: rgba(255,255,255,0.06) → --color-bs-border: rgba(0,0,0,0.08)
```

### 1.2 신규 화이트 베이스 토큰 전체 정의

```css
@theme {
  /* ── 배경 레이어 ── */
  --color-bs-bg:         #FFFFFF;          /* 기본 배경 */
  --color-bs-bg-alt:     #F8FAFB;          /* 교차 섹션 배경 (그레이-블루 틴트) */
  --color-bs-bg-dark:    #1A1A2E;          /* 다크 CTA 섹션 배경 */
  --color-bs-card:       #FFFFFF;          /* 카드 배경 */
  --color-bs-card-hover: #F8FAFB;          /* 카드 hover 배경 */

  /* ── 텍스트 ── */
  --color-bs-text:       #1A1A2E;          /* 제목/강조 (네이비 톤 — 순검정 X) */
  --color-bs-body:       #4A5568;          /* 본문 텍스트 */
  --color-bs-muted:      #9CA3AF;          /* 보조/플레이스홀더 */

  /* ── TRIATO 브랜드 컬러 유지 ── */
  --color-bs-accent:     #00C8E8;          /* 시안 액센트 (유지) */
  --color-bs-accent-dim: rgba(0,200,232,0.08); /* 시안 배경 틴트 */
  --color-bs-navy:       #0F2D78;          /* 네이비 (Primary CTA 배경) */
  --color-bs-navy-hover: #0D2568;          /* 네이비 hover */
  --color-bs-mid:        #1A6FBF;          /* 미드 블루 */

  /* ── 테두리 ── */
  --color-bs-border:       rgba(0,0,0,0.08);  /* 기본 테두리 */
  --color-bs-border-hover: rgba(0,0,0,0.16);  /* hover 테두리 */
  --color-bs-border-accent: rgba(0,200,232,0.3); /* 시안 강조 테두리 */

  /* ── 그림자 ── */
  --shadow-card:    0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  --shadow-hover:   0 4px 16px rgba(0,0,0,0.08), 0 2px 4px rgba(0,0,0,0.04);
  --shadow-accent:  0 4px 24px rgba(0,200,232,0.16);
}
```

---

## 2. 타이포그래피

### 2.1 폰트 패밀리 (변경 없음)

```css
--font-display: "Pretendard Variable", "Pretendard", "Inter", "ui-sans-serif", "system-ui", "sans-serif";
--font-body:    "Pretendard Variable", "Pretendard", "Inter", "ui-sans-serif", "system-ui", "sans-serif";
```

> **근거**: Pretendard는 한글+영문 통합 폰트로 비율이 가장 균형적. 토스·채널톡도 유사한 폰트 스택 사용.

### 2.2 크기 스케일 (화이트 기준 조정)

```
역할          크기(모바일)    크기(데스크톱)  Weight  Line-height  Letter-spacing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Display/H1   36px            56px            700     1.1          -0.025em
H2(섹션제목)  24px            36px            600     1.2          -0.015em
H3(카드제목)  18px            22px            600     1.3          -0.01em
Body Large   16px            18px            400     1.7          0
Body         15px            16px            400     1.7          0
Small/Label  12px            13px            500     1.4          0.02em
```

> **화이트에서 중요한 것**: 텍스트 대비가 높아져서 오히려 weight를 낮춰야 함.  
> 다크에서 600이 맞으면 화이트에서 400~500으로도 충분히 강조됨.

### 2.3 한글 필수 CSS 규칙

```css
/* 모든 텍스트 요소 */
word-break: keep-all;
overflow-wrap: break-word;

/* 긴 서브텍스트 최대 너비 */
max-width: 36em; /* 약 36자 — 가독성 최적 */
```

---

## 3. 레이아웃 시스템

### 3.1 컨테이너

```css
.bs-container {
  max-width: 1200px;   /* 현재와 동일 — 충분히 넓음 */
  margin: 0 auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}

/* 반응형 */
@media (min-width: 768px)  { padding: 0 2rem; }
@media (min-width: 1024px) { padding: 0 3rem; }
```

### 3.2 섹션 간격 (화이트에서 더 중요)

```
섹션 상하 패딩:   80px (모바일) / 120px (데스크톱)
섹션 간 구분:     배경색 교차 (#FFFFFF ↔ #F8FAFB) — divider 선 없음
카드 그리드 gap:  24px (모바일) / 32px (데스크톱)
카드 내부 패딩:   24px (모바일) / 32px (데스크톱)
```

> **근거**: 다크에서는 배경색 차이가 명확하지만, 화이트에서는 여백이 곧 섹션 구분. 좁으면 답답하게 느껴짐.

---

## 4. 컴포넌트별 상세 명세

### 4.1 HeaderMain (헤더)

**현재**: 다크 배경 고정 헤더  
**변경**: 화이트 배경 + 스크롤 시 blur 처리

```
┌────────────────────────────────────────────────────────────────────┐
│  [◇ TRIATO]          서비스   프로세스   강점   문의   [프로젝트 문의] │
└────────────────────────────────────────────────────────────────────┘
```

**스타일 명세**:
```
높이:           64px
배경(기본):     #FFFFFF
배경(스크롤 후): rgba(255,255,255,0.85) + backdrop-filter: blur(12px)
하단 테두리(스크롤 후): 1px solid rgba(0,0,0,0.06)
로고 텍스트:    #1A1A2E, font-weight 700
Nav 링크:      #6B7684, font-size 14px, font-weight 500
Nav 링크 hover: #1A1A2E, transition 150ms
CTA 버튼:      background #0F2D78, color #FFFFFF, border-radius 8px
               padding 10px 20px, font-size 14px, font-weight 600
               hover: background #0D2568
```

**코드 변경 포인트** (HeaderMain.astro):
```
class 변경:
  bg-bs-surface-0       → bg-white (기본) + sticky top-0 z-50
  text-bs-foreground-light → text-bs-text
  text-bs-foreground-dark  → text-bs-muted
  CTA 버튼: bg-bs-accent → bg-bs-navy
```

---

### 4.2 HeroSection (히어로)

**현재**: 다크 배경 + 시안 로고 비주얼  
**변경**: 화이트 배경 + 우측 제품 비주얼(스크린샷 또는 추상적 UI 데모)

```
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│  [Trigger  →  Action]          ← 뱃지 (시안 점 + 회색 텍스트)        │
│                                                                    │
│  행동이 시작되는 곳,              ┌──────────────────────────────┐   │
│  TRIATO                         │                              │   │
│                                 │   [제품 스크린샷 또는          │   │
│  AI와 자동화로 비즈니스의         │    UI 추상 요소]              │   │
│  실행력을 획기적으로              │                              │   │
│  높여드립니다.                   │                              │   │
│                                 └──────────────────────────────┘   │
│  [프로젝트 문의]  [서비스 보기]                                        │
│  (네이비 채움)    (테두리 아웃라인)                                     │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

**스타일 명세**:
```
섹션 배경:       #FFFFFF
섹션 상하 패딩:  pt-16 pb-20 (모바일), pt-24 pb-28 (데스크톱)

뱃지:
  배경: rgba(0,200,232,0.08)
  테두리: 1px solid rgba(0,200,232,0.2)
  텍스트: #4A5568, font-size 13px
  점: background #00C8E8, w-1.5 h-1.5

헤드라인:
  크기: 36px (모바일) / 56px (데스크톱)
  weight: 700
  색상: #1A1A2E
  letter-spacing: -0.025em
  line-height: 1.1

서브텍스트:
  크기: 16px (모바일) / 18px (데스크톱)
  weight: 400
  색상: #4A5568
  line-height: 1.7
  max-width: 480px

CTA Primary [프로젝트 문의]:
  배경: #0F2D78 (네이비)
  텍스트: #FFFFFF, font-weight 600
  padding: 12px 28px
  border-radius: 8px
  hover: background #0D2568, translateY(-1px)
  transition: all 200ms ease

CTA Secondary [서비스 보기]:
  배경: transparent
  텍스트: #1A1A2E
  border: 1.5px solid rgba(0,0,0,0.15)
  padding: 12px 28px
  border-radius: 8px
  hover: border-color rgba(0,0,0,0.3), background rgba(0,0,0,0.02)

우측 비주얼:
  배경: rgba(0,200,232,0.04) + 미묘한 그리드 패턴
  border-radius: 16px
  border: 1px solid rgba(0,0,0,0.06)
  반응형: 모바일에서 숨김(hidden lg:block)
```

**코드 변경 포인트** (HeroSection.astro):
```
section:       bg-bs-surface-0 제거 → 기본 배경 (#FFFFFF)
뱃지:          border-bs-border bg-bs-surface-2/60 → border-bs-border-accent bg-bs-accent-dim
               text-bs-foreground-dark → text-bs-body
h1:            [&_.text-bs-accent]:text-bs-accent (유지)
서브텍스트:    text-bs-foreground-dark → text-bs-body
CTA Primary:   bg-bs-accent text-bs-surface-0 → bg-bs-navy text-white
CTA Secondary: border-bs-border hover:border-bs-border-hover → 새 스타일
비주얼 배경:   bg-gradient from-bs-accent/8 → from-bs-accent-dim
              (다크 관련 색상 제거, 라이트 톤으로)
```

---

### 4.3 ServicesCarousel → ServicesSection으로 개편

**현재**: 가로 스크롤 카루셀  
**변경**: 3열 그리드 카드 (화이트에서는 카루셀보다 안정적)

```
┌─────────────────────────────── #F8FAFB ─────────────────────────┐
│                                                                  │
│           우리가 하는 일                    ← 섹션 제목           │
│           비즈니스 성장에 필요한 모든 기술적 역량을 제공합니다.       │
│                                                                  │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐ │
│  │ ╔══╗              │  │ ◈                │  │ ⟳                │ │
│  │ ╚══╝              │  │                  │  │                  │ │
│  │ 맞춤 소프트웨어    │  │ AI 솔루션         │  │ 업무 자동화       │ │
│  │ 개발              │  │                  │  │                  │ │
│  │                  │  │                  │  │                  │ │
│  │ 웹/앱부터 인프라까지│  │ AI 에이전트,      │  │ 반복 업무를       │ │
│  │ 풀스택 개발.       │  │ RAG, 챗봇 등      │  │ 자동화로 전환.    │ │
│  │ 클라우드 배포까지. │  │ 맞춤 개발.        │  │ 실행력을 높입니다.│ │
│  │                  │  │                  │  │                  │ │
│  │ 자세히 알아보기 →  │  │ 자세히 알아보기 → │  │ 자세히 알아보기 → │ │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘ │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**카드 스타일 명세**:
```
배경:         #FFFFFF
테두리:       1px solid rgba(0,0,0,0.08)
border-radius: 12px
패딩:         28px 32px (데스크톱)

아이콘:
  크기: 40px × 40px
  배경: rgba(0,200,232,0.08)
  색상: #00C8E8 (시안)
  border-radius: 10px
  padding: 8px

제목: #1A1A2E, 20px, weight 600, margin-top 16px
설명: #4A5568, 15px, weight 400, line-height 1.7, margin-top 8px
링크: #00C8E8, 14px, weight 500, margin-top 20px, 하단 밑줄

hover 상태:
  transform: translateY(-2px)
  box-shadow: 0 8px 24px rgba(0,0,0,0.08)
  border-color: rgba(0,200,232,0.3)
  transition: all 200ms ease-out
```

---

### 4.4 QuoteSection → 배경색 변경

**현재**: 다크 배경 인용문  
**변경**: 네이비 배경 인용문 섹션 (화이트 베이스에서 강한 대비)

```
┌────────────────────────── #0F2D78 (네이비) ──────────────────────┐
│                                                                  │
│     ❝                                                            │
│                                                                  │
│     아이디어를 현실로 만드는 것. 그것이 트리거입니다.              │
│     문제를 정의하고, 솔루션을 설계하고, 빠르게 실행합니다.         │
│     우리는 행동하는 팀입니다.                                     │
│                                                                  │
│     — 호병준, 대표, TRIATO                                        │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**스타일 명세**:
```
섹션 배경: #0F2D78 (TRIATO 네이비)
인용문 텍스트: #FFFFFF, 22px (모바일 18px), weight 400, line-height 1.7
인용문 기호 ❝: #00C8E8, 48px (장식)
Cite: rgba(255,255,255,0.6), 14px, margin-top 24px
섹션 패딩: 80px 상하 (데스크톱)
최대 너비: 720px, 중앙 정렬
```

---

### 4.5 ProcessSection (프로세스)

**현재**: 세로 타임라인  
**변경**: 가로 3단계 (화이트에서 더 명확)

```
┌─────────────────────────────── #FFFFFF ─────────────────────────┐
│                                                                  │
│           프로젝트 진행 방식                                       │
│           빠르고 투명하게, 처음부터 끝까지 함께.                    │
│                                                                  │
│   01 ────────────────── 02 ────────────────── 03                 │
│   ●                     ●                     ●                  │
│  상담 & 기획            개발 & 검증            런칭 & 운영          │
│                                                                  │
│  요구사항을 정확히       AI + 풀스택 팀이        배포 후 안정화,     │
│  이해하고 범위와         스프린트 단위로          유지보수와         │
│  일정을 확정합니다.      빠르게 만들어갑니다.     운영을 지원합니다.  │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**스타일 명세**:
```
섹션 배경: #FFFFFF
연결선: 2px solid #E5E7EB (점선 가능: border-style: dashed)
연결점(●): 
  배경: #00C8E8 (시안)
  크기: 12px × 12px, border-radius 50%
  테두리: 3px solid rgba(0,200,232,0.2)

번호(01, 02, 03):
  크기: 13px
  색상: #00C8E8
  font-weight: 600
  letter-spacing: 0.05em
  margin-bottom: 12px

단계 제목: #1A1A2E, 18px, weight 600
단계 설명: #4A5568, 15px, weight 400, line-height 1.7
```

---

### 4.6 StrengthsSection → 배경 변경

**현재**: 다크 배경 강점 리스트  
**변경**: #F8FAFB 배경 교차

```
스타일 명세:
섹션 배경: #F8FAFB
강점 카드:
  배경: #FFFFFF
  테두리: 1px solid rgba(0,0,0,0.08)
  border-radius: 12px
  패딩: 24px
  아이콘 색상: #00C8E8
  제목: #1A1A2E
  설명: #4A5568
```

---

### 4.7 FaqSection (FAQ)

**현재**: 다크 배경 아코디언  
**변경**: 화이트 배경 아코디언

**스타일 명세**:
```
섹션 배경: #FFFFFF
최대 너비: 720px, 중앙 정렬

아코디언 항목:
  구분선: 1px solid rgba(0,0,0,0.08)
  질문 텍스트: #1A1A2E, 16px, weight 500
  아이콘(+ / ×): #6B7684, 20px
  
  열린 상태:
    답변 텍스트: #4A5568, 15px, weight 400, line-height 1.7
    
  hover:
    질문 텍스트: #00C8E8
    transition: color 200ms
    
  열림/닫힘 애니메이션:
    max-height + opacity 조합, 200ms ease-out
```

---

### 4.8 ContactSection (문의)

**현재**: 다크 배경 CTA  
**변경**: 네이비 배경 최종 CTA

```
┌────────────────────────── #0F2D78 (네이비) ──────────────────────┐
│                                                                  │
│           프로젝트를 시작할 준비가 되셨나요?                        │
│           지금 바로 무료 상담을 신청하세요.                          │
│           응답까지 평균 24시간 이내.                                │
│                                                                  │
│                    [무료 상담 신청하기]                             │
│                    (흰 배경, 네이비 텍스트)                         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**스타일 명세**:
```
섹션 배경: #0F2D78

제목: #FFFFFF, 32px (모바일 24px), weight 700
서브텍스트: rgba(255,255,255,0.7), 16px, weight 400, margin-top 12px

CTA 버튼:
  배경: #FFFFFF
  텍스트: #0F2D78
  font-weight: 600
  padding: 14px 32px
  border-radius: 8px
  margin-top: 32px
  hover: background rgba(255,255,255,0.9), translateY(-1px)
  box-shadow: 0 4px 16px rgba(0,0,0,0.15)
```

---

### 4.9 FooterMain (푸터)

**현재**: 매우 다크 배경  
**변경**: 어두운 네이비 배경

```
┌─────────────────────────────── #1A1A2E ─────────────────────────┐
│                                                                  │
│  ◇ TRIATO                   서비스   프로세스   팀   블로그         │
│  행동이 시작되는 곳.                                              │
│                             맞춤 개발  진행 방식  소개  최신 글    │
│  bjho@triato.co.kr          AI 솔루션  팀 소개                   │
│  010-7207-1394              자동화                               │
│                                                                  │
│  ─────────────────────────────────────────────────────────────── │
│  © 2026 TRIATO. All rights reserved.                            │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**스타일 명세**:
```
배경: #1A1A2E (현재보다 약간 밝음 — 순검정 대신)
패딩: 상 64px, 하 40px
구분선: 1px solid rgba(255,255,255,0.08)

로고 텍스트: #FFFFFF
슬로건: rgba(255,255,255,0.5), 13px
연락처: rgba(255,255,255,0.5), 13px

메뉴 그룹 제목: rgba(255,255,255,0.35), 11px, uppercase, letter-spacing 0.06em
메뉴 링크: rgba(255,255,255,0.5), 13px
메뉴 링크 hover: rgba(255,255,255,0.85), transition 150ms

카피라이트: rgba(255,255,255,0.3), 12px
```

---

## 5. 섹션 구성 순서 (확정)

### Phase 1 — 초기 런칭 (현재 구현 범위)

```
순서   섹션                   배경색        설명
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1      Header (sticky)        #FFFFFF+blur  
2      HeroSection            #FFFFFF       헤드라인 + CTA + 비주얼
3      ServicesSection        #F8FAFB       3열 카드
4      QuoteSection           #0F2D78       인용문 (네이비 대비)
5      ProcessSection         #FFFFFF       가로 3단계
6      StrengthsSection       #F8FAFB       강점 카드
7      FaqSection             #FFFFFF       아코디언
8      ContactSection         #0F2D78       최종 CTA (네이비)
9      FooterMain             #1A1A2E       링크 + 카피라이트
```

> **배경색 리듬**: 화이트 → 연그레이 → 네이비 → 화이트 → 연그레이 → 화이트 → 네이비 → 다크  
> 단조롭지 않으면서도 TRIATO 네이비가 강조 포인트로 등장.

---

### Phase 2 — 콘텐츠 확보 후 추가 섹션

> **제외 사유**: 아래 3개 섹션은 B2B 에이전시 전환율에 직결되는 핵심 섹션(Blend B2B, Stripe, Anthropic 모두 포함)이나, TRIATO는 현재 론칭 초기로 실제 고객 데이터·프로젝트 레퍼런스가 없음. 빈 섹션이나 더미 콘텐츠는 신뢰도를 오히려 낮추므로 Phase 2로 연기.

#### 4-A. TrustLogoSection (신뢰도 로고) — Phase 2

```
┌─────────────────────────────── #F8FAFB ─────────────────────────┐
│                                                                  │
│           함께한 고객 / 파트너                                     │
│                                                                  │
│   [로고1]   [로고2]   [로고3]   [로고4]   [로고5]                 │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**위치**: HeroSection 바로 아래 (순서 3번으로 삽입, ServicesSection을 4번으로 밀기)  
**스타일 명세**:
```
섹션 배경:   #F8FAFB
패딩:        40px 상하
섹션 제목:   "함께한 고객", 12px uppercase, #9CA3AF, letter-spacing 0.08em, 중앙
로고 행:     grayscale(100%) opacity 0.4 → hover 시 grayscale(0) opacity 1, transition 300ms
로고 크기:   높이 28-36px, 자동 너비
로고 간격:   48px (데스크톱), 32px (모바일)
최소 개수:   3개 이상일 때 섹션 표시 (그 미만이면 숨김)
```
**활성화 조건**: 실제 고객사 로고 최소 3개 확보 시

---

#### 4-B. PortfolioSection (포트폴리오/케이스 스터디) — Phase 2

```
┌─────────────────────────────── #FFFFFF ─────────────────────────┐
│                                                                  │
│           프로젝트 사례                                            │
│           실제로 만든 것들을 보여드립니다.                           │
│                                                                  │
│   ┌──────────────────────┐  ┌──────────────────────┐            │
│   │  [스크린샷]           │  │  [스크린샷]           │            │
│   │                      │  │                      │            │
│   │  프로젝트명           │  │  프로젝트명           │            │
│   │  [태그: 웹개발] [AI]  │  │  [태그: 자동화]       │            │
│   │  짧은 설명 1-2줄      │  │  짧은 설명 1-2줄      │            │
│   │  자세히 보기 →        │  │  자세히 보기 →        │            │
│   └──────────────────────┘  └──────────────────────┘            │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**위치**: ProcessSection 다음 (순서 7번으로 삽입)  
**스타일 명세**:
```
섹션 배경:     #FFFFFF
그리드:        2열 (데스크톱), 1열 (모바일)
카드 border-radius: 12px
이미지 높이:   220px, object-fit: cover
태그:          작은 뱃지, rgba(0,200,232,0.08) 배경, #00C8E8 텍스트, 12px
카드 hover:    box-shadow 0 8px 24px rgba(0,0,0,0.08), translateY(-2px)
```
**활성화 조건**: 완성된 프로젝트 레퍼런스 최소 2개 이상

---

#### 4-C. TestimonialsSection (고객 추천사) — Phase 2

```
┌─────────────────────────────── #F8FAFB ─────────────────────────┐
│                                                                  │
│           고객 후기                                                │
│                                                                  │
│   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐ │
│   │ ❝                │  │ ❝                │  │ ❝                │ │
│   │ "덕분에 3개월 만에│  │ "AI 자동화 도입   │  │ "복잡한 요구사항  │ │
│   │  출시했습니다."   │  │  후 업무 처리    │  │  을 이해하고 빠   │ │
│   │                  │  │  속도가 크게 향  │  │  르게 구현해주   │ │
│   │  김○○ 대표       │  │  상됐습니다."    │  │  었습니다."      │ │
│   │  ○○ 회사         │  │  이○○ CTO       │  │  박○○ 팀장       │ │
│   └──────────────────┘  └──────────────────┘  └──────────────────┘ │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**위치**: PortfolioSection 다음 (ContactSection 바로 앞)  
**스타일 명세**:
```
섹션 배경:    #F8FAFB
카드:         3열 (데스크톱), 1열 (모바일)
카드 배경:    #FFFFFF, border 1px solid rgba(0,0,0,0.08), border-radius 12px
인용 기호 ❝: #00C8E8, 32px (장식)
인용문:       #1A1A2E, 16px, line-height 1.7, italic 없음 (한국어 italic 어색)
작성자:       #4A5568, 14px, font-weight 500
회사명:       #9CA3AF, 13px
```
**활성화 조건**: 실제 고객 동의 후기 최소 2개 이상

---

## 6. global.css 변경 요약

### 제거할 것
```css
--color-bs-surface-0, -1, -2, -3, -alt  (다크 서피스 레이어 전체)
--color-bs-foreground-light, -dark, -muted (다크용 포그라운드)
```

### 추가할 것
```css
--color-bs-bg, --color-bs-bg-alt, --color-bs-bg-dark
--color-bs-card, --color-bs-card-hover
--color-bs-text, --color-bs-body, --color-bs-muted
--color-bs-border, --color-bs-border-hover, --color-bs-border-accent
--color-bs-navy-hover
```

### 유지할 것
```css
--color-bs-accent: #00C8E8
--color-bs-accent-dim: rgba(0,200,232,0.08)
--color-bs-navy: #0F2D78
--color-bs-mid: #1A6FBF
--color-bs-warm, -green, -purple, -rose (기타 보조 색상)
--font-display, --font-body
--ease-bs-bounce, --ease-bs-spring
```

---

## 7. 구현 우선순위 (김민준 참고용)

```
1순위 (핵심 외관): global.css 토큰 교체
2순위 (즉각 효과): HeaderMain, HeroSection 변환
3순위 (본문):     ServicesSection(카루셀→그리드), ProcessSection
4순위 (CTA):      QuoteSection, ContactSection 네이비 배경
5순위 (마무리):   StrengthsSection, FaqSection, FooterMain
```

---

## 8. 검토 체크리스트

- [x] 레퍼런스 13개 분석 완료
- [x] Astro 템플릿 5개 비교 완료
- [x] 전체 섹션 와이어프레임 작성
- [x] 색상 토큰 정의 (CSS 변수 레벨)
- [x] 타이포그래피 스케일 확정
- [x] 컴포넌트별 구체적 수치 명세 (padding, border-radius, font-size 등)
- [x] 섹션 순서 및 배경색 리듬 설계
- [x] 구현 우선순위 정의
- [ ] 수빈 1차 검토
- [ ] 대표님 최종 승인
- [ ] 김민준 구현 착수

---

**다음 단계**: 수빈 검토 후 대표님 컨펌 → 김민준에게 전달하여 구현 착수
