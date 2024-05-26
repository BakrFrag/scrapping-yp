# scrapping-yp
Scrapping and extract necessary info from YP with definded number of returned results & keyword to search 

### Extracted info 

extract info about phone number , category , address , title , description , website_url , logo_url 
if these info exists 

### Inspecting Yellow Pages 
- render 26 card info per page 
- every 3 cad info have a breaker card which just exists but not include data 
- so the final cards including data is `20` per page 
- pagination handling using keyword `p`  like p1 , p2 , ... etc 
- fields like phone_number not being shown unless button click 
- fields like description , image_url , website_url may or may not exists 
- from code side any field not exists set it as `N/A` 
- while scrapping i don't need any proxies also the maxium scrapping 10 
- min and default is 30 and max is 100 

### API end point 

- the blow url is `postman collection` including scrapping data and various conditions 
- you can load it directly into postman 
- Postman Collection link
- post request end point `http:127.0.0.1:8000/api/scrape-yp/`

### Data sample 
- sample data include with name `response.json` scrapped 100 card of data for search results `restaurants`

### Date export 
- data being exported directly into mongodb `hosted online` for sample storage 
- if the data scrapped in the same day , app will load it directly from db 


### ENV variables 
- application depend on some application variables 

