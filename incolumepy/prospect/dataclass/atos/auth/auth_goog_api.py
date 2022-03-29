# !/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
import gspread
from oauth2client.service_account import ServiceAccountCredentials

__author__ = "@britodfbr"  # pragma: no cover

# Autenticação API Google
file_credenciais = Path('~').expanduser().joinpath(
    "projetos",
    "authkeys",
    'incolumepy-dev-6ae65605985c.json')
assert file_credenciais.is_file(), f'Ops: {file_credenciais=}'
escopo = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
credenciais = ServiceAccountCredentials.from_json_keyfile_name(
    file_credenciais, escopo)

# client_google
gc = gspread.authorize(credenciais)
