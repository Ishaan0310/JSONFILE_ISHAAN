import shutil
import datetime
import pandas as pd
import uvicorn
from fastapi import FastAPI, UploadFile, File, Form, Request, Response
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
import os
import matplotlib.pyplot as plt
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

#
# @app.post("/addcsv", tags=["datas"], summary="Add datas", description="Add / Insert data")
# async def def_post_add_data(request: Request, file: UploadFile = File(...), project_name: str = Form(...)):
#     return await add_data(project_name, file, request)
#
#
# async def add_data(projectName: str, file: UploadFile, request):
#     ts = datetime.datetime.now().strftime("%m%d_%H%M%S")
#     path = Path('D:/aryabhatta/training' + '/Regression/' + projectName + '/data/' + ts + '_' + file.filename)
#     await save_upload_file(file, path)
#     return {"filename": file.filename}
#
#
# @app.post("/uploadfile/")
# async def create_upload_file(projectName: str, file: UploadFile, request):
#     ts = datetime.datetime.now().strftime("%m%d_%H%M%S")
#     path = Path('D:/aryabhatta/training' + '/Regression/' + projectName + '/data/' + ts + '_' + file.filename)
#     await save_upload_file(file, path)
#     return {"filename": file.filename}


@app.post("/uploadJsonfile/")
async def create_upload_file(projectName: str, file: UploadFile, request):
    ts = datetime.datetime.now().strftime("%m%d_%H%M%S")
    path = Path('D:/aryabhatta/training' + '/Regression/' + projectName + '/data/' + ts + '_' + file.filename)
    await save_upload_file(file, path)
    df = open(path, 'r').read()
    print(df)
    return {df}



# @app.post("/convert/")
# async def csvtojson(csvFilePath: UploadFile, jsonFilePath: UploadFile):
#     return await convert(csvFilePath, jsonFilePath)
#
#
# def convert(csvFilePath, jsonFilePath):
#     df = pd.read_csv(csvFilePath, sep=",", header="infer", index_col=False)
#     df.to_json(jsonFilePath, orient="records", force_ascii=True)
#
#
# @app.get("/columns/")
# async def columns():
#     df = pd.read_csv(newest('D:/aryabhatta/training' + '/Regression/' + 'Ishaan' + '/data/'))
#     return tuple(df.keys())
#
#
# def cols(file):
#     df = pd.read_json(file)
#     return list(df.columns.values)
#
#
# def newest(path):
#     files = os.listdir(path)
#     paths = [os.path.join(path, basename) for basename in files]
#     return max(paths, key=os.path.getmtime)
#
#
# @app.get("/bar/", responses={200: {"content": {"image/jpg": {"example": "picture of a vector image."}}}},
#          response_class=FileResponse)
# async def bar():
#     bar()
#     return FileResponse("output.jpg", media_type="image/jpg")


# async def bar():
# bar()
# image_bytes: bytes = 'output.jpg'
# return Response(content=image_bytes, media_type="image/jpg")
# return FileResponse("output.jpg", media_type="image/jpg")

def bar():
    data = pd.read_csv(newest('D:/aryabhatta/training' + '/Regression/' + 'Pandey' + '/data/'))
    df = pd.DataFrame(data)

    X = list(df.iloc[:, 0])
    plt.xlabel("Years")

    Y = list(df.iloc[:, 1])
    plt.ylabel("Average")

    plt.bar(X, Y, color='g')
    # plt.show()
    plt.savefig("output.jpg")


async def save_upload_file(upload_file: UploadFile, destination: Path) -> None:
    try:
        upload_file.file.seek(0)
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8888)
