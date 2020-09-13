#docker run -d -p 8000:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin quay.io/keycloak/keycloak:latest


#docker run -d --name postgres -v ~/Projects/BA/pdbdata/main:/var/lib/postgresql/9.3/main -v ~/Projects/BA/pbdata/data:/var/lib/postgresql/data --net keycloak-network -e POSTGRES_DB=keycloak -e POSTGRES_USER=keycloak -e POSTGRES_PASSWORD=password postgres

docker network create keycloak-network

docker run -d --name postgres -v ~/Projects/BA/pbdata/data:/var/lib/postgresql/data --net keycloak-network -e POSTGRES_DB=keycloak -e POSTGRES_USER=keycloak -e POSTGRES_PASSWORD=password postgres


cp realm-export.json /tmp/example-realm.json

docker run -d --name keycloak -p 8000:8080 --net keycloak-network -e DB_ADDR=postgres -e DB_USER=keycloak -e DB_PASSWORD=password  -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin  -e KEYCLOAK_IMPORT=/tmp/example-realm.json -v /tmp/example-realm.json:/tmp/example-realm.json jboss/keycloak
