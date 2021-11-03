from datetime import datetime
from modules.antoshkaspb import Fetcher as Antoshkaspb
from configs import configs

if __name__ == "__main__":
    # fetcher = Antoshkaspb(configs[0])
    # fetcher.get_stream(goods_type='category/koljaski')
    # fetcher = Antoshkaspb(configs[1])
    # fetcher.get_stream(goods_type='kolyaski-spb/detskie-kolyaski/progulochnye-kolyaski-knizhki')
    # fetcher = Antoshkaspb(configs[2])
    # fetcher.get_stream(goods_type='/catalog/tipkolyaski-is-1v1-or-2v1-or-3v1-or-transformer-or-progulka-or-trost-or-dvoynya')
    # fetcher = Antoshkaspb(configs[3])
    # fetcher.get_stream(goods_type='/catalog/Детские-коляски/')
    # fetcher = Antoshkaspb(configs[4])
    # fetcher.get_stream(goods_type='/icatalog/categories/kolyaski')
    # fetcher = Antoshkaspb(configs[5])
    # fetcher.get_stream(goods_type='/catalog')
    # fetcher = Antoshkaspb(configs[6])
    # fetcher.get_stream(goods_type='')
    # fetcher = Antoshkaspb(configs[7])
    # fetcher.get_stream(goods_type='')
    # fetcher = Antoshkaspb(configs[8])
    # fetcher.get_stream(goods_type='kolyaski')
    fetcher = Antoshkaspb(configs[9])
    fetcher.get_stream(goods_type='search')

