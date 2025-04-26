# 2025-1huggingface 챗봇서비스 개발

### 캡스톤프로젝트2 중간고사 sLLM만들기

---

# 📚 목차
- [프로젝트 소개](#프로젝트-소개)
- [주요 기능](#주요-기능)
- [필요 환경](#필요-환경)
- [느낀점](#느낀점)

---

## 프로젝트 소개
huggingface에 있는 모델을 활용한 sLLM(smaller Large Language Model)만들기 프로젝트 입니다.<br>
먼저 활용한 모델은 [Bllossom/llama-3.2-Korean-Bllossom-3B](https://huggingface.co/Bllossom/llama-3.2-Korean-Bllossom-3B)이며 한국어가 지원하지 않는 모델인 llama3.2-3B를<br>
Bllossom 팀에서 한국어-영어로 강화모델입니다.<br>
이 모델을 활용하여 fastapi를 사용해 챗봇 서비스를 만들어 보는 것이 목표입니다.

## 주요 기능
아래 사진 처럼 질문란에 원하는 질문을 적고 보내기를 클릭해 원하는 답을 들어볼수 있습니다.
<img src="img/스크린샷 2025-04-27 043917.png" width="500px"><br>
<img src="img/스크린샷 2025-04-27 044129.png" width="500px">

## 필요 환경
    torch==2.5.1+cu121
    fastapi==0.115.12
    transformers==4.51.3
    uvicorn==0.34.1
필수적으로 설치해야 하며 cuda버전이 다를 시 에러가 발생하며 해결은 cmd에서 nvidia-smi로 cuda의 버전을 확인 후<br>
[여기서](https://pytorch.org/get-started/previous-versions/)본인과 맞는 버전을 선택해 설치하면 해결 됩니다.

## 느낀점 
챗봇 서비스를 개발해보며 필요 환경들의 버전호환문제와 여러 버그를 고쳐보고 모델을 선택해보며 경험이 많이 쌓인것 같고<br>
아직은 경험이 부족하지만 조금씩 조금씩 성장하는것 같아 뿌듯하며 앞으로도 많은 서비스와 프로그램을 개발하는 시간이 되면 좋겠다.


