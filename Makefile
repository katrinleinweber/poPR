PAT=
origin=katrinleinweber/ViPR-test

run: main.py
	touch $<
	python3 $< --PAT=${PAT} --origin=${origin}
