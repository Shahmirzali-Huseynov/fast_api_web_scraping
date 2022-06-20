from fastapi import FastAPI
import web_scaping_functions

app = FastAPI()


@app.get("/")
async def root(param1:str):
    return [
        {"message": f"Hello World {param1}"}, {"message": "Hello World"}, {"message": "Hello World"}
    ]


@app.get("/result")
def predict(product_name:str):

    # new_post = models.Post(**post.dict())
    resultTrendyol =  web_scaping_functions.trendyolWebScapingFunction(productName=product_name)
    resultAmazon = web_scaping_functions.amazonWebScapingFunction(productName=product_name)
    resultHepsiburada = web_scaping_functions.hepsiburadaWebScapingFunction(productName=product_name)
    return [resultTrendyol,resultAmazon,resultHepsiburada]