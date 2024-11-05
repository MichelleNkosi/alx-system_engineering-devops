#!/usr/bin/env ruby
# This script matches "htn" or "hbtn"

puts ARGV[0].scan(/hb?tn/).join
