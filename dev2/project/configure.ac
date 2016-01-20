#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.67])
AC_INIT([mistery_foo], [1.0], [fengyh7@gmail.com])
AC_CONFIG_SRCDIR([src/main/main.c])
AC_CONFIG_HEADERS([config.h])
AM_INIT_AUTOMAKE([1.9 foreign])

# Checks for programs.
AC_PROG_CC

# Checks for libraries.
AC_PROG_RANLIB
AC_SEARCH_LIBS([mistery_value], [magic voodoo mistery], [], [])

# Checks for header files.
AC_RUN_IFELSE(
 [AC_LANG_PROGRAM(
  [[#include <mistery.h>]],
  [[mistery_value(2);]])
 ],
 [AC_DEFINE([MISTERY_VALUE_ONEPARAM], [2], [victory])],
 []
)
# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.
AC_CONFIG_FILES([Makefile src/Makefile src/lib_foo/Makefile src/main/Makefile])

AC_OUTPUT
