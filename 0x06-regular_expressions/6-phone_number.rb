#!/usr/bin/env ruby
# This script matches a string that is exactly a 10-digit phone number

puts ARGV[0].scan(/^\d{10}$/).join
