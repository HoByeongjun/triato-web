# CLAUDE.md — TRIATO Web

## Project

TRIATO 회사 홈페이지 (triato.co.kr). Astro 6 + Tailwind 4 + TypeScript. Cloudflare Pages 배포.

## Design System

**모든 시각/UI 결정 전 `DESIGN.md`를 먼저 읽을 것.**

- 폰트, 색상, 간격, 레이아웃, 모션 규칙은 `DESIGN.md`에 정의되어 있다.
- `DESIGN.md`에 명시되지 않은 시각 결정은 사용자 승인 없이 추가하지 않는다.
- 디자인 시안 변경 요청은 `DESIGN.md`의 Decisions Log에 추가한다.
- QA 모드에서는 `DESIGN.md`와 일치하지 않는 코드를 발견하면 플래그한다.

핵심 강제 규칙 (DESIGN.md 미준수 시 1순위 거부):

1. 화이트 베이스 유지 (`#FBFAF7` warm off-white).
2. 액센트는 **잉크블루 `#1B2EFF` 단일** — 5% 룰. 네이비/그라디언트 금지.
3. 폰트는 Pretendard(한글) + Geist(영문) + Geist Mono(시스템). Inter/Roboto/Arial 금지.
4. 그림자 0 — 깊이는 1px 헤어라인 + surface 색상 차이로만.
5. 3컬럼 카드 그리드 반복 금지 — editorial entry 패턴 유지.
6. 스톡포토 사용 금지 — Terminal Card / Ping mockup / 타이포로 대체.
7. `word-break: keep-all` 전역 유지.

## Stack

- Astro 6 + Tailwind 4 (Vite 플러그인).
- TypeScript (strict).
- 데이터 파일: `src/data/*.json` (home, services, strengths, faq, process).
- 컴포넌트: `src/components/*.astro`.
- 글로벌 CSS: `src/assets/css/*.css` (base, buttons, typography, global, layout).
- 빌드: `npm run build` → `dist/`. 배포: Cloudflare Pages 자동.

## 콘텐츠 수정 가이드

- 카피 수정은 `src/data/*.json` 직접 수정. HTML in JSON은 허용 (현재 패턴).
- `home.json`의 `hero_title`, `hero_content`는 `DESIGN.md` Hero Composition과 일치해야 함.
- `global_settings.json`의 `theme_color`는 `#1B2EFF`(accent) 또는 `#0F0F0E`(ink) 검토 대상.

## 개발

```bash
npm run dev       # http://localhost:4321
npm run build
npm run preview
```
