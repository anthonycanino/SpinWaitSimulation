from optparse import OptionParser
import os
import random

def main():
  parser = OptionParser()
  parser.add_option("--threads", dest="threads", help="number of threads", type="int", metavar="INT")
  parser.add_option("--input_count", dest="input_count", help="number of prime numbers per threads", type="int", metavar="INT")
  parser.add_option("--complexity", dest="complexity", help="number between 0~31", type="int", metavar="INT")
  parser.add_option("--output", dest="output", help="file for output", type="string", metavar="STRING")

  (options, args) = parser.parse_args()

  if not options.input_count:
    parser.error("input_count required")

  if not options.complexity:
    parser.error("complexity required")

  if options.complexity >= 32:
    parser.error("complexity must be within 0~31")

  if not options.threads:
    options.threads = os.cpu_count()

  if not options.output:
    parser.error("output file must be specified")

  print(f"Generating {options.input_count} numbers for {options.threads} within the range 1 - 2^{options.complexity}")

  with open(options.output, "w+") as f:
    f.write(f"{options.threads} {options.input_count}\n")

    for i in range(0, options.threads):
      for c in range(0, options.input_count):
        if options.complexity != 0:
          r = random.randint(1, 2 ** options.complexity)
        else:
          r = c
        f.write(f"{i} {r}\n")

if __name__ == "__main__":
  main()