# Design System — TRIATO v3

> **Approved direction:** figma 4시안 (Basic App Landing) cherry-pick + 라이브 헤리티지(시안+네이비) 복귀
> **Approved by:** 호병준 (대표) · 2026-05-02
> **Tagline:** 행동이 시작되는 곳, TRIATO
> **Category (3초 룰):** AI 팀 · 기획부터 운영까지

## 강제 규칙 (이거 어기면 무조건 거부)

1. **60-30-10 색상 비율** 준수 — 60% 베이스(흰), 30% 브랜드(네이비 `#0F2D78`), 10% 액센트/CTA(시안 `#00C8E8`).
2. **3초 룰** — Hero에서 3초 안에 "AI 팀 · 기획부터 운영까지" 카테고리 인식 가능해야 함.
3. **로고는 `public/logo-symbol.png`** — 텍스트 마크 대체 금지.
4. **Pretendard Variable** 한영 통일. Inter/Roboto/Arial 금지.
5. **모노폰트(Geist Mono)는 액센트로만**, 제목·라벨에 헤비하게 X.
6. **그림자는 부드럽게**: `shadow-card` 기본, `shadow-hover` 호버 시.
7. **마이크로 인터렉션 필수**: 모든 인터랙티브 요소에 200ms ease-out + `translateY(-1px)` hover.
8. **회피**: 보라/핑크 그라디언트, 노트북 스톡포토, 3컬럼 카드 반복, 가짜 stat/testimonials.

## Color Tokens

```css
/* 60% 베이스 */
--color-bs-bg: #FFFFFF;
--color-bs-bg-alt: #F7F9FB;
--color-bs-card: #FFFFFF;

/* 30% 브랜드 (네이비) */
--color-bs-text: #0F2D78;
--color-bs-navy: #0F2D78;
--color-bs-navy-hover: #0D2568;
--color-bs-navy-dark: #06111F;
--color-bs-bg-dark: #06111F;
--color-bs-body: #4A5568;
--color-bs-muted: #9CA3AF;

/* 10% 액센트 / CTA (시안) */
--color-bs-accent: #00C8E8;
--color-bs-accent-dim: rgba(0, 200, 232, 0.08);
--color-bs-accent-mid: rgba(0, 200, 232, 0.18);
--color-bs-accent-strong: #00A5C4;

/* 테두리 */
--color-bs-border: rgba(15, 45, 120, 0.08);
--color-bs-border-hover: rgba(15, 45, 120, 0.16);
--color-bs-border-accent: rgba(0, 200, 232, 0.32);

/* 그림자 */
--shadow-card: 0 1px 3px rgba(15, 45, 120, 0.04), 0 1px 2px rgba(15, 45, 120, 0.03);
--shadow-hover: 0 8px 30px rgba(15, 45, 120, 0.10), 0 2px 6px rgba(15, 45, 120, 0.04);
--shadow-accent: 0 8px 32px rgba(0, 200, 232, 0.18);
```

## Typography

- **한영 통일**: Pretendard Variable (CDN: `cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css`)
- **모노 액센트**: Geist Mono (Google Fonts)
- 한국어 `word-break: keep-all` 전역
- 스케일: Display 64-72 / H1 40-72 / H2 28-44 / H3 18-22 / Body 16-18 / Small 14

## CTA 규칙

- **1차 CTA**: 시안 배경 + 네이비-다크 텍스트 (10% 영역). Hero·Contact 섹션.
- **2차 CTA**: 흰 배경 + 네이비 텍스트 + border (ghost). 보조 행동.
- **헤더 CTA**: 네이비 (지속 노출되는 nav 영역, 30% 영역). 화면당 시안 CTA 1개로 제한.

## 페이지 구조 (homepage)

1. **Header** — 로고 + nav + 네이비 CTA (sticky)
2. **Hero** — 시안 글로우 배경 + 카테고리 라벨 + h1 + 한 줄 lead + CTA pair (1차 시안) + 신뢰 라인
3. **Services** — 5-card 그리드 (3+2). 시안 아이콘 박스 + 부드러운 카드 그림자
4. **Quote** — 다크 네이비 `#06111F` 풀밴드 + 시안 글로우 + 시안 강조 단어
5. **Strengths** — 2x2 클린 카드. 시안 아이콘 + 네이비 제목
6. **Process** — 3-step horizontal. 시안 number circle
7. **FAQ** — 깔끔한 아코디언
8. **Contact CTA** — 풀폭 네이비 + 시안 글로우 + 시안 1차 CTA
9. **Footer** — 다크 `#06111F` + 메뉴/서비스 컬럼

## Section Header 패턴

모든 섹션은 동일 패턴:
```
[작은 시안 라벨, uppercase tracking-wide]   ← 카테고리
[큰 네이비 h2]                              ← 핵심 메시지
[한 줄 slate 부제]                          ← 보조
```

## 마이크로 인터렉션

- 호버: 200ms ease-out, `translateY(-1px)` + 그림자 강화 또는 brightness +5%
- 카드: hover 시 `shadow-hover` + border 색 진하게
- 인라인 링크: `gap` 1.5 → 2.5 (화살표 살짝 이동)
- Live 펄스 (Hero 워크플로 카드): `bg-bs-accent animate-pulse`
- `prefers-reduced-motion: reduce` 존중

## Decisions Log

| Date | Decision | Rationale |
|---|---|---|
| 2026-04-27 | DESIGN.md v2 (Editorial-Operator) | 잉크블루 액센트, 모노 헤비, 다크 quote |
| 2026-05-02 | v2 폐기, **v3로 갱신** | 잉크블루/모노/Editorial 너무 차가움. 라이브 시안+네이비 헤리티지 복귀 |
| 2026-05-02 | figma "Basic App Landing" 4시안 cherry-pick | Hero saas-2, Services saas-1, Quote 다크 saas-1, Contact saas-2 영감 |
| 2026-05-02 | 60-30-10 비율 강제 + 3초 룰 + 마이크로 인터렉션 명시 | 대표님 피드백 — UX 핵심 원칙 |
| 2026-05-02 | Hero CTA 1차 → 시안 (네이비 → 시안) | 60-30-10 룰: 핵심 CTA = 액센트 10% |
| 2026-05-02 | Hero 카테고리 라벨 추가 ("AI 팀 · 기획부터 운영까지") | 3초 룰: 정체 명료성 |
| 2026-05-02 | Hero lead 다이어트 (한 줄) | 첫 화면 글자 너무 많음 피드백 |
