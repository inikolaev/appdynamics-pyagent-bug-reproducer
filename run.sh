#!/bin/bash

if [[ $MODE == "pyagent" ]]; then
  pyagent run \
    -c appdynamics.cfg \
    --node test_node \
    -- gunicorn --bind 0.0.0.0:8080 \
    --workers 1 \
    --worker-class gevent \
    --log-level info \
    --reload \
    main:app
else
  gunicorn --bind 0.0.0.0:8080 \
    --workers 1 \
    --worker-class gevent \
    --log-level info \
    --reload \
    main:app
fi

