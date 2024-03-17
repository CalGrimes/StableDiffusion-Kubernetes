import json
import redis

class Task:
    def __init__(self, task_id, status='pending', result=None) -> None:
        self.task_id = task_id.replace(" ", "_")
        self.percent_complete = 0
        self.status = status
        self.result = result

    @classmethod
    def get_redis(cls) -> redis.client:
        try:
            cls._redis = redis.Redis(host='localhost', port=6379, db=0)  # Try to connect to Redis instance
        except redis.ConnectionError:
            print("Could not connect to Redis. Skipping Redis operations.")
            cls._redis = None  # Set to None if connection fails
        return cls._redis
    
    @classmethod
    def set_redis_task(cls) -> None:
        redis_instance = cls.get_redis()
        if redis_instance is not None:  # Only perform Redis operations if connection was successful
            # set class as json
            task = cls.__dict__
            task = json.dumps(task)
            redis_instance.set(cls.task_id, task)
            redis_instance.expire(cls.task_id, 1800)
            
    @staticmethod
    def set_task(self, task_id: str, status: str, percent_complete: int, result=None) -> None:
        self.task_id = task_id.replace(" ", "_")
        self.percent_complete = percent_complete
        self.status = status
        self.result = result
        self.set_redis_task()

    