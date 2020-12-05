"""
Convenient way to run skill locally as web-server. You can use ngrok for passing requests from
Alice.
"""

import uvicorn
from fastapi import (
    Body,
    FastAPI,
)

from alice_gotovo import skill

app = FastAPI()


@app.post('/')
def skill_entrypoint(event=Body(...)):
    response = skill.dispatcher(event)
    return response


if __name__ == '__main__':
    uvicorn.run(
        'alice_gotovo.server:app',
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
