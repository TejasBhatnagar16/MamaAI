from fastapi import FastAPI, HTTPException, status
import uvicorn 
import app.utils as utils


app = FastAPI()

@app.get("/get-dates")
def get_data(*, start_date: str, end_date: str=None):
    try:
        output = utils.main(start_date, end_date)
        return {"data": output} 
   
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=e)