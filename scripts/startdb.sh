docker run -d -p 27017:27017 -v ~/Projects/BA/dbdata:/data/db mongo
docker run -d -p 27000:27017 -v ~/Projects/BA/configdbdata:/data/db mongo
docker run -d -p 27070:27017 mongo

