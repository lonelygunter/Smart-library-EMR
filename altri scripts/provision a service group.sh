#!/bin/bash
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
            "resource": "/iot/d",
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