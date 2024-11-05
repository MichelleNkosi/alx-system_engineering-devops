#!/usr/bin/env ruby
# This script matches "hbtn" with 2 to 5 "t"s between "b" and "n"

puts ARGV[0].scan(/hbt{2,5}n/).join
