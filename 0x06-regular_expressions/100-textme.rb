#!/usr/bin/env ruby
# This script displays: [SENDER],[RECEIVER],[FLAGS] of a sms
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(",")

