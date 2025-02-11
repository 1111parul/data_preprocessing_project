from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
from data_preprocessing.preprocessor import Preprocessor
# from ..data_preprocessing.preprocessor import Preprocessor


app = FastAPI()
# BASE_DIR = Path(__file__).resolve().parent.parent
# templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))



# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates

app = FastAPI()

# Correctly point to the nested templates folder
templates = Jinja2Templates(directory="api/templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process", response_class=HTMLResponse)
async def process_data(
    request: Request,
    file: UploadFile = File(...)
):
    # Read the uploaded file
    df = pd.read_csv(file.file)
    
    # Preprocess the data
    preprocessor = Preprocessor()
    cleaned_df = preprocessor.preprocess(df)
    
    # Convert the cleaned data to HTML for display
    result_html = cleaned_df.to_html()
    
    return templates.TemplateResponse("index.html", {"request": request, "result_html": result_html})

# # from fastapi.responses import StreamingResponse
# # import io

# # @app.post("/download")
# # async def download_data(file: UploadFile = File(...)):
# #     # Read and preprocess the data
# #     df = pd.read_csv(file.file)
# #     preprocessor = Preprocessor()
# #     cleaned_df = preprocessor.preprocess(df)
    
# #     # Convert the DataFrame to a CSV string
# #     stream = io.StringIO()
# #     cleaned_df.to_csv(stream, index=False)
    
# #     # Create a streaming response
# #     response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
# #     response.headers["Content-Disposition"] = f"attachment; filename=cleaned_data.csv"
# #     return response



# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"message": "Hello"}
