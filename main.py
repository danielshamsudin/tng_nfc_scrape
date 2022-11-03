from bs4 import BeautifulSoup
import requests
from lxml import etree
from datetime import datetime
import pandas as pd


def main():
    curTime = datetime.now().strftime("%d/%m/%Y")
    df = pd.read_csv("res.csv")
    page = requests.get(
        "https://www.lazada.com.my/products/pre-order-delivery-in-14-days-enhanced-touch-n-go-card-to-be-released-by-batches-i3175099305-s16072707014.html?clickTrackInfo=undefined&search=1&spm=a2o4k.searchlistbrand.list.49"
    )
    soup = BeautifulSoup(page.content, "html.parser")
    dom = etree.HTML(str(soup))

    status = dom.xpath('//*[@id="module_quantity-input"]/div/div/span')[0].text
    qty = dom.xpath(
        '//*[@id="module_quantity-input"]/div/div/div/div[2]/span/input/@value'
    )[0]

    print(qty)
    df = pd.concat(
        [
            df,
            pd.DataFrame(
                [[curTime, status, qty]], columns=["Date", "Status", "Quantity"]
            ),
        ]
    )
    df.to_csv("res.csv", index=False)
    print(df)


if __name__ == "__main__":
    main()
