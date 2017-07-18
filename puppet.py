"""
collectd sensor for puppet's last_run_summary.yaml file.

To configure with collectd

<Plugin "python">
  LogTraces true
  Interactive false
  Import "puppet"
</Plugin>
"""

import time
import collectd
import yaml

PATH = "/opt/puppetlabs/puppet/cache/state/last_run_summary.yaml"

def config_func(config):
    """ accept configuration from collectd """
    path_set = False
    for node in config.children:
        key = node.key.lower()
        val = node.values[0]
        if key == 'path':
            global PATH
            PATH = val
            path_set = True
        else:
            collectd.info('puppet plugin: Unknown config key "%s"' % key)

    if path_set:
        collectd.info('puppet plugin: Using overridden path %s' % PATH)
    else:
        collectd.info('puppet plugin: Using default path %s' % PATH)

def read_func():
    """ open yaml file and publish  """
    with open(PATH, 'r') as stream:
        try:
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print exc

    # If a compile eorr the time and config_retrievial are not defined.
    # Would be better to return a NaN or None or something.
    times = [
        data['time']['last_run'],
        int(time.time()) - data['time']['last_run'],
        data['time']['total'] if 'total' in data['time'] else 0.0,
        data['time']['config_retrieval'] if 'config_retrieval' in data['time'] else 0.0,
    ]
    val = collectd.Values(plugin='puppet',)
    val.type = 'puppet_time'
    val.values = times
    val.dispatch()

    if 'resources' in data:
        resources = [
            data['resources']['total'],
            data['resources']['changed'],
            data['resources']['corrective_change'],
            data['resources']['failed'],
            data['resources']['failed_to_restart'],
            data['resources']['out_of_sync'],
            data['resources']['restarted'],
            data['resources']['scheduled'],
            data['resources']['skipped'],
        ]
        val = collectd.Values(plugin='puppet',)
        val.type = 'puppet_resources'
        val.values = resources
        val.dispatch()

collectd.register_config(config_func)
collectd.register_read(read_func)
