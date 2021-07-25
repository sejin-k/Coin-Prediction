class Preprocessing:
    
    def __init__(self, data=None):
        # 첫번째 column을 index로 지정
        if data != None:
            self.data = data.copy()
        
            print(self.df)
        
    def omitted_data_process(self, data, freq):
        '''생략된 데이터 추가
            @parm
                start_date: string형식의 시작 날짜
                end_date: string형식의 끝 날짜
                freq: string형식의 단위 ex) '1min', '1D'...
        '''
        data = data.copy()
        start_date = str(data.index[0])
        end_date = str(data.index[-1])
        dateRange = pd.date_range(start_date, end_date, freq=freq)

        # date_range와 비교하여 누락된 index 확인
        print("기본 데이터의 총 개수: ",len(data))
        print("데이터의 예상 총 개수: ",len(dateRange))
        omitLength = len(dateRange) - len(data.index)
        print("누락 데이터 개수: ", omitLength)
        
        if omitLength != 0:
            omit_data = dateRange.difference(data.index)

            # 누락된 시간 데이터 nan 데이터 생성
            columns_name = ['Open', 'High','Low', 'Close', 'Volume_(BTC)','Volume_(Currency)', 'Weighted_Price']
            omit_df = pd.DataFrame(np.empty((len(omit_data), len(data.columns))), columns=columns_name, index=omit_data)
            omit_df[:] = np.nan

            # 누락된 데이터 합치고 index 재설정
            data = pd.concat([data, omit_df], axis=0)
            data.sort_index(inplace=True)
        
        print("Success Omitted data processing")
        return data
    
    def missing_data_process(self, data):
        """결측 데이터 처리
                
        """
        print("missing data 처리")
        print(data.isnull().sum())
        data = data.copy()
        
        data.interpolate(method='linear', inplace=True)
        
        print("Success missing data processing")
        return data
    
    def add_MA(self, data):
        '''이동평균지수 추가 함수
        '''
        data = data.copy()
        ema_col_name = ['ema5m', 'ema30m', 'ema60m', 'ema1d', 'ema3d']
        sma_col_name = ['sma7d', 'sma30d', 'sma90d', 'sma180d']
        ema_mins = [5, 30, 60, 1440, 1440*3]
        sma_mins = [1440*7, 1440*30, 1440*90, 1440*180]
        ema_zip = zip(ema_col_name, ema_mins)
        sma_zip = zip(sma_col_name, sma_mins)
        
        for name, m in ema_zip:
            data[name] = self.ema(data, m)

        for name, m in sma_zip:
            data[name] = self.sma(data, m)
        
        # 초기 nan 값 처리
        data.interpolate(limit_direction="backward", inplace=True)
        print("Success add Moving average")
        return data
        
    def ema(self, data, min_=5):
        '''지수이동평균 함수'''
        return data['Close'].ewm(min_).mean()
    
    def sma(self, data, min_=1440*7):
        '''단순이동평균 함수'''   
        return data['Close'].rolling(min_).mean()
    
#     def wma(weight_array):
#         '''Binance 데이터에 추가해야하는 가중이동평균'''
#         def inner(x):
#             return (weight_array * x).mean()
#         return inner
    
    def add_MVRV_z_score(self):
        pass
    
    def preprocessing(self, data):
        '''전처리 진행 함수'''
        # 누락 데이터 처리
        data = self.omitted_data_process(data, '1min')
        # 결측 데이터 처리
        data = self.missing_data_process(data)
        # 이동평균선 추가
        data = self.add_MA(data)
        # z-score 추가
        
        return data        
        
#     def binance_preprocessing(self,data):
#         change = 58692.766481 # BTC -> Currency로 변환 (환률?)
#         # 아마 데이터 형식 변환 필요할 듯?
#         data = data.astype(np.float64)
        
#         # column이름 변겅 및 Volume_(Currency) column 추가
#         data = data.rename(columns = {"open": "Open", "high": "High", "low": "Low",
#                                             "close": "Close", "volume": "Volume_(BTC)"})
#         data['Volume_(Currency)'] = data['Volume_(BTC)'] * change
        
        
#         weights = np.arange(1,4)
#         wma5 = new_df['Close'].rolling(3).apply(lambda prices: np.dot(prices, weights)/weights.sum(), raw=True)
        
        
#         self.df = self.df[1:]
#         print("Success Binance preprocessing")
#         return self.df
    
    def save_data(self, fileName, path=""):
        '''파일 저장 함수
            @parm
                fileName: 저장 파일 이름
        '''
        self.df.to_csv(path + fileName)
        print("<저장 완료>\n{}".format(fileName))