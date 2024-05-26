
# scrapping-yp

Scrapping and extract necessary info from Yellow Pages with defined number of returned results & keyword to search

### Extracted info

extract info about phone number , category , address , title , description , website_url , logo_url

if these info exists  

### Inspecting Yellow Pages

- render 26 card info per page

- every 3 cad info have a breaker card which just exists but not include data

- so the final cards including data is `20` per page

- pagination handling using keyword `p` like p1 , p2 , ... etc

- fields like phone_number not being shown unless button click

- fields like description , image_url , website_url may or may not exists

- from code side any field not exists set it as `N/A`

- while my scrapping i don't need any proxies also the maxim scrapping 10, so no need to add them as per this scope 

- min and default is 30 and max is 100

 ### Usage Example 
 - blow is screen recorder for consuming api application on this app 
 - screen recorder link: https://calipio.com/app/play/w3Y5TpBb#n8tPPf7d

### API end point

- the blow url is `postman collection` including scrapping data and various conditions

- you can load it directly into postman

- Postman Collection link: https://winter-desert-603042.postman.co/workspace/GitHub-~83d00952-4216-4e33-889c-2957a579fafc/collection/6749950-78ca4c0f-8e8c-4727-8da9-173255c10a14?action=share&creator=6749950

- post request end point `http:127.0.0.1:8000/api/scrape-yp/`

  

### Data sample

- sample data include with name `response.json` scrapped 100 card of data for search results `restaurants`

  

### Date export

- data being exported directly into mongodb `hosted online` for sample storage

- if the data scrapped in the same day , app will load it directly from db  

### ENVvariables 

- application depend on some environment variables 

|Name  |  Description|
|--|--|
|  MONGO_USER| mongo username |
|MONGO_PASSWORD| mongo password |
|MONGO_DB_NAME| mongo db name|
|MONGO_COLLECTION_NAME| mongo collection name|


### Prerequisites
- machine with ubuntu 
- python v3.10 
- poetry package for management projects 
    `pip install poetry ` 

### Operate Locally 
- create `.env` file in root folder of application 
- set ENV variables with proper values as named above `ENVvariables Section`
- clone project from Github 
	`git clone https://github.com/BakrFrag/scrapping-yp`
- cd into project folder 
	`cd scrapping-yp`
- activate shell 
	`poetry shell` 
- install dependencies
`poetry install`
- start play 
	- will activate endpoint listening on 8000 on localhost 127.0.0.1 `http://127.0.0.1:8000/api/scrape-yp`
	- `python src/app.py` 

### Application  Logging 
- logging enable via application to track application behavior
- application level `DEBUG` 
### End Points 
- `http://127.0.0.1:8000/api/scrape-yp/`
- post request 
- if data scrapped in the same day data will be returned directly from `MongoDB` if not 
- app will define pages to scrape and results per each page 
- Request Body 

|Number  | Keyword |
|--|--|
| number |  number of result to scrape min and default 30 and max is 100|
|keyword| the keyword to search on Yellow Pages|

- Response Model 
- list of json include fields 

|Name| Description |
|--|--|
|  phone_number| phone_number if exists else "N/A"  |
|  title| title if exists else "N/A"  |
|  description| description if exists else "N/A"  |
|  address| address if exists else "N/A"  |
|  website_url| website_url if exists else "N/A"  |
|  image_url| image_url if exists else "N/A"  |
|  category| category if exists else "N/A"  |
|  date| date field when data inserted or scrapped   |
 



### Application Build 
- this application build using Python v3.10 
- libraries 

|Library | Usage  |
|--|--|
| FastAPI  | web framework for python web application micro-services   |
|uvicorn | asgi application for serving and running application|
| pydantic| python library for data validation using pandas |
| selenium | dynamic web scrapping |
|python-dotenv| python library for managing secrets and sensitive data|
|pymongo| python client for mongo db |

### Future Enhancements 
- add choices to export data along with store it like export data in `excel`  , `csv` or save it directly to hard disk 
- add options to scrape with commands on terminal like `CLI` application and take other arguments for terminal 
