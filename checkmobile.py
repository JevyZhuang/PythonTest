import re
pattern=r'(13[4-9]\d{8})$|(15[01289]\d{8})$'
mobile='13634222222'
match=re.match(pattern,mobile)
if match==None:
    print(mobile,"不是有效的中国移动号码")
else:
    print(mobile,"是有效的中国移动号码")
mobile="13144222221"
match=re.match(pattern,mobile)
if match==None:
    print(mobile,"不是有效的中国移动号码")
else:
    print(mobile,"是有效的中国移动号码")
