is_old = True
is_licensed = True

if is_old:
  print("You are old enough to drive")
elif is_licensed:
  print("You can drive")
else:
  print("You are not old enough to drive")

if is_old and is_licensed:
  print("You can drive")

if is_old or is_licensed:
  print("You can drive")


# Ternary
is_friend = True
can_see_posts = "allowed" if is_friend else "not allowed"
print(can_see_posts)

# Short Circuiting
print(2 < 3 and 3 < 4)
print(2 > 3 and 3 < 4)

# Negate
print(not False)
