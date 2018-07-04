
TARGET = worksheet

all: $(TARGET).pdf

$(TARGET).pdf: $(TARGET).dvi
	dvipdfmx $(TARGET).dvi

$(TARGET).dvi: $(TARGET).tex
	platex $(TARGET).tex

$(TARGET).tex: top.tex bottom.tex a.tex
	cat top.tex a.tex bottom.tex > $(TARGET).tex

a.tex: gen.py FORCE
	python3 gen.py > a.tex

FORCE:
