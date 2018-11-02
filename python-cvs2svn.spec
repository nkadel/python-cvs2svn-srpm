#
# spec file for package python-cvs2svn
#
# Copyright (c) 2018 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL does not include python3 by default
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%else
%global with_python3 0
%endif

# Fedora > 28 no longer publishes python2 by default
%if 0%{?fedora} > 28
%global with_python2 0
%else
%global with_python2 1
%endif

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

# Common SRPM package
Name:           python-cvs2svn
Version:        2.5.0
Release:        0%{?dist}
Url:            http://cvs2svn.tigris.org/
Summary:        CVS to Subversion/git/Bazaar/Mercurial repository converter
License:        Apache-style (FIXME:No SPDX)
Group:          Development/Languages/Python
#Source:         https://files.pythonhosted.org/packages/source/c/cvs2svn/ProjectDocumentList?folderID=2976
Source:	cvs2svn-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{with_python2}
%if 0%{?rhel}
BuildRequires:  python-devel
buildRequires:  python-setuptools
%else
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif # rhel
%endif # with_python2
%if 0%{with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif # with_python3

%if 0%{with_python2}
%package -n python2-cvs2svn
Version:        2.5.0
Release:        0%{?dist}
Url:            http://cvs2svn.tigris.org/
Summary:        CVS to Subversion/git/Bazaar/Mercurial repository converter
License:        Apache-style (FIXME:No SPDX)
%if 0%{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python2-cvs2svn}
%endif # with_python2

%if 0%{with_python3}
%package -n python3-cvs2svn
Version:        2.5.0
Release:        0%{?dist}
Url:            http://cvs2svn.tigris.org/
Summary:        CVS to Subversion/git/Bazaar/Mercurial repository converter
License:        Apache-style (FIXME:No SPDX)
%if 0%{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python3-cvs2svn}
%endif # with_python3

%description
cvs2svn_ is a tool for migrating a CVS repository to Subversion_, git_,
Bazaar_, or Mercurial_. The main design goals are robustness and 100% data
preservation. cvs2svn can convert just about any CVS repository we've ever
seen, including gcc, Mozilla, FreeBSD, KDE, GNOME...

.. _cvs2svn: http://cvs2svn.tigris.org/
.. _Subversion: http://svn.tigris.org/
.. _git: http://git-scm.com/
.. _Bazaar: http://bazaar-vcs.org/
.. _Mercurial: http://mercurial.selenic.com/

cvs2svn infers what happened in the history of your CVS repository and
replicates that history as accurately as possible in the target SCM. All
revisions, branches, tags, log messages, author names, and commit dates are
converted. cvs2svn deduces what CVS modifications were made at the same time,
and outputs these modifications grouped together as changesets in the target
SCM. cvs2svn also deals with many CVS quirks and is highly configurable.
See the comprehensive `feature list`_.

.. _feature list: http://cvs2svn.tigris.org/features.html
.. _documentation: http://cvs2svn.tigris.org/cvs2svn.html

Please read the documentation_ carefully before using cvs2svn.


Latest development version
--------------------------

For general use, the most recent released version of cvs2svn is usually the
best choice. However, if you want to use the newest cvs2svn features or if
you're debugging or patching cvs2svn, you might want to use the trunk version
(which is usually quite stable). To do so, use Subversion to check out a
working copy from http://cvs2svn.tigris.org/svn/cvs2svn/trunk/ using a command
like::

  svn co --username=guest http://cvs2svn.tigris.org/svn/cvs2svn/trunk cvs2svn-trunk

(the password is empty; i.e., just press return).

%if 0%{with_python2}
%description -n python2-cvs2svn
cvs2svn_ is a tool for migrating a CVS repository to Subversion_, git_,
Bazaar_, or Mercurial_. The main design goals are robustness and 100% data
preservation. cvs2svn can convert just about any CVS repository we've ever
seen, including gcc, Mozilla, FreeBSD, KDE, GNOME...

.. _cvs2svn: http://cvs2svn.tigris.org/
.. _Subversion: http://svn.tigris.org/
.. _git: http://git-scm.com/
.. _Bazaar: http://bazaar-vcs.org/
.. _Mercurial: http://mercurial.selenic.com/

cvs2svn infers what happened in the history of your CVS repository and
replicates that history as accurately as possible in the target SCM. All
revisions, branches, tags, log messages, author names, and commit dates are
converted. cvs2svn deduces what CVS modifications were made at the same time,
and outputs these modifications grouped together as changesets in the target
SCM. cvs2svn also deals with many CVS quirks and is highly configurable.
See the comprehensive `feature list`_.

.. _feature list: http://cvs2svn.tigris.org/features.html
.. _documentation: http://cvs2svn.tigris.org/cvs2svn.html

Please read the documentation_ carefully before using cvs2svn.


Latest development version
--------------------------

For general use, the most recent released version of cvs2svn is usually the
best choice. However, if you want to use the newest cvs2svn features or if
you're debugging or patching cvs2svn, you might want to use the trunk version
(which is usually quite stable). To do so, use Subversion to check out a
working copy from http://cvs2svn.tigris.org/svn/cvs2svn/trunk/ using a command
like::

  svn co --username=guest http://cvs2svn.tigris.org/svn/cvs2svn/trunk cvs2svn-trunk

(the password is empty; i.e., just press return).
%endif # with_python2

%if 0%{with_python3}
%description -n python3-cvs2svn
cvs2svn_ is a tool for migrating a CVS repository to Subversion_, git_,
Bazaar_, or Mercurial_. The main design goals are robustness and 100% data
preservation. cvs2svn can convert just about any CVS repository we've ever
seen, including gcc, Mozilla, FreeBSD, KDE, GNOME...

.. _cvs2svn: http://cvs2svn.tigris.org/
.. _Subversion: http://svn.tigris.org/
.. _git: http://git-scm.com/
.. _Bazaar: http://bazaar-vcs.org/
.. _Mercurial: http://mercurial.selenic.com/

cvs2svn infers what happened in the history of your CVS repository and
replicates that history as accurately as possible in the target SCM. All
revisions, branches, tags, log messages, author names, and commit dates are
converted. cvs2svn deduces what CVS modifications were made at the same time,
and outputs these modifications grouped together as changesets in the target
SCM. cvs2svn also deals with many CVS quirks and is highly configurable.
See the comprehensive `feature list`_.

.. _feature list: http://cvs2svn.tigris.org/features.html
.. _documentation: http://cvs2svn.tigris.org/cvs2svn.html

Please read the documentation_ carefully before using cvs2svn.


Latest development version
--------------------------

For general use, the most recent released version of cvs2svn is usually the
best choice. However, if you want to use the newest cvs2svn features or if
you're debugging or patching cvs2svn, you might want to use the trunk version
(which is usually quite stable). To do so, use Subversion to check out a
working copy from http://cvs2svn.tigris.org/svn/cvs2svn/trunk/ using a command
like::

  svn co --username=guest http://cvs2svn.tigris.org/svn/cvs2svn/trunk cvs2svn-trunk

(the password is empty; i.e., just press return).
%endif # with_python3

%prep
%setup -q -n cvs2svn-%{version}

%build
%if 0%{with_python2}
%py2_build
%endif # with_python2
%if 0%{with_python3}
%py3_build
%endif # with_python3

%install
%if 0%{with_python2}
%py2_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cvs2bzr $RPM_BUILD_ROOT%{_bindir}/cvs2bzr2
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cvs2git $RPM_BUILD_ROOT%{_bindir}/cvs2git2
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cvs2svn $RPM_BUILD_ROOT%{_bindir}/cvs2svn2
%if ! 0%{with_python3}
%endif # ! with_python3
%{__ln_s} cvs2bzr2 $RPM_BUILD_ROOT%{_bindir}/cvs2bzr
%{__ln_s} cvs2git2 $RPM_BUILD_ROOT%{_bindir}/cvs2git
%{__ln_s} cvs2svn2 $RPM_BUILD_ROOT%{_bindir}/cvs2svn
%endif # with_python2
%if 0%{with_python3}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cvs2bzr $RPM_BUILD_ROOT%{_bindir}/cvs2bzr3
%{__ln_s} cvs2bzr3  $RPM_BUILD_ROOT%{_bindir}/cvs2bzr
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cvs2git $RPM_BUILD_ROOT%{_bindir}/cvs2git3
%{__ln_s} cvs2git3  $RPM_BUILD_ROOT%{_bindir}/cvs2git
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cvs2svn $RPM_BUILD_ROOT%{_bindir}/cvs2svn3
%{__ln_s} cvs2svn3  $RPM_BUILD_ROOT%{_bindir}/cvs2svn
%py3_install
%endif # with_python3

%clean
rm -rf %{buildroot}

%if 0%{with_python2}
%files -n python2-cvs2svn
%defattr(-,root,root,-)
%{python2_sitelib}/*
%{_bindir}/cvs2bzr2
%{_bindir}/cvs2git2
%{_bindir}/cvs2svn2
%if ! 0%{with_python3}
%{_bindir}/cvs2bzr
%{_bindir}/cvs2git
%{_bindir}/cvs2svn
%endif # ! with_python3
%endif # with_python2

%if 0%{with_python3}
%files -n python3-cvs2svn
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/cvs2bzr3
%{_bindir}/cvs2git3
%{_bindir}/cvs2svn3
%{_bindir}/cvs2bzr
%{_bindir}/cvs2git
%{_bindir}/cvs2svn
%endif # with_python3

%changelog
