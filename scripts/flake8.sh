#!/usr/bin/env bash
if [ ! -d 'snowflakesqltoolsservice' ] || [ ! -d 'tests' ] || [ ! -d 'snow' ]
then
  echo "Script must be executed from root of repo"
  exit 1
fi

flake8 --max-line-length=160 --ignore W605,W503,W504 --builtins psycopg2,snowflakesqltoolsservice,View snowflakesqltoolsservice
flake8 --max-line-length=160 --ignore W605,W503,W504 --builtins psycopg2,snowflakesqltoolsservice,View tests
flake8 --max-line-length=160 --ignore W605,W503,W504 --builtins psycopg2,snowflakesqltoolsservice,View snow