import requests
import xml.etree.ElementTree as ET
import time

output_dict = dict()
output_list = []

YTS_RSS = "https://yts.mx/rss"

channel_element = ["title", "link", "description"]
item_element = ["title", "link", "description", "author", "category", "comments", "enclosure url", "guid", "pubDate", "source"]


def find_channel_element(root):
    print ("******** channel**********")

    string = ('channel/' + str(ch_elem) for ch_elem in channel_element)

    while True:
        try:
            data = root.find(next(string))
            if data is None:
                continue
        except StopIteration:
            break
        else:
            # print("Tag : {} - Value : {}".format(data.tag, data.text))
            output_dict[data.tag] = data.text


def find_item_element(root):
    print("********* Items **************")
    data_set = root.findall('channel/item/')

    for data in data_set:
        find_str = ('channel/item/' + str(item) for item in item_element)

        while True:
            try:
                data = root.find(next(find_str))
                if data is None:
                    continue
            except StopIteration:
                break
            else:
                print("Tag : {} - Value : {}".format(data.tag, data.text))


if __name__ == "__main__":
    obj = requests.get(YTS_RSS)

    with open("yts.xml", "wb") as file:
        file.write(obj.content)

    tree = ET.parse("yts.xml")
    root = tree.getroot()

    find_channel_element(root)
    find_item_element(root)