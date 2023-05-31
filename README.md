 # EDA : Easy Data Augmentation for NLP
 
- Data Augmentation은 학습 데이터가 부족한 상황에서 주로 사용되는 기법이다.
- 자연어 처리 분야는 이미지 처리에서 주로 사용되던 데이터 증강 기법이 적용되기 쉽지 않았다.
-- 문장에서 단어 하나만 바뀌어도 그 의미가 쉽게 바뀌어버리기 때문이고, 한국어는 특히나 심함


EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks
https://arxiv.org/pdf/1901.11196.pdf

몇 년간 고전을 하던 중 나오던게 본 논문이다.
2023년 5월 기준으로 그 인용수가 1300회가 넘는 걸 보면 그 위상을 알 수 있습니다.


해당 코드는 이 논문에 나오는 대표적인 네 가지 기법을 Class로 구현했습니다. 
1. SR : (Synonym Replacement) 특정 단어를 유의어로 교체 
2. RI : (Random Insertion) 임의의 단어를 삽입
3. RS : (Random Swap) 문장 내 임의의 두 단어의 위치를 바꿈
4. RD : (Random Deletion) 임의의 단어를 삭제

