import pandas as pd
import gzip
import json 

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)

def get_df(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

# Load meta data 
# https://colab.research.google.com/drive/1Zv6MARGQcrBbLHyjPVVMZVnRWsRnVMpV#scrollTo=7igYuRaV4bF7

def metadata_loader(path):
    # 创建空列表以存储提取的属性
    asin_list = []
    description_list = []
    price_list = []
    imUrl_list = []
    also_bought_list = []
    bought_together_list = []
    buy_after_viewing_list = []
    salesRank_list = []
    categories_list = []

    with gzip.open(path, 'rb') as f:
        for l in f:
            # 使用 eval 解析非严格 JSON 数据
            data = eval(l.strip())

            # 提取属性并添加到对应的列表
            asin_list.append(data.get("asin", None))
            description_list.append(data.get("description", None))
            price_list.append(data.get("price", None))
            imUrl_list.append(data.get("imUrl", None))

            related = data.get("related", {})
            also_bought_list.append(related.get("also_bought", None))
            bought_together_list.append(related.get("bought_together", None))
            buy_after_viewing_list.append(related.get("buy_after_viewing", None))

            salesRank = data.get("salesRank", {})
            salesRank_list.append(salesRank.get("Video Games", None))

            categories = data.get("categories", [])
            if len(categories) > 0:
                categories_list.append(categories[0])
            else:
                categories_list.append(None)

    # 创建包含属性的字典，可以使用字典创建 Pandas 数据帧
    data_dict = {
        "asin": asin_list,
        "description": description_list,
        "price": price_list,
        "imUrl": imUrl_list,
        "also_bought": also_bought_list,
        "bought_together": bought_together_list,
        "buy_after_viewing": buy_after_viewing_list,
        "salesRank": salesRank_list,
        "categories": categories_list
    }

    # 创建 Pandas 数据帧
    df = pd.DataFrame(data_dict)

    return df



