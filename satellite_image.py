import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70',
    }
url_image = 'https://satellite.nsmc.org.cn/mongoTile_DSS/FY/TileServer512.php'
url_data = 'https://fy4.nsmc.org.cn/nsmc/v1/nsmc/image/animation/datatime/mongodb'

def get_image(
    PRODUCT = 'FY4A-_AGRI--_N_REGI_1047E_L1C_MTCC_MULT_GLL_YYYYMMDDhhmmss_YYYYMMDDhhmmss_4000M_V0001.JPG',
    BBOX = '101.25,22.5,112.5,33.75',
    DATE = '20210721',
    TIME = '0053',
    ENDTIME = '',
):
    param_request = {
        'layer': 'PRODUCT',
        'PRODUCT': PRODUCT,
        'DATE': DATE,
        'TIME': TIME,
        'ENDTIME': ENDTIME,
        'SERVICE': 'WMS',
        'VERSION': '1.1.1',
        'REQUEST': 'GetMap',
        'FORMAT': 'image/jpeg',
        'TRANSPARENT': 'true',
        'LAYERS': 'satellite',
        'NOTILE': 'BLACK',
        'TILED': 'true',
        'WIDTH': '512',
        'HEIGHT': '512',
        'SRS: EPSG':'4326',
        'STYLES': '',
        'BBOX': BBOX,
    }
    image_request = requests.get(url=url_image, params=param_request, headers=headers)
    return image_request.content


def get_data():
    param_data = {
        'dataCode': 'FY4A-_AGRI--_N_REGI_1047E_L1C_MTCC_MULT_GLL_YYYYMMDDhhmmss_YYYYMMDDhhmmss_4000M_V0001.JPG',
        'hourRange': '3',
        'isHaveNight': '0',
        'isCustomTime': 'false',
        'endTime': '2018-07-11 16:00:00',
    }
    get_data = requests.get(url=url_data, params=param_data, headers=headers)
    data = get_data.json()
    return data['ds']


if __name__=="__main__":
    ds_data = get_data()
    # for ds in ds_data:
    #     print(ds['dataDate'], ds['dataTime'], ds['endTime'])
    #     img_content = get_image(BBOX='112.5,33.75,123.75,45',DATE=ds['dataDate'], TIME=ds['dataTime'][0:4], ENDTIME=ds['endTime'])
    #     with open('image_'+ds['dataDate']+ds['dataTime']+'.jpg','wb') as fp:
    #         fp.write(img_content)
    ds = ds_data[-1]
    img_content = get_image(BBOX='135,45.0,146.25,56.25',DATE=ds['dataDate'], TIME=ds['dataTime'][0:4], ENDTIME=ds['endTime'])
    with open('image3_'+ds['dataDate']+ds['dataTime']+'.jpg','wb') as fp:
        fp.write(img_content)