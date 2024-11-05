#!/usr/bin/env ruby
# This script matches "hbtn" with one or more "t"s between "b" and "n"

puts ARGV[0].scan(/hbt+n/).join
