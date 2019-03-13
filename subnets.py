import ipaddress

SUBNET_IDS = [
  (11, ('ops', 'dev', 'stage', 'prod')),
  (16, ('ops', 'nodes', 'web')),
  (18, ('us-east1', 'us-west1')),
  (20, ('a', 'b', 'c', 'd')),
  (22, ('public', 'private'))
]

def ip_to_subnets(ip_str):
  ip_intf = ipaddress.ip_interface(ip_str)
  parent_subnet = ipaddress.ip_network('10.0.0.0/8')

  results = []
  for subnet_id in SUBNET_IDS:
    resp = find_subnet(parent_subnet, subnet_id[0], ip_intf)
    if resp is None:
      raise Exception("can't find subnet in ", subnet_id)

    index, parent_subnet = resp
    results.append(subnet_id[1][index])

  return results

def find_subnet(parent, new_prefix, ip_intf):
  i = 0
  # TODO: index_of?
  for subnet in parent.subnets(new_prefix=new_prefix):
    if subnet.supernet_of(ip_intf.network):
      return [i, subnet]
    i+=1
  return None
