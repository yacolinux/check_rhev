#/usr/bin/env python
# 
# spearhead systems srl 2014
# based on check_rhev3.pl 
# https://github.com/ovido/check_rhev3/
# https://github.com/spearheadsys/check_rhev

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--versbose", help="Increase output verbosity", action="store_true")
parser.add_argument("-V", "--version", help="Print version information")
parser.add_argument("-H", "--host", help="The RHEVM/Ovirt host to query")
parser.add_argument("-p", "--port", help="The RHEVm/Ovir port", type=int)
parser.add_argument("-a", "--authorization", help="Username\@domain:password pair required for lgin to the REST API")
parser.parse_args()

# rhev / ovirt defaults
rhevm_port  = 443          # default port
rhevm_api   = "/api"       # default api path
rhevm_timeout = 15         # default timeout
rhevm_user = None          # default username
rhevm_pass = None          # default password

# Variables
prog       = "check_rhev"
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


### perly
# if (! defined( $o_rhevm_host )){
#    print "RHEV Manager hostname is missing.\n";
#    print_usage();
#    exit $ERRORS{$status{'unknown'}};
#  }
##


def print_usage():
    print "Usage:"

## perly
# sub print_usage(){
#  print "Usage: $0 [-v] -H <hostname> [-p <port>] -a <auth> | -f <authfile> [--ca-file <ca-file> [-o ] \n";
#  print "       [-A <api>] [-t <timeout>] -D <data center> | -C <cluster> | -R <rhev host> [-n <nic>] \n";
#  print "       | -S <storage domain> | -M <vm> | -P <vmpool> [-w <warn>] [-c <critical>] [-V] \n";
#  print "       [-l <check>] [-s <subcheck>]\n"; 
#}

# at one point, when we actually are doing something
# do something!
if args.verbosity:
    print "verbosity turned on"
