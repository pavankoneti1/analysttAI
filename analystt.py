from bs4 import BeautifulSoup as bs
import requests, time

url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

def scrapper(url):
    """
    To scrap url
    :param url:
    :return: html webpage
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        return soup
    return

def part1_dict_creator(product_url, product_name, rating, no_of_reviews):
    """
    To save data into the dict form of each URL
    :param product_url:
    :param product_name:
    :param rating:
    :param no_of_reviews:
    :return: dict with data
    """

    d = {
            'product_url': product_url,
            'product_name': product_name,
            'rating': rating,
            'no_of_reviews': no_of_reviews
    }
    return d

def part2_dict_creator(description, ASIN, manufacturer):
    """
    To save data into the dict form of each URL
    :param description:
    :param ASIN:
    :param manufacturer:
    :return: dict with data
    """

    d = {
        'description':description,
        'ASIN': ASIN,
        'manufacturer': manufacturer
    }
    return d

def part1_data_adder(scraped_data, page, soup):
    """
    To scrap data from html and filter
    :param scraped_data:
    :param page:
    :param soup:
    :return: scraped data
    """

    product_urls = ["https://www.amazon.in" + x.get('href') for x in soup.find_all('a', {
        "class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})]
    product_names = [x for x in soup.find_all('span', {"class": "a-size-medium a-color-base a-text-normal"})]
    reviews = [x for x in soup.find_all('span', {"class": "a-size-base s-underline-text"})]
    ratings = [x[:3] for x in soup.find_all('i', {"class": "aok-align-bottom"})]

    for i in len(product_urls):
        data = part1_dict_creator(product_urls[i], product_names[i], ratings[i], reviews[i])

        if page not in scraped_data:
            scraped_data[page] = [data]
        else:
            scraped_data[page].append(data)

    return scraped_data

def part2_data_adder(index, scraped_data, soup):
    """
    To scrap data from html and filter
    :param index:
    :param scraped_data:
    :param soup:
    :return:  data added to part2
    """

    description = soup.find_all('span', {"id": "productTitle"})[0]
    div_elements = soup.find_all('div', {"id": "detailBullets_feature_div"})
    li_s = div_elements[0].find_all_next('li')
    ASIN = li_s[3].find_all_next('span')[0].find_all_next('span')[1]
    manufacturer = li_s[2].find_all_next('span')[0].find_all_next('span')[1]

    data = part2_dict_creator(description, ASIN, manufacturer)
    scraped_data[index] = data
    return scraped_data

if __name__ == '__main__':
    """
    PART 1
    """
    part1_scraped_data = {}
    soup = scrapper(url)
    if soup is not None:
        page = 1
        part1_scraped_data = part1_data_adder(part1_scraped_data, page, soup)

        # For scraping data from the 20 pages
        for i in range(19):
            page+=1
            for j in soup.find_all('a', {"aria-label": f"Go to page {page}"}):
                link = "https://www.amazon.in" + j.get('href') # Next page link

                # To overcome the request pooling from amazon site used sleep
                time.sleep(1)
                temp = scrapper(link)
                if soup is not None:
                    soup = temp
                    part1_scraped_data = part1_data_adder(part1_scraped_data, page, soup)

        print('PART-1\n', part1_scraped_data)

    else:
        print('503 error server unable to handle requests')


    '''
        PART-2
    '''
    part2_scraped_data = {}
    if len(part1_scraped_data)>0:
        index = 1

        # Logic to storing data for part2
        for each in part1_scraped_data:
            for i in part1_scraped_data[each]:
                product_url = i['product_url']
                soup = scrapper(product_url)
                if soup is not None:
                    part2_scraped_data = part2_data_adder(index, part2_scraped_data, soup)
                    index += 1

        print('PART-2\n', part2_scraped_data)

