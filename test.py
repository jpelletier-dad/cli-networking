import unittest
import subnets
import ipaddress

class TestSubnets(unittest.TestCase):
  def test_parser(self):
    # 00001010.00100001.00010100.00001100
    # |------|.|-||---|.|||||||-.-------|
    # dev.nodes.us-east1.b.private.12
    ip_str = '10.33.20.12'
    expected_subnets = ['dev', 'nodes', 'us-east1', 'b', 'private']
    self.assertEqual(subnets.ip_to_subnets(ip_str), expected_subnets)

  def test_find_subnet(self):
    parent = ipaddress.ip_network('10.33.0.0/18')
    new_prefix = 20
    ip_str = '10.33.20.12'
    ip_intf = ipaddress.ip_interface(ip_str)

    expected_index = 1
    expected_network = ipaddress.ip_network('10.33.16.0/20')

    resp = subnets.find_subnet(parent, new_prefix, ip_intf)
    self.assertIsNotNone(resp)
    self.assertEqual(resp[0], expected_index)
    self.assertEqual(resp[1], expected_network)

if __name__ == '__main__':
  unittest.main()
