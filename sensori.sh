#!/bin/bash
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
      "uri": "http://172.18.1.4:5050/sensorBooksNotification",
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
      "uri": "http://172.18.1.4:5050/sensorSeatsNotification",
      "accept": "application/json"
    }
  },
   "@context": "http://context/ngsi-context.jsonld"
}'