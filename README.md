# Collectd Plugin for Puppet

## Configuration

```apache
TypesDB "/usr/share/collectd/puppet_types.db"
<LoadPlugin python>
  Globals true
</LoadPlugin>

<Plugin "python">
  LogTraces true
  Interactive false
  Import "puppet"
  PATH "/opt/puppetlabs/puppet/cache/state/last_run_summary.yaml"
</Plugin>
```


## Collectd Types
The plugin parses `/opt/puppetlabs/puppet/cache/state/last_run_summary.yaml`
and reports two collectd types.

### puppet_run

A count of numbers of resources
and duration of agent run and config_retrieval

* total
* changed
* corrective_change
* failed
* failed_to_restart
* out_of_sync
* restarted
* scheduled
* skipped
* time
* config_retrieval


#### puppet_time

All in units of seconds

* last_run   - epoch of last puppet run.





