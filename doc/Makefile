# Makefile for building example of unity2junit output in Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
OUTDIR        = $(SOURCEDIR)/generated
BUILDDIR      = _build
PYTHON        = python3
UNITY2JUNIT     = $(PYTHON) -m mlx.unity2junit
ROBOT         = $(PYTHON) -m robot
RM            := rm -rf
ECHO          := echo
CP            := cp

LOG_FILE      = log.html

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

clean:
	$(RM) $(BUILDDIR)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.
html: Makefile
	@$(UNITY2JUNIT) -v
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
