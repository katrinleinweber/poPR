test: main.py
	touch $<
	python3 $< --PAT="${PAT}" --repo="voc/cm"
