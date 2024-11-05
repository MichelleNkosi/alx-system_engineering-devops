#!/usr/bin/env ruby
# This script extracts sender, receiver, and flags from TextMe log entries

input = ARGV[0]

# Match sender, receiver, and flags using regular expressions
sender = input.scan(/\[from:(.*?)\]/).flatten.first
receiver = input.scan(/\[to:(.*?)\]/).flatten.first
flags = input.scan(/\[flags:(.*?)\]/).flatten.first

# Print output in the format: [SENDER],[RECEIVER],[FLAGS]
puts "#{sender},#{receiver},#{flags}"
