import pandas as pd
from sqlalchemy import create_engine
import requests
from zipfile import ZipFile
import os
import psycopg2
from config import pg_config
from sql import *
import datetime


def CITCreat(con):
    cu = con.cursor()
    cu.execute(create_cftc_cit_supplement_table_cmd)
    con.commit()


def FORCreat(con):
    cu = con.cursor()
    cu.execute(create_cftc_futures_only_reports_table_cmd)
    con.commit()


def Oldest(db):
    if db == 'cftc_cit_supplement':
        s = datetime.date(2006, 1, 1)
    elif db == 'cftc_futures_only_reports':
        s = datetime.date(1986, 1, 1)
    return s


def DataDownload(y, db):
    if db == 'cftc_cit_supplement':
        url = f"https://www.cftc.gov/files/dea/history/dea_cit_xls_{str(y)}.zip"
    elif db == 'cftc_futures_only_reports':
        if y <= 2003:
            url = f"https://www.cftc.gov/files/dea/history/deafut_xls_{str(y)}.zip"
        else:
            url = f"https://www.cftc.gov/files/dea/history/dea_fut_xls_{str(y)}.zip"
    print(f"下載{str(y)}年報告中...")
    filename = Download(url)
    return filename, os.path.basename(url)


def Download(u):
    resp = requests.get(u)
    file_path = os.path.join(os.path.basename(u))
    with open(file_path, 'wb') as file:
        file.write(resp.content)
    with ZipFile(file_path) as zip_ref:
        filename = zip_ref.namelist()[0]
        zip_ref.extractall()
    return filename


def Process(p, s):
    df = pd.read_excel(p)
    df = df.drop(columns=['As_of_Date_In_Form_YYMMDD'])
    header = df.columns.tolist()
    header = header[1:2] + header[0:1] + header[2:]
    dict = {}
    date = ['Report_Date_as_MM_DD_YYYY', 'Report_Date_as_YYYY_MM_DD']
    for h in header:
        if h in date:
            dict[h] = 'date'
        elif h[-1] == ' ':
            dict[h] = h[:-1].lower()
        elif h == 'Change_NonComm_Spead_All_NoCIT':
            dict[h] = 'Change_NonComm_Spread_All_NoCIT'.lower()
        elif h == 'Change_in_NonComm_Spead_All':
            dict[h] = 'Change_in_NonComm_Spread_All'.lower()
        elif h == 'Traders_NonComm_Spead_Old':
            dict[h] = 'Traders_NonComm_Spread_Old'.lower()
        else:
            dict[h] = h.lower()
    df = df[header]
    df = df.rename(columns=dict)
    df = df[df.date > pd.Timestamp(s)]
    df['date'] = df['date'].apply(lambda x: x.strftime("%Y-%m-%d"))
    return df


def SQL(df, db):
    engine = create_engine('postgres://' + pg_config['user'] + ':' +
                           pg_config['password'] + '@' + pg_config['host'] +
                           ':' + str(pg_config['port']) + '/' +
                           pg_config['dbname'])
    df.to_sql(db, engine, index=False, if_exists='append')


def main(db, c):
    c.execute(f"SELECT max(date) from {dbname}")
    start = cur.fetchone()[0]
    if start is None:
        start = Oldest(dbname)
    end = datetime.datetime.today()

    for i in range(start.year, end.year + 1):
        path, zpath = DataDownload(i, dbname)
        if (not (path)):
            print('Error')
            continue
        cit_df = Process(path, start)
        SQL(cit_df, dbname)
        print(f'{str(i)}年 Done')
        os.remove(zpath)
        os.remove(path)


if __name__ == '__main__':
    conn = psycopg2.connect(user=pg_config['user'],
                            password=pg_config['password'],
                            host=pg_config['host'],
                            port=pg_config['port'],
                            database=pg_config['dbname'])
    cur = conn.cursor()

    # 建表用
    # CITCreat(conn)
    FORCreat(conn)

    # 取得最新日期
    """dbname = 'cftc_cit_supplement'
    main(dbname, cur)"""
    dbname = 'cftc_futures_only_reports'
    main(dbname, cur)
