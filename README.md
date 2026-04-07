# TRIATO 회사 홈페이지

TRIATO(트리아토) 공식 회사 홈페이지. 화이트 베이스 디자인.

- **도메인**: triato.co.kr
- **기술 스택**: Astro 6, Tailwind CSS 4, TypeScript
- **배포**: Cloudflare Pages (자동 배포)

## 로컬 개발

```bash
npm install
npm run dev       # http://localhost:4321
```

## 빌드

```bash
npm run build     # dist/ 디렉토리에 정적 파일 생성
npm run preview   # 빌드 결과 로컬 프리뷰
```

## 디렉토리 구조

```
src/
├── assets/css/     # 스타일 (base, buttons, typography, global)
├── components/     # Astro 컴포넌트 (Hero, Services, Strengths 등)
├── data/           # 콘텐츠 데이터 (JSON)
├── layouts/        # 페이지 레이아웃
├── pages/          # 라우트 (index.astro)
└── styles/         # 글로벌 스타일
public/             # 정적 에셋 (로고, favicon)
reference/          # 디자인 레퍼런스 및 스펙 문서
screenshots/        # 디자인 스크린샷
```

## 배포

GitHub `main` 브랜치에 push하면 Cloudflare Pages가 자동 빌드·배포합니다.
