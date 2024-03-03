#!/bin/bash

port=12345

pushd $(dirname ${BASH_SOURCE[0]}) > /dev/null
docker run -d \
  -p "${port}":"${port}" \
  -v "$(pwd)/SEALPythonNotebooks":"/notebooks" \
  -w "/notebooks" \
  --name pyseal-jupyter \
  pyseal-lib \
  jupyter notebook --ip=0.0.0.0 --port="${port}"  --allow-root --NotebookApp.token=''

popd > /dev/null

#copy server.py to the container
docker cp $(pwd)/LinReg-pyseal/server.py pyseal-jupyter:/notebooks
#copy linmodel.py to the container
docker cp $(pwd)/LinReg-pyseal/linmodel.py pyseal-jupyter:/notebooks
#copy employee_data.csv to the container
docker cp $(pwd)/LinReg-pyseal/employee_data.csv pyseal-jupyter:/notebooks

sleep 2
open "http://localhost:$port" &
