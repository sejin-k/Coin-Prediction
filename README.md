# Coin-Prediction

### 프로젝트 배경
암호화폐 가격의 정확한 예측 방법은 탈중앙화된 통제 시장에서 자산의 가치를 증가시킬 수 있기 때문에 디지털 금융 시장에서 많은 주목을 받고 있다. 수많은 연구에서 예측 모델의 정확도를 연구했지만, 예측 모델의 성능이 좋지 않았는데 그 이유 중 하나는 가장 중요한 feature를 선별하지 않은 것과 구현 모델의 한계점이라고 볼 수 있다.\
따라서 이번 프로젝트의 목적은 암호화폐 가격에 가장 영향력이 큰 변수를 선정하다. 그리고 대표적인 4가지 딥러닝 모델 **DNN, CNN, RNN, LSTM을 사용하여 예측 모델을 구현하고 학습 후 4가지 모델의 성능을 비교 분석**한다.

### 데이터 출처
> [Kaggle bitcoin-historical-data](https://www.kaggle.com/mczielinski/bitcoin-historical-data)

* Columns
    1. Open - 시가
    2. High - 고가
    3. Low - 저가
    4. Close - 종가 
    5. Volume_(BTC) - 거래량(BTC)
    6. Vloume_(Currency) - 거래량(현물)
    7. Weighted_Price - 가중치이동평균
* Additional Columns
    1. ema1d - 지수이동평균 1일
    2. ema3d - 지수이동평균 3일
    3. sma7d - 단순이동평균 7일
    4. sma30d - 단순이동평균 30일
    5. sma90d - 단순이동평균 90일
    6. sma180d - 단순이동평균 180일
    7. z-score - MVRV z-score
* external Data -> HW성능 부족으로인해 추가하지 못함
    1. djia - 다우존스 지표
    2. hash-rate - 해쉬레이트
    3. minning-diff - 채굴 난이도
 
