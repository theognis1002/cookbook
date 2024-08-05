By default, PostgreSQL’s autovacuum process runs periodically to manage table bloat and maintain performance. The specific settings that control how often autovacuum runs are configurable, but here are the default values for key autovacuum parameters:

### Default Autovacuum Settings

1. `autovacuum_vacuum_threshold`:
   - Default: `50`
   - Description: The minimum number of updated or deleted tuples needed to trigger an autovacuum operation on a table. If a table has more changes than this threshold, autovacuum will be triggered.
2. `autovacuum_vacuum_scale_factor`:
   - Default: `0.2`
   - Description: A fraction of the number of tuples in the table that needs to be updated or deleted to trigger an autovacuum. For example, if a table has 1,000 rows, an autovacuum will be triggered if there are 200 (0.2 \* 1,000) updates or deletes.
3. `autovacuum_analyze_threshold`:
   - Default: `50`
   - Description: The minimum number of updated or deleted tuples needed to trigger an autovacuum analyze operation on a table.
4. `autovacuum_analyze_scale_factor`:
   - Default: `0.1`
   - Description: A fraction of the number of tuples in the table that needs to be updated to trigger an autovacuum analyze operation.
5. `autovacuum_naptime`:
   - Default: 1 minute
   - Description: The amount of time that the autovacuum process waits between successive checks for tables needing vacuuming. This is how often the autovacuum daemon wakes up to check for tables that need vacuuming or analyzing.
6. `autovacuum_vacuum_cost_delay`:
   - Default: `2ms`
   - Description: The delay between cost-based vacuum operations to prevent autovacuum from using excessive I/O resources.
7. `autovacuum_vacuum_cost_limit`:
   - Default: `200`
   - Description: The cost limit for each autovacuum operation. This helps to control the amount of I/O resources that autovacuum will consume.
