#
# Build mock and local RPM versions of python modules
#

# Assure that sorting is case sensitive
LANG=C

# Ignore ownership and group,
RSYNCOPTS=-a --no-owner --no-group
# Skip existing files to avoid binary churn in yum repos
RSYNCSAFEOPTS=$(RSYNCOPTS) --ignore-existing 

# "mock" configurations to build with, activate only as needed
MOCKS+=fedora-29-x86_64
MOCKS+=fedora-28-x86_64
MOCKS+=epel-7-x86_64
MOCKS+=epel-6-x86_64

# Local yum compatible RPM repository
REPOBASEDIR="`/bin/pwd | xargs dirname`/py2packrepo"

# Deduce local package names and .spec files, for universe Makefile use
SPEC := `ls *.spec | head -1`
PKGNAME := "`ls *.spec | head -1 | sed 's/.spec$$//g'`"

all:: verifyspec
# Needed for yum repo updates
all:: /usr/bin/createrepo
all:: $(MOCKS)

# Oddness to get deduced .spec file verified
verifyspec:: FORCE
	@if [ ! -e $(SPEC) ]; then \
	    echo Error: SPEC file $(SPEC) not found, exiting; \
	    exit 1; \
	fi

# Needed for correct srpm and build format
#build srpm:: /etc/rpm/macros.python27-config

srpm:: verifyspec FORCE
	@echo "Building $(SPEC) SRPM"
	rm -rf rpmbuild
	rpmbuild --define '_topdir $(PWD)/rpmbuild' \
		--define '_sourcedir $(PWD)' \
		-bs $(SPEC) --nodeps

# Needed for python27 compatible compilation
build:: srpm FORCE
	rpmbuild --define '_topdir $(PWD)/rpmbuild' \
		--rebuild rpmbuild/SRPMS/*.src.rpm

$(MOCKS):: verifyspec FORCE
	@if [ -n "`find $@ -name \*.rpm ! -name \*.src.rpm 2>/dev/null`" ]; then \
		echo "	Skipping $(SPEC) in $@ with RPMS"; \
	else \
		echo "	Building $@ SRPM with $(SPEC)"; \
		rm -rf $@; \
		mock -r $@ \
		    --resultdir=$(PWD)/$@ \
		    --sources=$(PWD) --buildsrpm --spec=$(SPEC); \
		echo "Storing $@/*.src.rpm in $@.src.rpm"; \
		/bin/mv $@/*.src.rpm $@.src.rpm; \
		echo "Building $@.src.rpm in $@"; \
		rm -rf $@; \
		mock -r $@ \
		    --resultdir=$(PWD)/$@ \
		    $@.src.rpm; \
	fi

mock:: $(MOCKS)

clean::
	rm -rf $(MOCKS)
	rm -rf rpmbuild
	rm -rf *.rpm

realclean distclean:: clean
	rm -f *.src.rpm

FORCE:
