import requests
import json
import pandas as pd
import folium

def get_json(sido_code):
    body = {
        # 지정한 위도와 경도에서 가까운 순으로 나열
        'ins_lat': '37.56682',  
        'ins_lng': '126.97865',
        # 01=서울시, 08=경기 ... 17=세종
        # 10 미만의 값인 경우 첫 부분에 0을 넣어줘야함.
        'p_sido_cd': '{}'.format(sido_code if sido_code > 9 else "0{}".format(sido_code)),
        'p_gugun_cd': '',  # 세부지역 (지정하지 않으면 시/도 전체)
        'in_biz_cd': '',
        'set_date': '',
        'searchType': 'C',
        'all_store': 1,
        'iend': '1000',
    }

    url = 'https://www.starbucks.co.kr/store/getStore.do'
    r = requests.post(url, data=body)

    return json.loads(r.text)
    
if __name__ == "__main__":
    df = None  # 결과 데이터 프레임 정의

    for area in range(1, 18):  # 지역 INDEX가 1 ~ 17까지있음.
        jo = get_json(area)

        if df is None:
            df = pd.json_normalize(jo, 'list')
        else:
            area_df = pd.json_normalize(jo, 'list')
            df = df.append(other=area_df, ignore_index=True, sort=False)

    df = df.astype({'lat': 'float', 'lot': 'float', 's_code': 'int'})  # GPS 좌표를 float로 매장 코드를 int로 변경
    df = df[['s_code', 's_name', 'sido_name', 'lat', 'lot']]  # 필요한 데이터만 남김.
    df = df.sort_values(by="s_code")





map_osm = folium.Map(location=[36, 127], zoom_start=7)

for index, row in df.iterrows():
    location = (row['lat'], row['lot'])
    folium.Marker(location, popup=row['s_name']).add_to(map_osm)

map_osm



map_osm.save('result.html')
 






