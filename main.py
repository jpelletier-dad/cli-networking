#!/usr/bin/env python3
import sys, subnets

def main(argv):
  resp = subnets.ip_to_subnets(argv[0])
  print(resp)

if __name__ == "__main__":
  main(sys.argv[1:])
