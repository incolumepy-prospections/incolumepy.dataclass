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


def drop_sheet(spreadsheet, dropthis: bool = False):
    """
    Drop Planilha

    :param spreadsheet:
    :param dropthis:
    :return:
    """
    if dropthis:
        gc.del_spreadsheet(spreadsheet.id)
        return True
    return False


def load_create_sheet(spreadsheetname):
    """
    Carregar/Criar Planilha.

    :return:
    """

    try:
        spreadsheet = gc.open(spreadsheetname)
    except (gspread.exceptions.SpreadsheetNotFound,
            gspread.exceptions.APIError):
        spreadsheet = gc.create(spreadsheetname)

    return spreadsheet


def permission_sheet(spreadsheet):
    """
    permissões Planilha.

    :param spreadsheet:
    :return:
    """

    users = ['brito@incolume.com.br', 'britodfbr@gmail.com',
             'dev@incolume.com.br']
    for user in users:
        spreadsheet.share(user, perm_type='user', role='writer')


def get_url_sheet(spreadsheet):
    """
    Link acesso web

    :return:
    """
    result = f'https://docs.google.com/spreadsheets/d/{spreadsheet.id}'
    return result
