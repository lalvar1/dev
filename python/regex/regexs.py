import re
import sys

regex_pattern = r"^\S{3}\.\S{3}\.\S{3}\.\S{3}$"
test_string = '123.456.abc.def'
match = re.match(regex_pattern, test_string) is not None
match_search = re.search(regex_pattern, test_string)
match_findall = re.findall(regex_pattern, test_string)
print(str(match).lower())
print(match_search)
print(match_findall)
test_string = '1234.456.abc.def'
match = re.match(regex_pattern, test_string)
print(str(match).lower())

#------------------
# ipv4 and ipv6 regex
#number = int(input())
# for n in range(number):
#     string = input()
#     if re.match(r'^[0-2]?[0-9]{1,2}\.[0-2]?[0-9]{1,2}\.[0-2]?[0-9]{1,2}\.[0-2]?[0-9]{1,2}$', string):
#         print('IPv4')
#     elif re.match(r'^[0-9,a-f]{1,4}\:[0-9,a-f]{1,4}\:[0-9,a-f]{1,4}\:[0-9,a-f]{1,4}\:[0-9,a-f,A-F]{1,4}\:[0-9,a-f,A-F]{1,4}\:[0-9,a-f,A-F]{1,4}\:[0-9,a-f,A-F]{1,4}$', string):
#         print('IPv6')
#     else:
#         print('Neither')

#------------------
# email checker
# p=sys.stdin.read()
# emails = re.findall(r'\S+@\S+\.\S{1,3}',str(p))
# print(';'.join(sorted(list(set(emails)))))


#----------------------------
# html parser
# p=sys.stdin.read()
string = '<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p><div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>'
pattern = r'<a.*?href=\"(.*?)\".*?>(.*?)<\/a>'
matches = re.findall(pattern, string)
for match in matches:
    print('{},{}'.format(match[0], match[1]))


