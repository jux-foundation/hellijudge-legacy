#	makefile
#	Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi

#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.

#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.

#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

JUDGE_ROOT=
JAIL_ROOT=
LOG_DIR=

.PHONY: clean test all install

default:
	@echo    ##################################################################
	@echo    #	                                                              #
	@echo    #	Options:                                                      #
	@echo    #	  make all                                                    #
	@echo    #	  make install                                                #
	@echo    #	  make clean                                                  #
	@echo    #	                                                              #
	@echo    #	  make test                                                   #
	@echo    #	  make compilers                                              #
	@echo    #	                                                              #
	@echo    #	                                                              #
	@echo    #	                                                              #
	@echo    ##################################################################

all: jail log problems test 

install:
	mv hellijudge-jail /mnt/jail
	cp utils/daemon.sh /usr/bin/daemon.sh

clean:
	rm -f salam

test:
	cd utils
	@echo "Testing normal judging (hellow problem) ..."
	. hellow-tester.sh
	@echo "Testing interactive judging (bs problem) ..."
	. bs-tester.sh
	cd ..

problems:
	cd problems
	for problem in `ls`
	do
		cd $(problem)
		g++ tester.cpp -o tester
		cd ..
	done
	cd ..

jail: hellijudge-jail

hellijudge-jail:
	git clone https://github.com/jux-foundation/hellijudge-jail.git
	@echo    ##################################################################
	@echo    #                                                                #
	@echo    # 	  For more jail options go to hellijudge-jail directory and	  #
	@echo    #    type: `make`                                                #
	@echo    #                                                                #
	@echo    ##################################################################

log:
	mkdir /var/log/jury
	ln -s /var/log/jury $(JUDGE_ROOT)/log

#mysql:
