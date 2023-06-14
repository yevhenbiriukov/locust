from locust import HttpUser, task, between
import json
import uuid
import random
import string
import logging
from datetime import datetime
from faker import Faker

fake = Faker("ru_RU")

logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class MyLocust(HttpUser):
    def generate_random_code(self, length):
        return "".join(random.choices(string.digits, k=length))

    def generate_random_string(self, length):
        return "".join(random.choices(string.ascii_letters, k=length))

    @task
    def my_task(self):
        wait_time = between(1, 1)
        name = fake.first_name()
        headers = {"Content-Type": "application/json"}
        data = {
            "MessageId": "884188e2-14d7-45ae-bbaa-0ba18779587b",
            "Entity": {
                "messageId": str(uuid.uuid4()),
                "entityName": "Customers",
                "isMasterData": True,
                "sourceName": "sap",
                "destName": "mdm",
                "userId": "NAVICONS\\agrigoryeva",
                # "userName": None,
                "modelId": 1,
                "parameters": [],
                "action": "create",
                "entityData": {
                    "primitiveEntityName": "Customer",
                    "sourceCode": self.generate_random_code(10),
                    # "mdmCode": None,
                    # "destCode": None,
                    "attributes": [
                        {
                            "name": "Surname",
                            "attributeType": 0,
                            # "value": self.generate_random_string(8)
                            "value": fake.last_name(),
                        },
                        {
                            "name": "Name",
                            "attributeType": 0,
                            # "value": self.generate_random_string(8)
                            "value": name,
                        },
                        {
                            "name": "MiddleName",
                            "attributeType": 0,
                            # "value": None
                        },
                        {
                            "name": "Birthday",
                            "attributeType": 6,
                            # "value": None
                        },
                        {
                            "name": "MaritalStatus",
                            "attributeType": 0,
                            # "value": None
                        },
                        {
                            "name": "MarketingAgree",
                            "attributeType": 3,
                            # "value": None
                        },
                        {
                            "name": "PersonalDataAgree",
                            "attributeType": 3,
                            # "value": None
                        },
                        {
                            "name": "ResearchAgree",
                            "attributeType": 3,
                            # "value": None
                        },
                        {
                            "name": "SuppressAllCalls",
                            "attributeType": 3,
                            # "value": None
                        },
                        {
                            "name": "SuppressAllEmails",
                            "attributeType": 3,
                            # "value": None
                        },
                        {
                            "name": "SuppressAllMessages",
                            "attributeType": 3,
                            # "value": None
                        },
                        {
                            "name": "EmailBounceBlock",
                            "attributeType": 3,
                            # "value": None
                        },
                        {
                            "name": "AddressBounceBlock",
                            "attributeType": 3,
                            # "value": None
                        },
                        {
                            "name": "CustomerGender",
                            "attributeType": 4,
                            "value": "Женский",
                        },
                        {
                            "name": "phonemobile",
                            "attributeType": 0,
                            # "value": None
                        },
                        {
                            "name": "phonework",
                            "attributeType": 0,
                            # "value": None
                        },
                        {
                            "name": "phonehome",
                            "attributeType": 0,
                            "value": "+79993658511",
                        },
                        {
                            "name": "mail",
                            "attributeType": 0,
                            # "value": None
                        },
                        {
                            "name": "IsSuspicious",
                            "attributeType": 3,
                            # "value": None
                        },
                        {
                            "name": "Reason",
                            "attributeType": 0,
                            # "value": None
                        },
                        {
                            "name": "SuppressAllSMS",
                            "attributeType": 0,
                            # "value": None
                        },
                    ],
                    "linkAttributes": [
                        {
                            "name": "CustomerType",
                            "entityName": "CustomerType",
                            # "entitySourceCode": None,
                            # "entityDestCode": None,
                            # "entityMdmCode": None,
                            # "title": None,
                            # "isMultiLink": None
                        },
                        {
                            "name": "PreferredDealer",
                            "entityName": "Dealers",
                            # "entitySourceCode": None,
                            # "entityDestCode": None,
                            # "entityMdmCode": None,
                            # "title": None,
                            # "isMultiLink": None
                        },
                        {
                            "name": "SalesDealer",
                            "entityName": "Dealers",
                            # "entitySourceCode": None,
                            # "entityDestCode": None,
                            # "entityMdmCode": None,
                            # "title": None,
                            # "isMultiLink": None
                        },
                        {
                            "name": "ServiceDealer",
                            "entityName": "Dealers",
                            # "entitySourceCode": None,
                            # "entityDestCode": None,
                            # "entityMdmCode": None,
                            # "title": None,
                            # "isMultiLink": None
                        },
                    ],
                },
            },
        }
        start_time = datetime.now()
        response = self.client.post(
            "/saveentity", data=json.dumps(data), headers=headers
        )
        end_time = datetime.now()  # Записываем время получения ответа
        if response.status_code == 200:
            logging.info(
                f"Запрос успешно выполнен! Код ответа: {response.status_code}, Отправлено: {start_time}, Получено: {end_time}, MessageId: {name}"
            )
            self.last_response_status_code = response.status_code
        else:
            logging.error(
                f"Ошибка выполнения запроса. Код ошибки: {response.status_code}, Тело ответа: {response.text}, Отправлено: {start_time}, Получено: {end_time}, MessageId: {name}"
            )
            self.last_response_status_code = response.status_code
            if self.last_response_status_code != 200:
                
                self.stop(True)
