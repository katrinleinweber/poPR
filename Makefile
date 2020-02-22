PAT=
origin=katrinleinweber/poPR-test

run: main.py
	touch $<
	python3 $< --PAT=${PAT} --origin=${origin}
