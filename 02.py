sentence = raw_input("sentence:")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_width = (screen_width - box_width) // 2

print
print ' ' * left_width + '+'  + '-' *(box_width - 2) +  '+'
print ' ' * left_width + '| ' + ' ' *text_width      + ' |'
print ' ' * left_width + '| ' +      sentence        + ' |'
print ' ' * left_width + '| ' + ' ' *text_width      + ' |'
print ' ' * left_width + '+'  + '-' *(box_width - 2) +  '+'
print
