generate=`python generate.py`

expect "answer=`python answer.py`
send echo "$generate"
"
