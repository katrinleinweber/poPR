PAT=
origin=katrinleinweber/poPR

run: main.py
	touch $<
	python3 $< --PAT=${PAT} --origin=${origin}
