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

    times = {
        'last_run':         data['time']['last_run'],
        'since_last_run':   int(time.time()) - data['time']['last_run'],
        'total':            data['time']['total'],
        'config_retrieval': data['time']['config_retrieval'],
    }
    val = collectd.Values(plugin='puppet',)
    val.type = 'puppet_time'
    val.values = list(times.values())
    val.dispatch()

    resources = {
        'total':              data['resources']['total'],
        'changed':            data['resources']['changed'],
        'corrective_change':  data['resources']['corrective_change'],
        'failed':             data['resources']['failed'],
        'failed_to_restart':  data['resources']['failed_to_restart'],
        'out_of_sync':        data['resources']['out_of_sync'],
        'restarted':          data['resources']['restarted'],
        'scheduled':          data['resources']['scheduled'],
        'skipped':            data['resources']['skipped'],
    }
    val = collectd.Values(plugin='puppet',)
    val.type = 'puppet_resources'
    val.values = list(resources.values())
    val.dispatch()

collectd.register_config(config_func)
collectd.register_read(read_func)
