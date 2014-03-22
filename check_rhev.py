#/usr/bin/env python
# 
# spearhead systems srl 2014
# based on check_rhev3.pl from https://github.com/ovido/check_rhev3/
#


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
parser.parse_args()
print args.echo

# rhev / ovirt defaults
rhevm_port  = 443          # default port
rhevm_api   = "/api"       # default api path
rhevm_timeout = 15         # default timeout
rhevm_user = None          # default username
rhevm_pass = None          # default password

# Variables
prog      = "check_rhev3"
version    = "0.0"
projecturl = "https://github.com/spearheadsys/check_rhev"
cookie     = "/tmp"   # default path to cookie file

o_rhevm_host   = None   # rhevm hostname
o_rhevm_port   = None   # rhevm port
o_rhevm_api    = None   # rhevm api path
o_version      = None   # version
o_timeout      = None   # timeout
o_warn         = None   # warning
o_crit         = None   # critical
o_auth         = None   # authentication
o_authfile     = None   # authentication file
o_ca_file      = None   # certificate authority
o_cookie       = None   # cookie authentication
o_rhev_dc      = None   # rhev data center
o_rhev_cluster = None   # rhev cluster
o_rhev_host    = None   # rhev host
o_rhev_storage = None   # rhev storage domain
o_rhev_vm      = None   # rhev vm
o_rhev_vmpool  = None   # rhev vm pool
o_check        = None
o_subcheck     = None
o_nics         = []
#@o_nics 

status  =  { "ok": "OK", "warning": "WARNING", "critical": "CRITICAL", "unknown": "UNKNOWN" }
ERRORS  = { "OK": 0, "WARNING": 1, "CRITICAL": 2, "UNKNOWN": 3 }

try:
  o_rhevm_host
except NameError:
  print "RHEV Manager hostname is missing.\n"
  print_usage()
else:
  print "sure, it was defined."


### perly
 if (! defined( $o_rhevm_host )){
    print "RHEV Manager hostname is missing.\n";
    print_usage();
    exit $ERRORS{$status{'unknown'}};
  }

## perly
 sub print_usage(){
  print "Usage: $0 [-v] -H <hostname> [-p <port>] -a <auth> | -f <authfile> [--ca-file <ca-file> [-o ] \n";
  print "       [-A <api>] [-t <timeout>] -D <data center> | -C <cluster> | -R <rhev host> [-n <nic>] \n";
  print "       | -S <storage domain> | -M <vm> | -P <vmpool> [-w <warn>] [-c <critical>] [-V] \n";
  print "       [-l <check>] [-s <subcheck>]\n"; 
}
