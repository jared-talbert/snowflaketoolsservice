from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
include_files = [('./snowflakesqltoolsservice/pg_exes', './pg_exes')]
buildOptions = dict(packages=['asyncio'], excludes=[], include_files=include_files)

base = 'Console'

executables = [
    Executable('snowflakesqltoolsservice/snowflakesqltoolsservice_main.py', base=base)
]

setup(name='Snowflake Tools Service',
      version='0.1.0',
      description='Carbon data protocol server implementation for Snowflake',
      options=dict(build_exe=buildOptions),
      executables=executables)
