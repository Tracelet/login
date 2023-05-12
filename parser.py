import time
from bs4 import BeautifulSoup as bs
import requests
from requests.exceptions import RequestException, HTTPError
from dataclasses import dataclass


@dataclass
class Listing:
    url: str
    title: str
    address: str
    phone_number: str
    alternate: str = None
    mobile: str = None
    fax: str = None
    email: str = None
    web_site: str = None
    open_hours: str = None
    accepted_payments: list[str] = None
    comp_info: str = None


def get_ad(endpoint: str):
    time.sleep(1)

    ad_url = "https://www.fyple.com" + endpoint

    for i in range(5):
        try:
            ad_page = requests.get(ad_url)
            break
        except (RequestException, HTTPError) as e:
            print(e)
            if i == 4:
                return None
            time.sleep(1)
        else:
            break


    ad_soup = bs(ad_page.text, "html.parser")
    ad_data = ad_soup.findAll('div', class_='mdl-card mdl-shadow--2dp panel_wrap_card')
    ad_data_contact = ad_data[0].find('div', class_='col-md-5')
    result = ad_data_contact.findAll('div', class_='row')
    contact: dict = {'Address': None, 'Phone number': None, 'Alternate': None, 'Mobile': None, 'Fax': None,
                     'Email': None, 'WebSite': None, 'OPEN HOURS': None, 'Accepted payments': None}

    for item in result:
        has_header = item.find('strong')
        text = item.get_text(' ', True)

        if has_header:
            if has_header.text == 'Contact':
                continue
            elif has_header.text == 'WebSite:':
                contact['WebSite'] = item.find('a').get('href')
            head, body = text.split(': ')
            contact[head] = body

    hours_and_payments = ad_data_contact.findAll('h3')

    for item in hours_and_payments:
        if item.text == 'OPEN HOURS':
            contact['OPEN HOURS'] = ad_data_contact \
                .find('div', class_='row collapse') \
                .get_text('\n', True)
        if item.text == 'Accepted payments':
            payments = ad_data_contact.findAll('img')
            payments_list = []
            for payment in payments:
                payments_list.append(payment.get('alt'))
            contact['Accepted payments'] = payments_list

    ad_data_info = ad_data[2].get_text('\n', True)

    ad_model = Listing(
        url=ad_url,
        title=ad_soup.find('title').text,
        address=contact['Address'],
        phone_number=contact['Phone number'],
        alternate=contact['Alternate'],
        mobile=contact['Mobile'],
        fax=contact['Fax'],
        email=contact['Email'],
        web_site=contact['WebSite'],
        open_hours=contact['OPEN HOURS'],
        accepted_payments=contact['Accepted payments'],
        comp_info=ad_data_info
    )
    return ad_model


category_dict: dict[str: list[Listing]] = {}
url = "https://www.fyple.com/categories/"
ctg_names = []
ad_list = []

for i in range(5):
    try:
        page = requests.get(url)
    except (RequestException, HTTPError) as e:
        print(e)
        time.sleep(1)
        if i == 4:
            raise e


category_soup = bs(page.text, "html.parser")
ctg_data = category_soup.find('div', class_='tab-content col-md-9')


for item in ctg_data.findAll('a'):
    ctg_names.append(item.text)
    ad_list_url = "https://www.fyple.com" + item.get('href')
    time.sleep(1)

    for i in range(5):
        try:
            ad_list_page = requests.get(ad_list_url)
        except (RequestException, HTTPError) as e:
            print(e)
            if i == 4:
                continue
            time.sleep(1)
        else:
            break

    ad_list_soup = bs(ad_list_page.text, "html.parser")
    ad_list_data = ad_list_soup.findAll('a', class_='comp_title')

    for ad in ad_list_data:
        ad_list.append(get_ad(endpoint=ad.get('href')))

    category_dict[item.text] = ad_list

    print(category_dict)
