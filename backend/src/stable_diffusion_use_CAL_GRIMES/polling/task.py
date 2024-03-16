import redis

class Task:
    def __init__(self, task_id, status='pending', result=None):
        self.task_id = task_id
        self.percent_complete = 0
        self.status = status
        self.result = result

    @classmethod
    def get_redis(cls):
        if not hasattr(cls, "_redis"):
            cls._redis = redis.Redis(host='localhost', port=6379, db=0)  # Connect to Redis instance
        return cls._redis

    def __call__(self, task_id: str, status: str, percent_complete: int):
        self.get_redis().hset(task_id, 'status', status)
        self.get_redis().hset(task_id, 'percent_complete', percent_complete)

    def update_task_status(self, task_id: str, new_status: str):
        self.get_redis().hset(task_id, 'status', new_status)