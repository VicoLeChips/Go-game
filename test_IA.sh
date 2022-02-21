#!/bin/bash
touch .tmp_test_ia_rec.pg

for ((i = 1; i <= $3; i++)); do
	python3.5 PyGo.py -q -m --player1 $1 --player2 $2 >> .tmp_test_ia_rec.pg
done

python3.5 parse_result.py

rm .tmp_test_ia_rec.pg

