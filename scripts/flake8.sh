#!/usr/bin/env bash
if [ ! -d 'snowflaketoolsservice' ] || [ ! -d 'tests' ] || [ ! -d 'snow' ]
then
  echo "Script must be executed from root of repo"
  exit 1
fi

flake8 --max-line-length=160 --ignore W605,W503,W504 --builtins psycopg2,snowflaketoolsservice,View snowflaketoolsservice
flake8 --max-line-length=160 --ignore W605,W503,W504 --builtins psycopg2,snowflaketoolsservice,View tests
flake8 --max-line-length=160 --ignore W605,W503,W504 --builtins psycopg2,snowflaketoolsservice,View snow