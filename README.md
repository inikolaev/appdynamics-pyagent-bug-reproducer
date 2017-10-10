# Reproducer for a problem in AppDynamics PyAgent

The following error occurs when accessing database and using `NamedTupleCursor`:

```
Traceback (most recent call last):
  File "/app/main.py", line 37, in context_db_cursor
    yield (db, cursor)
  File "/app/main.py", line 50, in root
    return cursor.fetchone().pong
AttributeError: 'tuple' object has no attribute 'pong'
```

The code expects a `namedtuple` to be returned from `cursor.fetchone()` call, but it looks like `pyagent` does not recognize it and simply converts it to `tuple` instead.

## Prerequisites

You would need the following software in order to run this reproducer:

* Docker, which can be downloader from [https://www.docker.com/community-edition](https://www.docker.com/community-edition)


## Running reproducer

There are two modes to run the reproducer: with `pyagent` enabled or disabled.

The following command will run reproducer with `pyagent` enabled:

```
docker-compose up
```

In order to disable it you need to set `MODE` environment variable to value `nopyagent`:

```
MODE=nopyagent docker-compose up
```

This would start PostgreSQL database along with the reproducer container.

No you can open up you browser and access reproducer at [http://localhost:8080/](http://localhost:8080/)

## Building the reproducer

When you run `docker-compose up` for the first time Docker Compose will build image automatically.

But if you want to make any changes then you have to rebuild it with the following command

```
docker-compose build
```

and start again with

```
docker-compose up
```