#!/usr/bin/env ruby
# This script matches "hbn", "hbtn", "hbttn", "hbtttn", "hbttttn" (t appearing zero or more times)

puts ARGV[0].scan(/hbt*n/).join
