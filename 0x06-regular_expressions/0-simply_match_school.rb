#!/usr/bin/env ruby
if ARGV.length == 1
  string = ARGV[0]
  puts string.scan(/School+/).join
end
