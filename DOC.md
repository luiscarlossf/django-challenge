FORMAT: 1A

# Django Challenge

Django Challenge is a API allowing consumers to list, update and create Regular Plans.

# Group Regular Plan

Resources related to regular plans in the API.

## Regular Plan Collection [/plans]

### List All Questions [GET]

List all public regular plans. 

+ Response 200 (application/json)
        
        [
            {
                "id": 1,
                "name": "1212",
                "tar_included": true,
                "subscription": 1212.0,
                "cycle": "DD",
                "type": "BT",
                "offer_iva": true,
                "off_peak_price": 1212.0,
                "peak_price": 1212.0,
                "unit": "KWH",
                "valid": true,
                "publish": true,
                "vat": 20
            },
            {
                "id": 2,
                "name": "Regular Plan",
                "tar_included": true,
                "subscription": 200.0,
                "cycle": "DD",
                "type": "BT",
                "offer_iva": true,
                "off_peak_price": 200.0,
                "peak_price": 2020.0,
                "unit": "KWH",
                "valid": true,
                "publish": true,
                "vat": 40
            },
            {
                "id": 3,
                "name": "Regular Plan 2",
                "tar_included": true,
                "subscription": 222.0,
                "cycle": "DD",
                "type": "BT",
                "offer_iva": true,
                "off_peak_price": 222.0,
                "peak_price": 2222.0,
                "unit": "KWH",
                "valid": true,
                "publish": true,
                "vat": 40
            }
        ]
### Create a New Question [POST]
Creates a new Regular Plan for the user authenticated.

+ Attributes (Regular Plan)

+ Request (application/json)

+ Response 201 (application/json)

    + Headers
        
            Location: /plans/1/
    
    + Body

            {
                "id": 1,
                "name": "Regular Plan 2",
                "tar_included": true,
                "subscription": 222.0,
                "cycle": "DD",
                "type": "BT",
                "offer_iva": true,
                "off_peak_price": 222.0,
                "peak_price": 2222.0,
                "unit": "KWH",
                "valid": true,
                "publish": true,
                "vat": 40
            }

## Regular Plan [/plans/{plan_id}/]

+ Parameters
    + plan_id (number) - ID of the Regular Plan in form of an integer

+ Attributes
    + id (number)
    
        Identifier of Regular Plan
        
            {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            }
            
    + name (string)
    
        A string with 200 maximum length

            {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Name",
                "help_text": "Name of plan",
                "max_length": 200
            }

    + tar_included (boolean)
    
            {
                "type": "boolean",
                "required": true,
                "read_only": false,
                "label": "Tar Included"
            }
            
    + subscription (number) 
    
        A float number. It's the monthly subscription for the User.
        
            {
                "type": "float",
                "required": true,
                "read_only": false,
                "label": "Subscription",
                "help_text": "It's the monthly subscription for the user"
            }
            
    + cycle (string)
    
        A string with 2 maximun length. Can be 'DD' or 'WK'. More info:
        
            {
                "type": "choice",
                "required": true,
                "read_only": false,
                "label": "Cycle",
                "choices": [
                    {
                        "value": "DD",
                        "display_name": "Daily"
                    },
                    {
                        "value": "WK",
                        "display_name": "Weekly"
                    }
                ]
            }
            
    + type (string)
    
        A string with 2 maximun length. Can be 'BT', 'TT' or 'ST'. More info:
        
            {
                "type": "choice",
                "required": true,
                "read_only": false,
                "label": "Type",
                "choices": [
                    {
                        "value": "BT",
                        "display_name": "Bi-Time"
                    },
                    {
                        "value": "TT",
                        "display_name": "Tri-Time"
                    },
                    {
                        "value": "ST",
                        "display_name": "Simple"
                    }
                ]
            }
            
    + offer_iva (boolean)
        {
            "type": "boolean",
            "required": true,
            "read_only": false,
            "label": "Offer IVA"
        }

    + off_peak_price (number)
        More infos:
        {
            "type": "float",
            "required": true,
            "read_only": false,
            "label": "Off Peak Price"
        }

    + peak_price (number)
    
        More infos:
        
        {
            "type": "float",
            "required": true,
            "read_only": false,
            "label": "Peak Price"
        }

    + unit (string)

                {
                    "type": "choice",
                    "required": true,
                    "read_only": false,
                    "label": "Unit",
                    "choices": [
                        {
                            "value": "KWH",
                            "display_name": "Kilometers/hour"
                        },
                        {
                            "value": "MIN",
                            "display_name": "Minutes"
                        }
                    ]
                }

    + valid (boolean)
    
        More infos: 
        
                {
                    "type": "boolean",
                    "required": true,
                    "read_only": false,
                    "label": "Valid"
                }
                
    + publish (boolean)
    
                {
                    "type": "boolean",
                    "required": true,
                    "read_only": false,
                    "label": "Publish",
                    "help_text": "Indicates if plan can be showed to everyone."
                }
        
    + vat (number)
    
        A positive integer between 1 and 100. More infos:

                {
                    "type": "integer",
                    "required": true,
                    "read_only": false,
                    "label": "Vat",
                    "help_text": "Choose a value from 1 to 100.",
                    "min_value": 1,
                    "max_value": 100
                }

### Update a Regular Plan [PUT]
Users only can update a Regular Plan owns by him.

+ Attributes (Regular Plan)

+ Request (application/json)

+ Response 200 (application/json)

            {
                "id": 3,
                "name": "Regular Plan 2",
                "tar_included": true,
                "subscription": 222.0,
                "cycle": "DD",
                "type": "BT",
                "offer_iva": true,
                "off_peak_price": 222.0,
                "peak_price": 2222.0,
                "unit": "KWH",
                "valid": true,
                "publish": true,
                "vat": 40
            }

## Regular Plan Collection of the User [/plans/list_by_user/]


### List Regular Plans of the User [GET]

+ Response 200 (application/json)

        [
            {
                "id": 1,
                "name": "1212",
                "tar_included": true,
                "subscription": 1212.0,
                "cycle": "DD",
                "type": "BT",
                "offer_iva": true,
                "off_peak_price": 1212.0,
                "peak_price": 1212.0,
                "unit": "KWH",
                "valid": true,
                "publish": true,
                "vat": 20
            },
            {
                "id": 2,
                "name": "Regular Plan",
                "tar_included": true,
                "subscription": 200.0,
                "cycle": "DD",
                "type": "BT",
                "offer_iva": true,
                "off_peak_price": 200.0,
                "peak_price": 2020.0,
                "unit": "KWH",
                "valid": true,
                "publish": true,
                "vat": 40
            },
            {
                "id": 3,
                "name": "Regular Plan 2",
                "tar_included": true,
                "subscription": 222.0,
                "cycle": "DD",
                "type": "BT",
                "offer_iva": true,
                "off_peak_price": 222.0,
                "peak_price": 2222.0,
                "unit": "KWH",
                "valid": true,
                "publish": true,
                "vat": 40
            },
            {
                "id": 4,
                "name": "Regular Plan 3",
                "tar_included": true,
                "subscription": 333.0,
                "cycle": "WK",
                "type": "ST",
                "offer_iva": true,
                "off_peak_price": 333.0,
                "peak_price": 3333.0,
                "unit": "MIN",
                "valid": true,
                "publish": false,
                "vat": 40
            },
            {
                "id": 5,
                "name": "Regular Plan 4",
                "tar_included": true,
                "subscription": 444.0,
                "cycle": "WK",
                "type": "ST",
                "offer_iva": true,
                "off_peak_price": 444.0,
                "peak_price": 4444.0,
                "unit": "KWH",
                "valid": true,
                "publish": false,
                "vat": 100
            }
        ]
