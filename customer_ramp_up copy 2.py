from locust import events

class UserTasks(TaskSet):

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
        try:
            response = self.client.post(
                "/saveentity", data=json.dumps(data), headers=headers
            )
            response.raise_for_status()
            logging.info(
                f"Запрос успешно выполнен! Код ответа: {response.status_code}, Отправлено: {start_time}, Получено: {datetime.now()}, MessageId: {name}"
            )
        except Exception as e:
            logging.error(
                f"Ошибка выполнения запроса. Код ошибки: {e.response.status_code}, Тело ответа: {e.response.text}, Отправлено: {start_time}, Получено: {datetime.now()}, MessageId: {name}"
            )
            events.request_failure.fire(
                request_type="POST",
                name="/saveentity",
                response_time=(datetime.now() - start_time).total_seconds(),
                exception=e,
            )
            self.fail("Request failed")
