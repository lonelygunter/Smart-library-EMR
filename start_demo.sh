curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Library:library001",
    "type": "Library",              
    "seats": {                   
        "type": "Property",
        "value": "30"
    },                       
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Category:category001",
    "type": "Category",              
    "categoryName": {                   
        "type": "Property",
        "value": "Horror"
    },                       
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Category:category002",
    "type": "Category",              
    "categoryName": {                   
        "type": "Property",
        "value": "Letteratura"
    },                       
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Category:category003",
    "type": "Category",              
    "categoryName": {                   
        "type": "Property",
        "value": "Informatica"
    },                       
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Category:category004",
    "type": "Category",              
    "categoryName": {                   
        "type": "Property",
        "value": "Architettura"
    },                       
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Category:category005",
    "type": "Category",              
    "categoryName": {                   
        "type": "Property",
        "value": "Medicina"
    },                       
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Category:category006",
    "type": "Category",              
    "categoryName": {                   
        "type": "Property",
        "value": "Ingegneria"
    },                       
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Category:category007",
    "type": "Category",              
    "categoryName": {                   
        "type": "Property",
        "value": "Storia"
    },                       
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Category:category008",
    "type": "Category",              
    "categoryName": {                   
        "type": "Property",
        "value": "Geografia"
    },                       
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Person:person001",
    "type": "Person",

    "email": {
        "type": "Property",
        "value": "root@root"
    },
    "password": {
        "type":"Property",
        "value": "63a9f0ea7bb98050796b649e85481845"
    }, 
    "surname": {
        "type": "Property",
        "value": "root"
    },
    "name": {
        "type": "Property",
        "value": "root"
    },
    "courseCode": {
        "type": "Property",
        "value": "Medicina"
    },
    "preferences": {
        "type": "Property",
        "value": [
                "Letteratura",
                "Geografia"]
    },
    "@context": "http://context/ngsi-context.jsonld"
}'


curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Book:book001",
    "type": "Book",

    "isbn": {
        "type": "Property",
        "value": "978-1133970777"
    },
    "title": {
        "type": "Property",
        "value": "Title1"
    },
    "description": {
        "type": "Property",
        "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    },                                                                                                              
    "author": {
        "type": "Property",
        "value": "Mario Rossi"
    },                           
    "category": {                   
        "type": "Property",
        "value": "Letteratura"
    },                     
    "pathimg": {         
        "type": "Property",
        "value": "static/libro7.jpeg"
    },                                             
    "available": {                             
        "type": "Property",
        "value": "0"
    },    
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Book:book002",
    "type": "Book",

    "isbn": {
        "type": "Property",
        "value": "971-1133970777"
    },
    "title": {
        "type": "Property",
        "value": "Title2"
    },
    "description": {
        "type": "Property",
        "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    },                                                                                                              
    "author": {
        "type": "Property",
        "value": "Mario Rossi"
    },                           
    "category": {                   
        "type": "Property",
        "value": "Storia"
    },                     
    "pathimg": {         
        "type": "Property",
        "value": "static/libro8.jpg"
    },                                             
    "available": {                             
        "type": "Property",
        "value": "1"
    },    
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Book:book003",
    "type": "Book",

    "isbn": {
        "type": "Property",
        "value": "978-1133170777"
    },
    "title": {
        "type": "Property",
        "value": "Title3"
    },
    "description": {
        "type": "Property",
        "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    },                                                                                                              
    "author": {
        "type": "Property",
        "value": "Luca Blu"
    },                           
    "category": {                   
        "type": "Property",
        "value": "Architettura"
    },                     
    "pathimg": {         
        "type": "Property",
        "value": "static/libro3.jpg"
    },                                             
    "available": {                             
        "type": "Property",
        "value": "0"
    },    
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Book:book004",
    "type": "Book",

    "isbn": {
        "type": "Property",
        "value": "978-1133170717"
    },
    "title": {
        "type": "Property",
        "value": "Title4"
    },
    "description": {
        "type": "Property",
        "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    },                                                                                                              
    "author": {
        "type": "Property",
        "value": "Luca Blu"
    },                           
    "category": {                   
        "type": "Property",
        "value": "Medicina"
    },                     
    "pathimg": {         
        "type": "Property",
        "value": "static/libro4.jpeg"
    },                                             
    "available": {                             
        "type": "Property",
        "value": "0"
    },    
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Book:book005",
    "type": "Book",

    "isbn": {
        "type": "Property",
        "value": "978-1313171777"
    },
    "title": {
        "type": "Property",
        "value": "Title5"
    },
    "description": {
        "type": "Property",
        "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    },                                                                                                              
    "author": {
        "type": "Property",
        "value": "Armando Blu"
    },                           
    "category": {                   
        "type": "Property",
        "value": "Geografia"
    },                     
    "pathimg": {         
        "type": "Property",
        "value": "static/libro5.jpeg"
    },                                             
    "available": {                             
        "type": "Property",
        "value": "1"
    },    
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Book:book013",
    "type": "Book",

    "isbn": {
        "type": "Property",
        "value": "973-1133170777"
    },
    "title": {
        "type": "Property",
        "value": "Title6"
    },
    "description": {
        "type": "Property",
        "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    },                                                                                                              
    "author": {
        "type": "Property",
        "value": "Roberto Minoza"
    },                           
    "category": {                   
        "type": "Property",
        "value": "Informatica"
    },                     
    "pathimg": {         
        "type": "Property",
        "value": "static/libro9.jpg"
    },                                             
    "available": {                             
        "type": "Property",
        "value": "1"
    },    
    "@context": "http://context/ngsi-context.jsonld"
}'

curl -iX POST 'http://localhost:1026/ngsi-ld/v1/entities/' -H 'Content-Type: application/ld+json' --data-raw '{
    "id": "urn:ngsi-ld:Book:book023",
    "type": "Book",

    "isbn": {
        "type": "Property",
        "value": "973-1133170777"
    },
    "title": {
        "type": "Property",
        "value": "Title7"
    },
    "description": {
        "type": "Property",
        "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    },                                                                                                              
    "author": {
        "type": "Property",
        "value": "Roberto Rossi"
    },                           
    "category": {                   
        "type": "Property",
        "value": "Informatica"
    },                     
    "pathimg": {         
        "type": "Property",
        "value": "static/libro10.jpg"
    },                                             
    "available": {                             
        "type": "Property",
        "value": "0"
    },    
    "@context": "http://context/ngsi-context.jsonld"
}'

#provisioning a service group
curl -iX POST 'http://localhost:4041/iot/services' \
-H 'fiware-service: openiot' \
-H 'fiware-servicepath: /' \
-H 'Content-Type: application/json' \
--data-raw '{
    "services": [
        {
            "apikey": "testapikey",
            "cbroker": "http://orion:1026",
            "entity_type": "Device",
            "resource": "/iot/json",
            "attributes": [
                {
                    "object_id": "m", "name": "motion", "type": "Property"
                },
                {
                    "object_id": "i", "name": "isbn", "type": "Property"
                }
            ],
            "static_attributes": [
                {
                    "name": "category", "type": "Property", "value": "sensor"
                },
                {
                    "name": "supportedProtocol", "type": "Property", "value": "ul20"
                }
            ]
        }
    ]
}'

#provisioning a motion sensor
curl -L -X POST 'http://localhost:4041/iot/devices' \
    -H 'fiware-service: openiot' \
    -H 'fiware-servicepath: /' \
    -H 'Content-Type: application/json' \
--data-raw '{
  "devices": [
    {
      "device_id": "motion001",
      "entity_name": "urn:ngsi-ld:Device:motion001",
      "entity_type": "Device",
      "timezone": "Europe/Rome",
      "attributes": [
        {
          "object_id": "m",
          "name": "motion",
          "type": "Property"
        }
      ],
      "static_attributes": [
        {
          "name": "controlledAsset",
          "type": "Relationship",
          "value": "urn:ngsi-ld:Library:library001"
        }
      ]
    }
  ]
}'

#provisioning a book scanner sensor
curl -L -X POST 'http://localhost:4041/iot/devices' \
    -H 'fiware-service: openiot' \
    -H 'fiware-servicepath: /' \
    -H 'Content-Type: application/json' \
--data-raw '{
  "devices": [
    {
      "device_id": "scanner001",
      "entity_name": "urn:ngsi-ld:Device:scanner001",
      "entity_type": "Device",
      "timezone": "Europe/Rome",
      "attributes": [
        {
          "object_id": "i",
          "name": "isbn",
          "type": "Property"
        }
      ],
      "static_attributes": [
        {
          "name": "controlledAsset",
          "type": "Relationship",
          "value": "urn:ngsi-ld:Library:library001"
        }
      ]
    }
  ]
}'


curl -L -X POST 'http://localhost:1026/ngsi-ld/v1/subscriptions/' \
-H 'Content-Type: application/ld+json' \
-H 'NGSILD-Tenant: openiot' \
--data-raw '{
  "description": "Notificami quando viene prelevato un libro",
  "type": "Subscription",
  "entities": [{"type": "Device"}],
  "watchedAttributes": ["isbn"],
  "notification": {
    "format": "keyValues",
    "endpoint": {
      "uri": "http://10.20.10.100:5050/sensorBooksNotification",
      "accept": "application/json"
    }
  },
   "@context": "http://context/ngsi-context.jsonld"
}'


curl -L -X POST 'http://localhost:1026/ngsi-ld/v1/subscriptions/' \
-H 'Content-Type: application/ld+json' \
-H 'NGSILD-Tenant: openiot' \
--data-raw '{
  "description": "Notificami quando entra o esce qualcuno",
  "type": "Subscription",
  "entities": [{"type": "Device"}],
  "watchedAttributes": ["motion"],
  "notification": {
    "format": "keyValues",
    "endpoint": {
      "uri": "http://10.20.10.100:5050/sensorSeatsNotification",
      "accept": "application/json"
    }
  },
   "@context": "http://context/ngsi-context.jsonld"
}'