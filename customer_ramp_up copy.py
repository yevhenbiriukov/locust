from locust import HttpUser, TaskSet, task, constant, between
import json
from datetime import datetime
import math
import logging
from locust import LoadTestShape
import random
import string
import uuid
from faker import Faker

fake = Faker("ru_RU")

logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class UserTasks(TaskSet):
    def generate_random_code(self, length):
        return "".join(random.choices(string.digits, k=length))

    def generate_random_string(self, length):
        return "".join(random.choices(string.ascii_letters, k=length))

    @task
    def my_task(self):
        name = fake.first_name()
        headers = {"Content-Type": "application/json"}
        data = {
            "messageId": str(uuid.uuid4()),
            "sourceCode": self.generate_random_code(10),
            "value": fake.last_name(),
        }
        start_time = datetime.now()
        response = self.client.post(
            "/saveentity", data=json.dumps(data), headers=headers
        )
        end_time = datetime.now()
        if response.status_code == 200:
            logging.info(
                f"Запрос успешно выполнен! Код ответа: {response.status_code}, Отправлено: {start_time}, Получено: {end_time}, MessageId: {name}"
            )
        else:
            logging.error(
                f"Ошибка выполнения запроса. Код ошибки: {response.status_code}, Тело ответа: {response.text}, Отправлено: {start_time}, Получено: {end_time}, MessageId: {name}"
            )


class MyLocust(HttpUser):
    tasks = [UserTasks]
    wait_time = between(1, 1)


class StepLoadShape(LoadTestShape):
    """
    A step load shape
    Keyword arguments:
        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds
    """

    step_time = 1
    step_load = 10
    spawn_rate = 10
    time_limit = 12

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return (current_step * self.step_load, self.spawn_rate)
