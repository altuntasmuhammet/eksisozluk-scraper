# altuntas-eksisozluk-scraper
altuntas-eksisozluk-scraper

altuntas is a complete eksi-sozluk scraper management system.

## Requirements
Docker 19.03.6+
Compose 1.24.1+

## Setup
1. To make system run
```sh
docker-compose up
```
2. Create super user in web app
```sh
docker exec -it web sh
python manage.py createsuper
```

## Creating scheduled task
1. Enter link given below
http://localhost:8000/admin/django_celery_beat/periodictask/

2. Click add button
![image](https://user-images.githubusercontent.com/38005987/125173177-a69ccc00-e1c6-11eb-877c-da15929f4d72.png)

3. Named scheduled task and select one of task(registered)
![image](https://user-images.githubusercontent.com/38005987/125173344-802b6080-e1c7-11eb-8974-176512f99bfc.png)
4. Create schedule (Only one should be filled)
![image](https://user-images.githubusercontent.com/38005987/125173208-ccc26c00-e1c6-11eb-96d3-980d6c2ab828.png)
5. Extend **Arguments** title and fill **Keyworded arguments** as given below
```
{"keyword": "apache kafka, winter wine"}
```
6. Click save button

## Seeing scraped entries
Enter link given below
http://localhost:8000/admin/scraper/entry/
![image](https://user-images.githubusercontent.com/38005987/125173382-ba94fd80-e1c7-11eb-8612-626ea3622135.png)

## Monitoring tasks
http://localhost:8000/admin/scraper/entry/
![image](https://user-images.githubusercontent.com/38005987/125173390-caacdd00-e1c7-11eb-86fe-971d9c2f1a69.png)
![image](https://user-images.githubusercontent.com/38005987/125173396-d6989f00-e1c7-11eb-9c37-6207b5d5a945.png)

## Architecture
![image](https://user-images.githubusercontent.com/38005987/125174379-cbe10880-e1cd-11eb-9d7a-15d846f4c2b6.png)

# TO dos
1. REST API for obtaining scraped data programmatically
2. React or VueJs frontend for monitoring data
3. Code edit to achive Remote database option

## Notes
I think of creating a scraper managework framework which extends this idea in the project for scraping any other websites or datasource. Please reach me out if you are interested in this kind of project.
