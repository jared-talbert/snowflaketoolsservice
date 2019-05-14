{#
 # pgAdmin 4 - Snowflake Tools
 #
 # Copyright (C) 2013 - 2017, The pgAdmin Development Team
 # This software is released under the Snowflake Licence
 #}
{# Change database server password #}
ALTER USER {{conn|qtIdent(user)}} WITH ENCRYPTED PASSWORD {{encrypted_password|qtLiteral}};
