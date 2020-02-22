PAT=
origin=katrinleinweber/poPR

test: main.py
	touch $<
	python3 $< --PAT=${PAT} --origin=${origin}
