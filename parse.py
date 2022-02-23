# Fetch following data from SEC
# Interest expense
# Tax expense
# Liability
# Revenue
# Outstanding share
# Market cap
# Total asset

from bs4 import BeautifulSoup
import re
import os

# read saved txt
root = 'tempdir'
file_list = []
for path, subdirs, files in os.walk(root):
    for name in files:
        file_list.append(os.path.join(path, name))
for file in file_list:
    f = open(file, "r")
    content = f.read()
    # print(content[0:1300])
    soup = BeautifulSoup(content, 'xml')
    # print(soup.prettify())

    data = {}

    selected_items = soup.find_all('ix:nonFraction')
    for item in selected_items:
        if len(data) == 5:
            break

        if 'interest_expense' not in data and item.get('name') == 'us-gaap:InterestExpense':
            scale = item.get('scale')
            data['interest_expense'] = int(re.search(r'\d+\,?\d*', item.text)[0].replace(',', '')) * 10 ** int(scale)

        if 'tax_expense' not in data and re.search('TaxExpense', item.get('name')):
            scale = item.get('scale')
            data['tax_expense'] = int(re.search(r'\d+\,?\d*', item.text)[0].replace(',', '')) * 10 ** int(scale)

        if 'total_liabilities' not in data and item.get('name') == 'us-gaap:Liabilities':
            scale = item.get('scale')
            data['total_liabilities'] = int(re.search(r'\d+\,?\d*', item.text)[0].replace(',', '')) * 10 ** int(scale)

        # if 'revenue' not in data and item.get('name') == ''

        if 'basic_shares' not in data and item.get('name') == 'us-gaap:WeightedAverageNumberOfSharesOutstandingBasic':
            scale = item.get('scale')
            data['basic_shares'] = int(re.search(r'\d+\,?\d*', item.text)[0].replace(',', '')) * 10 ** int(scale)

        if 'total_assets' not in data and item.get('name') == 'us-gaap:Assets':
            scale = item.get('scale')
            data['total_assets'] = int(re.search(r'\d+\,?\d*', item.text)[0].replace(',', '')) * 10 ** int(scale)

    print(data)













    # interest_expense = soup.find('span', string='Interest expense').findNext().text
    # interest_expense = int(re.search(r'\d+\,?\d*', interest_expense)[0].replace(',', ''))
    # print('Interest expense: %d' % interest_expense)
    #
    # tax_expense = soup.find('span', string=re.compile('.*{0}.*'.format('tax expense')), recursive=True).findNext().text
    # tax_expense = int(re.search(r'\d+\,?\d*', tax_expense)[0].replace(',', ''))
    # print('Tax expense: %d' % tax_expense)
    #
    # total_liabilities = soup.find('span', string=re.compile('.*{0}.*'.format('[Tt]otal liabilities')),
    #                               recursive=True).findNext().text
    # total_liabilities = int(re.search(r'\d+\,?\d*', total_liabilities)[0].replace(',', ''))
    # print('Total liabilities: %d' % total_liabilities)
    #
    # targets = ['net sales', '[Rr]evenue']
    # for target in targets:
    #     item = soup.find('span', string=re.compile(target))
    #     if item:
    #         revenue = item.findNext().text
    #         break
    #
    # revenue = int(re.search(r'\d+\,?\d*', revenue)[0].replace(',', ''))
    # print('Revenue: %d' % revenue)