#!/usr/bin/env ruby
# This script extracts and prints only uppercase letters from the given string

puts ARGV[0].scan(/[A-Z]/).join
