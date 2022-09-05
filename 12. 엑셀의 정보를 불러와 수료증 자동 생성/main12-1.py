import pandas as pd
import numpy as np
# 데이터를 다루는 pandas 라이브러리를 이용하여 dataframe을 작성하고 엑셀로 저장
# pandas는 대량의 데이터를 다루기 좋음
df = pd.DataFrame([["홍길동", "1990.01.02", "2021-0001"],
                    ["김민준", "1990.05.06", "2021-0002"],
                    ["김철수", "2000.08.08", "2021-0003"],
                    ["김영희", "2000.09.09", "2021-0004"],
                    ["이서준", "2010.10.10", "2021-0005"],
                    ["장다인", "2017.12.12", "2021-0006"]])

print(df)
# pandas 라이브러리의 to_excel 함수를 이용하여 엑셀로 저장
df.to_excel(r'12. 엑셀의 정보를 불러와 수료증 자동 생성\수료증명단.xlsx',
            index=False, header=False)
df.to_excel(r'12. 엑셀의 정보를 불러와 수료증 자동 생성\수료증명단_index.xlsx',
            index=True, header=True)