from fastapi import Depends, FastAPI, HTTPException

import models
from company import companyapis, dependencies
from database import engine
from routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(companyapis.router,
                   prefix="/companyapis",
                   tags=["companyapis"],
                   dependencies=[Depends(dependencies.get_token_header)],
                   responses={418: {"description": "Internal Use Only"}})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
