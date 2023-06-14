{
    "MessageId": "884188e2-14d7-45ae-bbaa-0ba18779587b",
    "Entity":
    {
        "messageId": str(uuid.uuid4()),
        "entityName": "Customers",
        "isMasterData": True,
        "sourceName": "sap",
        "destName": "mdm",
        "userId": "NAVICONS\\agrigoryeva",
        "userName": None,
        "modelId": 1,
        "parameters": [],
        "action": "create",
        "entityData": {
            "primitiveEntityName": "Customer",
            "sourceCode": generate_random_code(10),
            "mdmCode": None,
            "destCode": None,
            "attributes": [
                {
                    "name": "Surname",
                    "attributeType": 0,
                    "value": generate_random_string(8)
                },
                {
                    "name": "Name",
                    "attributeType": 0,
                    "value": generate_random_string(8)
                },
                {
                    "name": "MiddleName",
                    "attributeType": 0,
                    "value": None
                },
                {
                    "name": "Birthday",
                    "attributeType": 6,
                    "value": None
                },
                {
                    "name": "MaritalStatus",
                    "attributeType": 0,
                    "value": None
                },
                {
                    "name": "MarketingAgree",
                    "attributeType": 3,
                    "value": None
                },
                {
                    "name": "PersonalDataAgree",
                    "attributeType": 3,
                    "value": None
                },
                {
                    "name": "ResearchAgree",
                    "attributeType": 3,
                    "value": None
                },
                {
                    "name": "SuppressAllCalls",
                    "attributeType": 3,
                    "value": None
                },
                {
                    "name": "SuppressAllEmails",
                    "attributeType": 3,
                    "value": None
                },
                {
                    "name": "SuppressAllMessages",
                    "attributeType": 3,
                    "value": None
                },
                {
                    "name": "EmailBounceBlock",
                    "attributeType": 3,
                    "value": None
                },
                {
                    "name": "AddressBounceBlock",
                    "attributeType": 3,
                    "value": None
                },
                {
                    "name": "CustomerGender",
                    "attributeType": 4,
                    "value": "Женский"
                },
                {
                    "name": "phonemobile",
                    "attributeType": 0,
                    "value": None
                },
                {
                    "name": "phonework",
                    "attributeType": 0,
                    "value": None
                },
                {
                    "name": "phonehome",
                    "attributeType": 0,
                    "value": "+79993658511"
                },
                {
                    "name": "mail",
                    "attributeType": 0,
                    "value": None
                },
                {
                    "name": "IsSuspicious",
                    "attributeType": 3,
                    "value": None
                },
                {
                    "name": "Reason",
                    "attributeType": 0,
                    "value": None
                },
                {
                    "name": "SuppressAllSMS",
                    "attributeType": 0,
                    "value": None
                }
            ],
            "linkAttributes": [
                {
                    "name": "CustomerType",
                    "entityName": "CustomerType",
                    "entitySourceCode": None,
                    "entityDestCode": None,
                    "entityMdmCode": None,
                    "title": None,
                    "isMultiLink": None
                },
                {
                    "name": "PreferredDealer",
                    "entityName": "Dealers",
                    "entitySourceCode": None,
                    "entityDestCode": None,
                    "entityMdmCode": None,
                    "title": None,
                    "isMultiLink": None
                },
                {
                    "name": "SalesDealer",
                    "entityName": "Dealers",
                    "entitySourceCode": None,
                    "entityDestCode": None,
                    "entityMdmCode": None,
                    "title": None,
                    "isMultiLink": None
                },
                {
                    "name": "ServiceDealer",
                    "entityName": "Dealers",
                    "entitySourceCode": None,
                    "entityDestCode": None,
                    "entityMdmCode": None,
                    "title": None,
                    "isMultiLink": None
                }
            ]
        }
    }
}
