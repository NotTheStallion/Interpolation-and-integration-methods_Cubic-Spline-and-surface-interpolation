all: report clean

report:
	pdflatex -interaction batchmode report.tex
	pdflatex -interaction batchmode report.tex

verbose:
	pdflatex report.tex
	pdflatex report.tex

test:
	@set -e ; \
	for file in src/test*.py ; do \
		echo -e "\n===== TESTS $$file =====" ; \
		python3 $$file ; \
	done
	@echo

clean:
	rm -rf *.log *.aux *.toc *.out sections/*.aux

.PHONY: all verbose test clean
