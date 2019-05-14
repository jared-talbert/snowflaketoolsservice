#!/usr/bin/env bash
if [ ! -d 'snowflakesqltoolsservice' ] || [ ! -d 'tests' ] || [ ! -d 'snow' ]
then
  echo "Script must be executed from root of repo"
  exit 1
fi

nosetests -a '!is_integration_test' --processes=-1 "$@"