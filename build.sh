#!/bin/bash

docker build -t pyseal-lib -f Dockerfile .

## uncomment this if you need to force a rebuild without cache 
## only use this if the changes you added do not take effects
## this happens in certain instances.
# docker build --no-cache -t pyseal-lib -f Dockerfile .