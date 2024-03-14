'''
This file contains the configuration for the BNZ_to_iCost_statement_converter.
'''

ICOST_FILE_PATH = '/Users/leolee/Desktop/coding/BNZ_to_iCost_statement_converter/test_materials/iCost.csv'
BNZ_FILE_PATH = '/Users/leolee/Desktop/coding/BNZ_to_iCost_statement_converter/test_materials/BNZ.csv'
DST_PATH = '/Users/leolee/Desktop/coding/BNZ_to_iCost_statement_converter/test_materials/test.csv'
HEADERS = ['日期', '类型', '金额', '一级分类', '二级分类', '账户1', '账户2', '备注', '货币', '标签']
ENG_TO_CN_HEADER_MAP = {
    'Payee': '备注',
    'Amount': '金额',
    'Date': '日期',
    'This Party Account': '账户1',
    'Other Party Account': '账户2'
}

BNZ_TO_ICOST_ACCOUNT_MAP = {
    '02-0810-0146802-00': 'BNZ 4042',
    '02-0865-0100529-00': 'Joint account'
}
