def format_name(f_name,s_name):
  if (f_name == "" or s_name == ""):
    return f"Name or second name are empty"
  formated_f_name = f_name.title()
  formated_s_name = s_name.title()
  return f"{formated_f_name} {formated_s_name}"
  #return f_name.title() + " " + s_name.title()
output = format_name("michal", "fityka")
print(format_name(input("What is your first name?"),input("What is your second name?")))
