import traceback


class RedisKeyNotFoundError(Exception):
    pass


def redis_get(key):
    raise RedisKeyNotFoundError(f"redis db couldn't find key {key}")


# you are working with a specific database (redis) which introduces its own exceptions.
# when your database raises exception, you can't let it propagate up to the client because it will reveal your
# implementation details (client shouldn't get redis errors and code logic around it...)
# fix the code below so that RedisKeyNotFoundError will be raised as standard KeyError(f"key {key} not found").
def my_get(key):

    raise NotImplementedError("YOUR IMPLEMENTATION HERE")

    redis_get(key)


try:
    my_get("some_key")
except Exception as e:
    traceback.print_exc()
