from fastapi import FastAPI, HTTPException, status
import uvicorn 
import app.utils as utils


app = FastAPI()

@app.get("/get-dates")
def get_data(*, start_date: str, end_date: str=None):
    try:
        if utils.is_valid_end_date(start_date, end_date):
            output = utils.main(start_date, end_date)
            if isinstance(output, str): 
                return {"data": output}
            return {"data": output} 
        else: 
            return {'data': "not found as one of the dates is in an invalid format or the end date is not within the 7 day limit"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=e)

