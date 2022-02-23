from secedgar import CompanyFilings, FilingType

# get txt from sec
my_filings = CompanyFilings(cik_lookup='aapl',
                            filing_type=FilingType.FILING_10Q,
                            count=1,
                            user_agent='winston719@gmail.com')
my_filings.save('tempdir/')












# import requests
#
# def get_cik_map():
#     response = requests.get("https://www.sec.gov/files/company_tickers.json")
#     json_response = response.json()
#     return {v['ticker'].upper(): str(v["cik_str"]) for v in json_response.values()
#                       if v['ticker'] is not None}
#
# def get_company_facts(cik_number):
#     headers = {"User-Agent": "winston719@gmail.com"}
#     response = requests.get("https://data.sec.gov/api/xbrl/companyfacts/CIK" + str(cik_number).zfill(10) + ".json", headers=headers)
#     json_response = response.json()
#     return json_response["facts"]["dei"]["EntityCommonStockSharesOutstanding"]["units"]["shares"]
#
# def get_latest_10Q(cik_number):
#     facts = get_company_facts(cik_number)
#
#     for i in range(len(facts) - 1, -1, -1):
#         if facts[i]['form'] == '10-Q':
#             accession_number = facts[i]['accn']
#             response = requests.get(
#                 "https://www.sec.gov/cgi-bin/viewer?action=view&cik=" + str(int(cik_number)) + "&accession_number=" + accession_number + "&xbrl_type=v")
#             return response.json()
#     return None
#
# cik_map = get_cik_map()
# cik_number = cik_map['AAPL']
# print(get_latest_10Q(cik_number))