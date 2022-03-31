# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

from pathlib import Path
from datetime import datetime
import json
import httpx
from itertools import count
from tqdm import tqdm
import pandas as pd
from dataclasses import dataclass, field
from incolumepy.prospect.dataclass.atos.auth.auth_firebase import db
from incolumepy.prospect.dataclass.atos.auth.auth_goog_api import (
    drop_sheet,
    gc,
    get_url_sheet,
    load_create_sheet,
    permission_sheet,
)
from tempfile import gettempdir

url = (
    "https://docs.google.com/spreadsheets/d"
    "/1h5GXW-7IlRCPBl99Va7KGU78L0Z-4VUNKc0kmtJIE14"
)


def get_df_from_gsheet(url_gsheet: str = ''):
    """
    GSheet

    :param url_gsheet:
    :return:
    """
    # gsheet = gc.open('report_principal_20210706')
    # gsheet = gc.open_by_key('1h5GXW-7IlRCPBl99Va7KGU78L0Z-4VUNKc0kmtJIE14')
    url_gsheet = url_gsheet or url
    gsheet = gc.open_by_url(url_gsheet)

    # print(gsheet.worksheets())
    ws = gsheet.sheet1
    # print(ws.get_all_records())
    df = pd.DataFrame(ws.get_all_records())
    df.columns = df.columns.map(str.casefold)
    df.date = pd.to_datetime(df["date"])
    df.size = df.size.astype("int16")
    df.quantia_links = pd.to_numeric(df.quantia_links, errors="coerce")
    df.quantia_links.fillna(0, inplace=True)
    df.quantia_links = df.quantia_links.astype("int8")
    # df[df.columns[df.columns.str.contains('is|has')]] = df[
    #     df.columns[
    #         df.columns.str.contains('is|has')]
    #     ].apply(lambda x: x.astype(bool))
    df[df.columns[df.columns.str.contains("is|has")]] = df[
        df.columns[df.columns.str.contains("is|has")]
    ].apply(lambda x: x.str.contains("TRUE"))

    df.ato_tipo = df.ato_tipo.astype("category")
    # df.classify = df.classify.astype('category')
    df.mimetype = df.mimetype.astype("category")
    return df


@dataclass(kw_only=True)
class Ato:
    num: str
    classify: str
    ato_tipo: str
    date: datetime = field(default=datetime.now())
    ementa: str = field(default="", repr=False)
    path: Path = field(default=None, repr=False)
    npath: Path = field(default=None, repr=False)
    epigrafe: str = field(default="", repr=False)
    basename: str = field(default="", repr=False)
    mimetype: str = field(default="text/html", repr=False)
    size: int = field(default=0, repr=False)
    quantia_links: int = field(default=0, repr=False)
    published: bool = field(default=False, repr=False)
    is_dir: bool = field(default=False, repr=False)
    is_file: bool = field(default=False, repr=False)
    is_migrable: bool = field(default=False, repr=False)
    has_tag_epigrafe: bool = field(default=False, repr=False)
    has_tag_ementa: bool = field(default=False, repr=False)
    has_tag_nav: bool = field(default=False, repr=False)
    has_tag_navdup: bool = field(default=False, repr=False)
    has_script: bool = field(default=False, repr=False)
    has_tag_css: bool = field(default=False, repr=False)
    has_tag_css_correct: bool = field(default=False, repr=False)


def run():
    # GSheet
    ss = load_create_sheet('test')
    print(ss.id)
    permission_sheet(ss)
    print(get_url_sheet(ss))
    print(drop_sheet(ss))

    # Dataclass
    a = Ato(num="00001", classify="DEC", ato_tipo="decreto")
    print(a)

    # DataFrame
    df = get_df_from_gsheet()
    print(df.info())

    # Dataclass + Dataframe
    print(df.loc[12345].to_dict())
    ato = Ato(**df.loc[12345].to_dict())
    print(ato)


if __name__ == "__main__":  # pragma: no cover
    run()
