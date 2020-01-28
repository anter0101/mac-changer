import subprocess
import re
import optparse
def parser_arguments():
          parser = optparse.OptionParser()
          parser.add_option("-i", "--interface", dest="interface", help="for enter your interface")
          parser.add_option("-m", "--mac", dest="new_mac", help="for enter your new_mac")
          (options, arguments) = parser.parse_args()
          if not options.interface:
             parser.error("[+]enter valid interface")
          elif not options.new_mac:
             parser.error("[+]enter valid mac ")
          else: return options
def __get_current_mac(interface):
    ifconfig_results = subprocess.check_output(["ifconfig", interface])
    ifconfig_results_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)
    if ifconfig_results_search:

        return ifconfig_results_search.group(0)
    else:
        print("[+] error cant read mac please try again")
def changer( interface, new_mac):
         print("[+]changing mac of " + interface + " to " + new_mac)
         subprocess.call(["ifconfig", interface, "down"])
         subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
         subprocess.call(["ifconfig", interface, "up"])
options=parser_arguments()
changer(options.interface, options.new_mac)
current_mac=__get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+]Great mac has been changed to ", current_mac)
else: print("[+] error cant read current_mac  please try again")


