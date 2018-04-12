
class ConstantsObj(object):
    def __getattribute__(self,name):
        val=object.__getattribute__(self,name)
        if name.startswith('__'):
            return val
        else:
            return val()



    def add_drop_database(self):
        """--add-drop-database
Add a DROP DATABASE statement before each CREATE DATABASE  statement"""
        return """--add-drop-database"""


    def add_drop_table(self):
        """--add-drop-table
Add a DROP TABLE statement before each CREATE TABLE statement"""
        return """--add-drop-table"""


    def add_drop_trigger(self):
        """--add-drop-trigger
Add a DROP TRIGGER statement before each CREATE TRIGGER statement"""
        return """--add-drop-trigger"""


    def add_locks(self):
        """--add-locks
Surround each table dump with LOCK TABLES and UNLOCK TABLES  statements"""
        return """--add-locks"""


    def all_databases(self):
        """--all-databases
Dump all tables in all databases"""
        return """--all-databases"""


    def allow_keywords(self):
        """--allow-keywords
Allow creation of column names that are keywords"""
        return """--allow-keywords"""


    def apply_slave_statements(self):
        """--apply-slave-statements
Include STOP SLAVE prior to CHANGE MASTER statement and START  SLAVE at end of output"""
        return """--apply-slave-statements"""


    def bind_address(self):
        """--bind-address=ip_address
Use the specified network interface to connect to the MySQL Server"""
        return """--bind-address=ip_address"""


    def comments(self):
        """--comments
Add comments to the dump file"""
        return """--comments"""


    def compact(self):
        """--compact
Produce more compact output"""
        return """--compact"""


    def compatible(self):
        """--compatible=name[,name,...]
Produce output that is more compatible with other database systems  or with older MySQL servers"""
        return """--compatible=name[,name,...]"""


    def complete_insert(self):
        """--complete-insert
Use complete INSERT statements that include column names"""
        return """--complete-insert"""


    def create_options(self):
        """--create-options
Include all MySQL-specific table options in CREATE TABLE  statements"""
        return """--create-options"""


    def databases(self):
        """--databases
Dump several databases"""
        return """--databases"""


    def debug(self):
        """--debug[=debug_options]
Write a debugging log"""
        return """--debug[=debug_options]"""


    def debug_check(self):
        """--debug-check
Print debugging information when the program exits"""
        return """--debug-check"""


    def debug_info(self):
        """--debug-info
Print debugging information, memory and CPU statistics when the  program exits"""
        return """--debug-info"""


    def default_auth(self):
        """--default-auth=plugin
The authentication plugin to use"""
        return """--default-auth=plugin"""


    def default_character_set(self):
        """--default-character-set=charset_name
Use charset_name as the default character set"""
        return """--default-character-set=charset_name"""


    def delayed_insert(self):
        """--delayed-insert
Write INSERT DELAYED statements rather than INSERT statements"""
        return """--delayed-insert"""


    def delete_master_logs(self):
        """--delete-master-logs
On a master replication server, delete the binary logs after  performing the dump operation"""
        return """--delete-master-logs"""


    def disable_keys(self):
        """--disable-keys
For each table, surround the INSERT statements with statements to  disable and enable keys"""
        return """--disable-keys"""


    def dump_date(self):
        """--dump-date
Include dump date as "Dump completed on" comment if --comments is  given"""
        return """--dump-date"""


    def dump_slave(self):
        """--dump-slave[=value]
Include CHANGE MASTER statement that lists binary log coordinates  of slave's master"""
        return """--dump-slave[=value]"""


    def events(self):
        """--events
Dump events from the dumped databases"""
        return """--events"""


    def extended_insert(self):
        """--extended-insert
Use multiple-row INSERT syntax that include several VALUES lists"""
        return """--extended-insert"""


    def fields_enclosed_by(self):
        """--fields-enclosed-by=string
This option is used with the --tab option and has the same meaning  as the corresponding clause for LOAD DATA INFILE"""
        return """--fields-enclosed-by=string"""


    def fields_escaped_by(self):
        """--fields-escaped-by
This option is used with the --tab option and has the same meaning  as the corresponding clause for LOAD DATA INFILE"""
        return """--fields-escaped-by"""


    def fields_optionally_enclosed_by(self):
        """--fields-optionally-enclosed-by=string
This option is used with the --tab option and has the same meaning  as the corresponding clause for LOAD DATA INFILE"""
        return """--fields-optionally-enclosed-by=string"""


    def fields_terminated_by(self):
        """--fields-terminated-by=string
This option is used with the --tab option and has the same meaning  as the corresponding clause for LOAD DATA INFILE"""
        return """--fields-terminated-by=string"""


    def flush_logs(self):
        """--flush-logs
Flush the MySQL server log files before starting the dump"""
        return """--flush-logs"""


    def flush_privileges(self):
        """--flush-privileges
Emit a FLUSH PRIVILEGES statement after dumping the mysql database"""
        return """--flush-privileges"""


    def help(self):
        """--help
Display help message and exit"""
        return """--help"""


    def hex_blob(self):
        """--hex-blob
Dump binary columns using hexadecimal notation (for example, 'abc'  becomes 0x616263)"""
        return """--hex-blob"""


    def host(self):
        """--host
Host to connect to (IP address or hostname)"""
        return """--host"""


    def ignore_table(self):
        """--ignore-table=db_name.tbl_name
Do not dump the given table"""
        return """--ignore-table=db_name.tbl_name"""


    def include_master_host_port(self):
        """--include-master-host-port
Include MASTER_HOST/MASTER_PORT options in CHANGE MASTER statement  produced with --dump-slave"""
        return """--include-master-host-port"""


    def insert_ignore(self):
        """--insert-ignore
Write INSERT IGNORE statements rather than INSERT statements"""
        return """--insert-ignore"""


    def lines_terminated_by(self):
        """--lines-terminated-by=string
This option is used with the --tab option and has the same meaning  as the corresponding clause for LOAD DATA INFILE"""
        return """--lines-terminated-by=string"""


    def lock_all_tables(self):
        """--lock-all-tables
Lock all tables across all databases"""
        return """--lock-all-tables"""


    def lock_tables(self):
        """--lock-tables
Lock all tables before dumping them"""
        return """--lock-tables"""


    def log_error(self):
        """--log-error=file_name
Append warnings and errors to the named file"""
        return """--log-error=file_name"""


    def master_data(self):
        """--master-data[=value]
Write the binary log file name and position to the output"""
        return """--master-data[=value]"""


    def max_allowed_packet(self):
        """--max_allowed_packet=value
The maximum packet length to send to or receive from the server"""
        return """--max_allowed_packet=value"""


    def net_buffer_length(self):
        """--net_buffer_length=value
The buffer size for TCP/IP and socket communication"""
        return """--net_buffer_length=value"""


    def no_autocommit(self):
        """--no-autocommit
Enclose the INSERT statements for each dumped table within SET  autocommit = 0 and COMMIT statements"""
        return """--no-autocommit"""


    def no_create_db(self):
        """--no-create-db
This option suppresses the CREATE DATABASE statements"""
        return """--no-create-db"""


    def no_create_info(self):
        """--no-create-info
Do not write CREATE TABLE statements that re-create each dumped  table"""
        return """--no-create-info"""


    def no_data(self):
        """--no-data
Do not dump table contents"""
        return """--no-data"""


    def no_set_names(self):
        """--no-set-names
Same as --skip-set-charset"""
        return """--no-set-names"""


    def no_tablespaces(self):
        """--no-tablespaces
Do not write any CREATE LOGFILE GROUP or CREATE TABLESPACE  statements in output"""
        return """--no-tablespaces"""


    def opt(self):
        """--opt
Shorthand for --add-drop-table --add-locks --create-options  --disable-keys --extended-insert --lock-tables --quick  --set-charset."""
        return """--opt"""


    def order_by_primary(self):
        """--order-by-primary
Dump each table's rows sorted by its primary key, or by its first  unique index"""
        return """--order-by-primary"""


    def password(self):
        """--password[=password]
The password to use when connecting to the server"""
        return """--password[=password]"""


    def pipe(self):
        """--pipe
On Windows, connect to server using a named pipe"""
        return """--pipe"""


    def plugin_dir(self):
        """--plugin-dir=path
The directory where plugins are located"""
        return """--plugin-dir=path"""


    def port(self):
        """--port=port_num
The TCP/IP port number to use for the connection"""
        return """--port=port_num"""


    def quick(self):
        """--quick
Retrieve rows for a table from the server a row at a time"""
        return """--quick"""


    def quote_names(self):
        """--quote-names
Quote identifiers within backtick characters"""
        return """--quote-names"""


    def replace(self):
        """--replace
Write REPLACE statements rather than INSERT statements"""
        return """--replace"""


    def result_file(self):
        """--result-file=file
Direct output to a given file"""
        return """--result-file=file"""


    def routines(self):
        """--routines
Dump stored routines (procedures and functions) from the dumped  databases"""
        return """--routines"""


    def set_charset(self):
        """--set-charset
Add SET NAMES default_character_set to the output"""
        return """--set-charset"""


    def single_transaction(self):
        """--single-transaction
This option issues a BEGIN SQL statement before dumping data from  the server"""
        return """--single-transaction"""


    def skip_add_drop_table(self):
        """--skip-add-drop-table
Do not add a DROP TABLE statement before each CREATE TABLE  statement"""
        return """--skip-add-drop-table"""


    def skip_add_locks(self):
        """--skip-add-locks
Do not add locks"""
        return """--skip-add-locks"""


    def skip_comments(self):
        """--skip-comments
Do not add comments to the dump file"""
        return """--skip-comments"""


    def skip_compact(self):
        """--skip-compact
Do not produce more compact output"""
        return """--skip-compact"""


    def skip_disable_keys(self):
        """--skip-disable-keys
Do not disable keys"""
        return """--skip-disable-keys"""


    def skip_extended_insert(self):
        """--skip-extended-insert
Turn off extended-insert"""
        return """--skip-extended-insert"""


    def skip_opt(self):
        """--skip-opt
Turn off the options set by --opt"""
        return """--skip-opt"""


    def skip_quick(self):
        """--skip-quick
Do not retrieve rows for a table from the server a row at a time"""
        return """--skip-quick"""


    def skip_quote_names(self):
        """--skip-quote-names
Do not quote identifiers"""
        return """--skip-quote-names"""


    def skip_set_charset(self):
        """--skip-set-charset
Suppress the SET NAMES statement"""
        return """--skip-set-charset"""


    def skip_triggers(self):
        """--skip-triggers
Do not dump triggers"""
        return """--skip-triggers"""


    def skip_tz_utc(self):
        """--skip-tz-utc
Turn off tz-utc"""
        return """--skip-tz-utc"""


    def ssl_ca(self):
        """--ssl-ca=file_name
The path to a file that contains a list of trusted SSL CAs"""
        return """--ssl-ca=file_name"""


    def ssl_capath(self):
        """--ssl-capath=dir_name
The path to a directory that contains trusted SSL CA certificates  in PEM format"""
        return """--ssl-capath=dir_name"""


    def ssl_cert(self):
        """--ssl-cert=file_name
The name of the SSL certificate file to use for establishing a  secure connection"""
        return """--ssl-cert=file_name"""


    def ssl_cipher(self):
        """--ssl-cipher=cipher_list
A list of allowable ciphers to use for SSL encryption"""
        return """--ssl-cipher=cipher_list"""


    def ssl_crl(self):
        """--ssl-crl=file_name
The path to a file that contains certificate revocation lists"""
        return """--ssl-crl=file_name"""


    def ssl_crlpath(self):
        """--ssl-crlpath=dir_name
The path to a directory that contains certificate revocation list  files"""
        return """--ssl-crlpath=dir_name"""


    def ssl_key(self):
        """--ssl-key=file_name
The name of the SSL key file to use for establishing a secure  connection"""
        return """--ssl-key=file_name"""


    def ssl_verify_server_cert(self):
        """--ssl-verify-server-cert
The server's Common Name value in its certificate is verified  against the host name used when connecting to the server"""
        return """--ssl-verify-server-cert"""


    def tab(self):
        """--tab=path
Produce tab-separated data files"""
        return """--tab=path"""


    def tables(self):
        """--tables
Override the --databases or -B option"""
        return """--tables"""


    def triggers(self):
        """--triggers
Dump triggers for each dumped table"""
        return """--triggers"""


    def tz_utc(self):
        """--tz-utc
Add SET TIME_ZONE='+00:00' to the dump file"""
        return """--tz-utc"""


    def user(self):
        """--user=user_name
The MySQL user name to use when connecting to the server"""
        return """--user=user_name"""


    def verbose(self):
        """--verbose
Verbose mode"""
        return """--verbose"""


    def version(self):
        """--version
Display version information and exit"""
        return """--version"""


    def where(self):
        """--where='where_condition'
Dump only rows selected by the given WHERE condition"""
        return """--where='where_condition'"""


    def xml(self):
        """--xml
Produce XML output"""
        return """--xml"""

dump_options=ConstantsObj()