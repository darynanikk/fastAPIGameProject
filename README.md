# fastAPIGameProject

## Getting started
  - I am using PyCharm, so there is no need to manully create virtual environment
  - git clone git@github.com:darynanikk/fastAPIGameProject.git
  - cd fastAPIGameProject
  - pip install -r requriements.txt
  
## Run the project locally:
  * set DEBUG to True in config.py
  * uvicorn app.main:app --reload --port[PORT_NUMBER]

## In Docker:
    * set DEBUG to False
    * set you DB_NAME, DB_USER, DB_PASSWORD, DB_PORT, DB_LOCALHOST in .env
    
      in docker-compose.yaml
          DATABASE_URL=postgresql://{DB_USER}:{DB_PASSWORD}@db:{DB_PORT}/{DB_NAME}

          POSTGRES_USER={DB_USER}
          POSTGRES_PASSWORD={DB_PASSWORD}
          POSTGRES_DB={DB_NAME}

    *  docker compose up --build
    
 ## Testing endpoints
   - Navigate to /docs
