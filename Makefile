OPENTAB_DEVEL_PATH = ~/.opentab/devel/
TABS_FILE = tabs.yml
OPENTAB_FILE_PATH = ${OPENTAB_DEVEL_PATH}${TABS_FILE}
PYTHON_PATH = /usr/bin/env python
OPENTAB_MAIN_PATH = src/devel/init_devel.py

.PHONY: devel-up
devel-up:
	@echo 'Creating devel environment'
	@if [ ! -d $(OPENTAB_DEVEL_PATH) ]; then \
	echo 'Creating the devel dir.'; \
	mkdir -p ${OPENTAB_DEVEL_PATH}; \
	echo 'Creating and initializing the devel tabs.yml file'; \
	${PYTHON_PATH} ${OPENTAB_MAIN_PATH}; \
	else \
	echo 'Devel environment already created!'; fi
	
.PHONY: devel-down
devel-down:
	@echo 'Destroying the devel environment...'
	@if [ -d ${OPENTAB_DEVEL_PATH} ]; then \
	echo 'Removing the devel folder.'; \
	rm -r ${OPENTAB_DEVEL_PATH}; \
	else \
	echo 'No devel environment found.'; fi