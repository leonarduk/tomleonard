#!/bin/bash
echo “Testing lambda”
lambda="lamda_function.py"
json="cloudwatch-scheduled-event.json"
export expected="Fused Glass jewellery"
export site="http://glassandsilverjewellery.co.uk/"
python-lambda-local -f lambda_handler $lambda $json