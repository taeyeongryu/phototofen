# PhotoToFen: 체스 퍼즐 이미지 FEN 변환기

**PhotoToFen**은 체스 입문자와 애호가들을 위해 책이나 화면 속의 체스 퍼즐 사진을 [FEN(Forsyth-Edwards Notation)](https://ko.wikipedia.org/wiki/포사이스-에드워즈_표기법) 형식으로 빠르게 변환해 주는 웹 애플리케이션입니다. 리체스(Lichess)나 스톡피시(Stockfish) 같은 엔진에 보드를 수동으로 배치할 필요 없이 즉시 분석할 수 있도록 돕습니다.

## 🚀 주요 기능

- **이미지 업로드**: 체스 퍼즐 사진을 간편하게 업로드할 수 있습니다.
- **자동 인식**: OpenCV와 머신러닝을 사용하여 체스판의 위치와 기물 배치를 자동으로 감지합니다.
- **차례 선택**: 백(White) 또는 흑(Black) 중 누구의 차례인지 선택할 수 있습니다.
- **즉각적인 FEN 생성**: 감지된 정보를 바탕으로 유효한 FEN 문자열을 생성합니다.
- **간편 복사**: 생성된 FEN을 클릭 한 번으로 클립보드에 복사하여 다른 앱에서 바로 사용할 수 있습니다.

## 🛠️ 기술 스택

### 프론트엔드
- **프레임워크**: React (Vite 기반)
- **언어**: TypeScript
- **스타일링**: Tailwind CSS
- **상태 관리**: React Hooks

### 백엔드
- **프레임워크**: FastAPI (Python 3.10+)
- **컴퓨터 비전**: OpenCV
- **머신러닝/추론**: PyTorch (기물 분류 모델 적용 예정)

## 📦 시작하기

### 사전 준비 사항
- Node.js 18 이상
- Python 3.10 이상
- `pip` 및 `npm`

### 설치 및 실행 방법

#### 1. 백엔드 (Python)

```bash
cd backend

# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows:
.\venv\Scripts\Activate
# Mac/Linux:
# source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt

# 서버 실행
uvicorn app.main:app --reload
```
*서버는 `http://localhost:8000`에서 실행됩니다.*

#### 2. 프론트엔드 (React)

```bash
cd frontend

# 의존성 설치
npm install

# 개발 서버 실행
npm run dev
```
*클라이언트는 `http://localhost:5173`에서 실행됩니다.*

## 📂 프로젝트 구조

```text
phototofen/
├── backend/            # FastAPI 애플리케이션 (백엔드)
│   ├── app/            # 소스 코드 (API, 서비스, 모델)
│   └── tests/          # 테스트 코드
├── frontend/           # React 애플리케이션 (프론트엔드)
│   ├── src/            # 컴포넌트, 페이지, 훅
│   └── public/         # 정적 자산
└── specs/              # 프로젝트 상세 명세 및 설계 문서
```

## 📈 개발 현황

- **[2026-01-20] Phase 1: Setup 완료**
  - 백엔드 FastAPI 초기 구조 및 CORS 설정 완료
  - 프론트엔드 Vite + React + TypeScript 환경 구축
  - Tailwind CSS 연동 및 UI 기본 틀 마련
- **[2026-01-21] Phase 3: 기본 업로드 및 FEN 변환 구현 (US1)**
  - 이미지 업로드 UI (`ImageUpload`) 및 미리보기
  - 백엔드 이미지 처리 파이프라인 (OpenCV 기반 보드 감지)
  - 기초적인 기물/빈 칸 분류 로직
  - FEN 생성 및 결과 표시

## 📝 라이선스

이 프로젝트는 교육 및 학습 목적으로 제작되었습니다.
